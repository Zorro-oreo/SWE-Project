class adminRepo:
    def __init__(self, db_conn, adminID):

        self.db = db_conn
        self.pID = adminID

    def getLogin(self, id, password=None):
        if password:
            return self.db.execute("""SELECT aID, aname, pass FROM Admin WHERE aID = ? AND pass = ?""", (id, password)).fetchone()
        else:
            return self.db.execute("""SELECT aID, aname, pass FROM Admin WHERE aID = ?""", (id,)).fetchone()
    
    def add_student(self, s_id, name, password):
        try:
            self.db.execute("INSERT INTO Student (stID, sname, pass) VALUES (?, ?, ?)", (s_id, name, password))
            self.db.commit()
            return f"""Successfully added {name}"""
        except Exception as e:
            return f"""Error: {e}"""
        
    def add_prof(self, p_id, name, password):
        try:
            self.db.execute("INSERT INTO Professor (pID, pname, pass) VALUES (?, ?, ?)", (p_id, name, password))
            self.db.commit()
            return f"""Successfully added {name}"""
        except Exception as e:
            return f"""Error: {e}"""
        
    def add_admin(self, a_id, name, password):
        try:
            self.db.execute("INSERT INTO Admin (aID, aname, pass) VALUES (?, ?, ?)", (a_id, name, password))
            self.db.commit()
            return f"""Successfully added {name}"""
        except Exception as e:
            return f"""Error: {e}"""

    def get_all_students(self):
        return self.db.execute("SELECT stID, sname FROM Student").fetchall()
    
    def get_all_professors(self):
        return self.db.execute("SELECT pID, pname FROM Professor").fetchall()
    
    def get_student_by_id(self, student_id):
        return self.db.execute("SELECT stID, sname FROM Student WHERE stID = ?", (student_id,)).fetchone()
    
    def get_professor_by_id(self, professor_id):
        return self.db.execute("SELECT pID, pname FROM Professor WHERE pID = ?", (professor_id,)).fetchone()
    
    def update_student(self, student_id, name, password=None):
        try:
            if password:
                self.db.execute("UPDATE Student SET sname = ?, pass = ? WHERE stID = ?", (name, password, student_id))
            else:
                self.db.execute("UPDATE Student SET sname = ? WHERE stID = ?", (name, student_id))
            self.db.commit()
            return f"""Successfully updated student {student_id}"""
        except Exception as e:
            return f"""Error: {e}"""
    
    def update_professor(self, professor_id, name, password=None):
        try:
            if password:
                self.db.execute("UPDATE Professor SET pname = ?, pass = ? WHERE pID = ?", (name, password, professor_id))
            else:
                self.db.execute("UPDATE Professor SET pname = ? WHERE pID = ?", (name, professor_id))
            self.db.commit()
            return f"""Successfully updated professor {professor_id}"""
        except Exception as e:
            return f"""Error: {e}"""
    
    def delete_student(self, student_id):
        try:
            self.db.execute("DELETE FROM Student WHERE stID = ?", (student_id,))
            self.db.commit()
            return f"""Successfully deleted student {student_id}"""
        except Exception as e:
            return f"""Error: {e}"""
    
    def delete_professor(self, professor_id):
        try:
            self.db.execute("DELETE FROM Professor WHERE pID = ?", (professor_id,))
            self.db.commit()
            return f"""Successfully deleted professor {professor_id}"""
        except Exception as e:
            return f"""Error: {e}"""

    def get_all_courses(self):
        return self.db.execute("""
            SELECT c.cID, c.cname, c.PrID, p.pname 
            FROM Course c 
            LEFT JOIN Professor p ON c.PrID = p.pID
        """).fetchall()
    
    def get_course_by_id(self, course_id):
        return self.db.execute("""
            SELECT c.cID, c.cname, c.PrID, p.pname 
            FROM Course c 
            LEFT JOIN Professor p ON c.PrID = p.pID
            WHERE c.cID = ?
        """, (course_id,)).fetchone()
    
    def assign_professor_to_course(self, course_id, professor_id):
        try:
            # Check if professor exists
            prof = self.db.execute("SELECT pID FROM Professor WHERE pID = ?", (professor_id,)).fetchone()
            if not prof:
                return f"Error: Professor {professor_id} not found"
            
            # Update course professor
            self.db.execute("UPDATE Course SET PrID = ? WHERE cID = ?", (professor_id, course_id))
            self.db.commit()
            return f"Successfully assigned professor {professor_id} to course {course_id}"
        except Exception as e:
            return f"Error: {e}"
    
    def add_course(self, c_id, cname, capacity, semester, credits, professor_id):
        try:
            self.db.execute(
                "INSERT INTO Course (cID, cname, capacity, semester, credits, PrID) VALUES (?, ?, ?, ?, ?, ?)",
                (c_id, cname, capacity, semester, credits, professor_id),
            )
            self.db.commit()
            return "Course added successfully."
        except Exception as e:
            return f"Error: {e}"

    
    def remove_course(self, c_id):
        try:
            self.db.execute(
                "DELETE FROM Course WHERE cID = ?",
                (c_id,),
            )
            self.db.commit()
            return "Course removed successfully."
        except Exception as e:
            return f"Error: {e}"

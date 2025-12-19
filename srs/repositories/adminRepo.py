class adminRepo:
    def __init__(self, db_conn, adminID):

        self.db = db_conn
        self.pID = adminID

    def getLogin(self, id, password):

        return self.db.execute("""SELECT aname FROM Admin WHERE aID = ? AND pass = ?""", (id, password)).fetchone()
    
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
            self.db.execute("INSERT INTO Student (aID, aname, pass) VALUES (?, ?, ?)", (a_id, name, password))
            self.db.commit()
            return f"""Successfully added {name}"""
        except Exception as e:
            return f"""Error: {e}"""

    def add_course(self, c_id, cname, capacity, professor_id):
        self.db.execute(
            "INSERT INTO Course (cID, cname, capacity, PrID) VALUES (?, ?, ?, ?)",
            (c_id, cname, capacity, professor_id),
        )
        self.db.commit()
        return "Course added successfully."
    
    def remove_course(self, c_id):
        self.db.execute(
            "DELETE FROM Course WHERE cID = ?",
            (c_id,),
        )
        self.db.commit()
        return "Course removed successfully."

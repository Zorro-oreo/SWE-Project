class studentRepo:
    def __init__(self, db_conn, studentID):
        self.db = db_conn
        self.sID = studentID

    def RegisterCourse(self, course_id):

        valid_course = self.db.execute("SELECT cID, capacity FROM Course WHERE cID = ?", (course_id,)).fetchone()
        
        if valid_course is None:
            raise Exception("The selected Course does not exist.")

        taken = self.db.execute("SELECT COUNT(*) FROM Registered_In WHERE coID = ?", (course_id,)).fetchone()[0]

        if(taken >= valid_course["capacity"]):
            raise Exception(f"{course_id} is full ({taken}/{valid_course['capacity']} seats taken).")

        self.db.execute("""
                INSERT INTO Registered_In VALUES(?, ?, NULL)
                """, (self.sID, course_id))
        self.db.commit()

    def getAvailableCourses(self):
        return self.db.execute("""
            SELECT c.cID, c.cname, c.credits, COALESCE(p.pname, 'TBA')
            FROM Course c
            LEFT JOIN Professor p ON c.PrID = p.pID
            WHERE c.cID NOT IN (
                SELECT coID FROM Registered_In WHERE stuID = ?
            )
        """, (self.sID,)).fetchall()

    def get_registered_courses(self):
        sql = """
            SELECT c.cID, c.cname, c.credits, COALESCE(p.pname, 'TBA')
            FROM Course c
            JOIN Registered_In r ON c.cID = r.coID
            LEFT JOIN Professor p ON c.PrID = p.pID
            WHERE r.stuID = ?
        """
        cursor = self.db.execute(sql, (self.sID,))
        rows = cursor.fetchall()
        return [{'cID': row[0], 'cName': row[1], 'credits': row[2], 'pname': row[3]} for row in rows]

    def get_grades(self):

        sql = """SELECT c.cname, r.grade, c.credits FROM Course c 
                join Registered_In r ON c.cID = r.coID 
                WHERE r.stuID = ?;"""
        cursor = self.db.execute(sql, (self.sID,))
        rows = cursor.fetchall()
        grades = [{'course': row[0], 'grade': row[1], 'credits': row[2]} for row in rows]
        return grades
    
    def getLogin(self, id, password=None):
        if password:
            return self.db.execute("""SELECT stID, sname, pass FROM Student WHERE stID = ? AND pass = ?""", (id, password)).fetchone()
        else:
            return self.db.execute("""SELECT stID, sname, pass FROM Student WHERE stID = ?""", (id,)).fetchone()

    def DropCourse(self, course_id):
        cursor = self.db.execute(
            "DELETE FROM Registered_In WHERE stuID = ? AND coID = ?",
          (self.sID, course_id),
        )
        self.db.commit()

        if(cursor.rowcount == 0):
            raise Exception("You're not registered in this course!")
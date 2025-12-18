class studentRepo:
    def __init__(self, db_conn, studentID):
        self.db = db_conn
        self.sID = studentID

    def RegisterCourse(self, course_id):
        

        valid_course = self.db.execute("SELECT cID FROM Course WHERE cID = ?", (course_id,)).fetchone()
        
        if valid_course is None:
            raise Exception("The selected Course does not exist.")

        self.db.execute("""
                INSERT INTO Registered_In VALUES(?, ?, NULL)
                """, (self.sID, course_id))
        self.db.commit()

    def get_grades(self):

        sql = """SELECT c.cname, r.grade FROM Course c 
                join Registered_In r ON c.cID = r.coID 
                WHERE r.stuID = ?;"""
        cursor = self.db.execute(sql, (self.sID,))
        rows = cursor.fetchall()
        grades = [{'course': row[0], 'grade': row[1]} for row in rows]
        return grades
    
    def getLogin(self, id, password=None):
        if password:
            return self.db.execute("""SELECT stID, sname, pass FROM Student WHERE stID = ? AND pass = ?""", (id, password)).fetchone()
        else:
            return self.db.execute("""SELECT stID, sname, pass FROM Student WHERE stID = ?""", (id,)).fetchone()

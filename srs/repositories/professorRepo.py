class professorRepo:
    def __init__(self, db_conn, professorID):

        self.db = db_conn
        self.pID = professorID

    def get_students_in_course(self, course_id: str):

        sql = """SELECT s.stID, s.sname, r.grade
                 FROM Student s
                 JOIN Registered_In r ON s.stID = r.stuID
                 JOIN Course c        ON r.coID = c.cID
                 WHERE c.cID = ? AND c.PrID = ?;
              """

        rows = self.db.execute(sql, (course_id, self.pID)).fetchall()

        students = [dict(row) for row in rows]

        return students
    
    def assign_grade(self, student_id, course_id, grade):

        cursor = self.db.cursor()
        
        cursor.execute('''
            UPDATE Registered_In 
            SET grade = ? 
            WHERE stuID = ? AND coID = ?
        ''', (grade, student_id, course_id))
        
        self.db.commit()
        self.db.close()
        
        return f"Grade {grade} has been assigned to student {student_id} for course {course_id}"
    
    def getLogin(self, id, password):

        return self.db.execute("""SELECT pname FROM Professor WHERE pID = ? AND pass = ?""", (id, password)).fetchone()
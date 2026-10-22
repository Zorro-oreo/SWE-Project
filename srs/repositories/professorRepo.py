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

        cursor = self.db.execute(sql, (course_id, self.pID))
        rows = cursor.fetchall()

        students = [dict(row) for row in rows]

        return students
    
    def assign_grade(self, student_id, course_id, grade):

        course = self.db.execute(
            "SELECT PrID FROM Course WHERE cID = ?", (course_id,)
        ).fetchone()

        if course is None:
            return f"Error: course {course_id} does not exist"

        if course["PrID"] != self.pID:
            return f"Error: you are not the instructor of {course_id}"

        cursor = self.db.execute('''
            UPDATE Registered_In 
            SET grade = ? 
            WHERE stuID = ? AND coID = ?
        ''', (grade, student_id, course_id))
        
        self.db.commit()

        if cursor.rowcount == 0:
            return f"Error: student {student_id} is not registered in {course_id}"
        
        return f"Grade {grade} has been assigned to student {student_id} for course {course_id}"
    
    def getLogin(self, id, password=None):
        if password:
            return self.db.execute("""SELECT pID, pname, pass FROM Professor WHERE pID = ? AND pass = ?""", (id, password)).fetchone()
        else:
            return self.db.execute("""SELECT pID, pname, pass FROM Professor WHERE pID = ?""", (id,)).fetchone()
        
    def get_courses(self):
        sql = """SELECT cID, cname FROM Course WHERE PrID = ?;"""
        cursor = self.db.execute(sql, (self.pID,))
        rows = cursor.fetchall()
        courses = [{'course_id': row[0], 'course_name': row[1]} for row in rows]
        return courses
    
    def RemoveStudent(self, student_id, course_id):

        course = self.db.execute(
            "SELECT PrID FROM Course WHERE cID = ?", (course_id,)
        ).fetchone()

        if course is None or course["PrID"] != self.pID:
            return f"Error: you are not the instructor of {course_id}"

        cursor = self.db.execute('''
            DELETE FROM Registered_In 
            WHERE stuID = ? AND coID = ?''', (student_id, course_id))

        self.db.commit()

        if cursor.rowcount == 0:
            return f"Error: student {student_id} is not registered in {course_id}"
            
        return f"Student {student_id} has been removed from course {course_id}"
        
    
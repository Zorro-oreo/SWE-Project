from db import get_db
class Professor:
    def _init_(self, pID: str, pname: str, password: str):
        self.pID = pID       
        self.pname = pname   
        self.password = password  

    def get_students_in_course(self, course_id: str):
        db = get_db()

        sql = """SELECT s.stID, s.sname, r.grade
                 FROM Student s
                 JOIN Registered_In r ON s.stID = r.stuID
                 JOIN Course c        ON r.coID = c.cID
                 WHERE c.cID = ? AND c.PrID = ?;
              """

        rows = db.execute(sql, (course_id, self.pID)).fetchall()

        students = [dict(row) for row in rows]

        return students
    
    def assign_grade(self, student_id, course_id, grade):
        import sqlite3
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        
        cursor.execute('''
            UPDATE Registered_In 
            SET grade = ? 
            WHERE stuID = ? AND coID = ?
        ''', (grade, student_id, course_id))
        
        db.commit()
        db.close()
        
        return f"Grade {grade} has been assigned to student {student_id} for course {course_id}"
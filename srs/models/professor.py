from flask_login import UserMixin
from srs.db import get_db

class Professor(UserMixin):
    def __init__(self, pID: str, pname: str, password: str):
        self.pID = pID       
        self.pname = pname   
        self.password = password

    def get_id(self):
        return f"professor_{self.pID}"

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
        
        cursor.execute('SELECT cID FROM Course WHERE cID = ? AND PrID = ?', (course_id, self.pID))
        if not cursor.fetchone():
            db.close()
            return "You don't teach this course"
        
        cursor.execute('UPDATE Registered_In SET grade = ? WHERE stuID = ? AND coID = ?', (grade, student_id, course_id))
        db.commit()
        db.close()
        return "Grade assigned"
    
    def get_students_in_course(self, course_id):
        import sqlite3
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        
        cursor.execute('SELECT cID FROM Course WHERE cID = ? AND PrID = ?', (course_id, self.pID))
        if not cursor.fetchone():
            db.close()
            return []
        
        cursor.execute('SELECT s.stID, s.sname FROM Student s JOIN Registered_In r ON s.stID = r.stuID WHERE r.coID = ?', (course_id,))
        students = cursor.fetchall()
        db.close()
        return students

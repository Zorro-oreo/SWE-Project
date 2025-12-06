from db import get_db

class Student:
    def __init__(self, sID: str, sname: str, password: str):
        self.sID = sID
        self.sname = sname
        self.password = password

    def RegisterCourse(self, course_id):
        
        db = get_db()

        db.execute("""
                INSERT INTO Registered_In VALUES(?, ?, None)
                """, (self.sID, course_id))
        db.commit()
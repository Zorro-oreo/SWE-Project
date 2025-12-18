from flask_login import UserMixin

class Student(UserMixin):
    def __init__(self, sID: str, sname: str, password: str):
        self.sID = sID
        self.sname = sname
        self.password = password

    def get_id(self):
        return f"student_{self.sID}"
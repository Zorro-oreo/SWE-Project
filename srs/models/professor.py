from flask_login import UserMixin

class Professor(UserMixin):
    def __init__(self, pID: str, pname: str, password: str):
        self.pID = pID       
        self.pname = pname   
        self.password = password

    def get_id(self):
        return f"professor_{self.pID}"
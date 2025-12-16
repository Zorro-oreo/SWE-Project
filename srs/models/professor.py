from db import get_db
class Professor:
    def _init_(self, pID: str, pname: str, password: str):
        self.pID = pID       
        self.pname = pname   
        self.password = password  
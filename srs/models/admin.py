from flask_login import UserMixin

class Admin(UserMixin):
    def __init__ (self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    
    def get_id(self):
        return f"admin_{self.id}"

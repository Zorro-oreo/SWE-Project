class adminRepo:
    def __init__(self, db_conn, adminID):

        self.db = db_conn
        self.pID = adminID

    def getLogin(self, id, password=None):
        if password:
            return self.db.execute("""SELECT aID, aname, pass FROM Admin WHERE aID = ? AND pass = ?""", (id, password)).fetchone()
        else:
            return self.db.execute("""SELECT aID, aname, pass FROM Admin WHERE aID = ?""", (id,)).fetchone()
    
    def add_student(self, s_id, name, password):
        try:
            self.db.execute("INSERT INTO Student (stID, sname, pass) VALUES (?, ?, ?)", (s_id, name, password))
            self.db.commit()
            return f"""Successfully added {name}"""
        except Exception as e:
            return f"""Error: {e}"""
        
    def add_prof(self, p_id, name, password):
        try:
            self.db.execute("INSERT INTO Professor (pID, pname, pass) VALUES (?, ?, ?)", (p_id, name, password))
            self.db.commit()
            return f"""Successfully added {name}"""
        except Exception as e:
            return f"""Error: {e}"""
        
    def add_admin(self, a_id, name, password):
        try:
            self.db.execute("INSERT INTO Student (aID, aname, pass) VALUES (?, ?, ?)", (a_id, name, password))
            self.db.commit()
            return f"""Successfully added {name}"""
        except Exception as e:
            return f"""Error: {e}"""
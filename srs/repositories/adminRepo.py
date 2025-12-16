class adminRepo:
    def __init__(self, db_conn, adminID):

        self.db = db_conn
        self.pID = adminID

    def getLogin(self, id, password):

        return self.db.execute("""SELECT aname FROM Admin WHERE aID = ? AND pass = ?""", (id, password)).fetchone()
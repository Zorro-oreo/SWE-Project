from flask import Flask, g, render_template, request, redirect, session
import sqlite3
from config import DATABASE_PATH

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(arg=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with app.open_resource("database\\schema.sql", mode="r") as f:
        db.executescript(f.read())
    db.commit()

app = Flask(__name__)
app.secret_key = "prjct"

app.teardown_appcontext(close_db)

@app.route("/init")
def init():
    init_db()
    return "DB initialized."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/StudentLogin.html")
def studentlogin():
    return render_template("StudentLogin.html")

@app.route("/Slogin", methods=["POST"])
def student_login():
    id = request.form["id"]
    password = request.form["password"]

    db = get_db()
    
    studentData = db.execute("""SELECT sname FROM Student WHERE stID = ? AND pass = ?""", (id, password)).fetchone()

    if (studentData):

        session["username"] = studentData['sname']
        session["type"] = "Student"
        session["userID"] = id

        return redirect("/StudentHome")
    else:
        return "Credentials incorrect."
    
@app.route("/ProfessorLogin.html")
def professorlogin():
    return render_template("ProfessorLogin.html")

@app.route("/StudentHome")
def sHome():
    return render_template("StudentHome.html", username = session["username"])

@app.route("/Plogin", methods=["POST"])
def professor_login():
    id = request.form["id"]
    password = request.form["password"]

    db = get_db()
    
    profData = db.execute("""SELECT pname FROM Professor WHERE pID = ? AND pass = ?""", (id, password)).fetchone()

    if (profData):

        session["username"] = profData['pname']
        session["type"] = "Professor"
        session["userID"] = id

        return redirect("/ProfessorHome")
    else:
        return "Credentials incorrect."

@app.route("/ProfessorHome")
def pHome():
    return render_template("ProfessorHome.html", username = session["username"])

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, session
from config import DATABASE_PATH
from controllers.student_controller import student_bp
from controllers.professor_controller import professor_bp
from db import get_db, close_db

def init_db():
    db = get_db()
    with app.open_resource("database\\schema.sql", mode="r") as f:
        db.executescript(f.read())

    with app.open_resource("database\\data.sql", mode="r") as f:
            db.executescript(f.read())
    
    db.commit()

app = Flask(__name__)
app.secret_key = "prjct"

app.register_blueprint(student_bp)
app.register_blueprint(professor_bp)

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
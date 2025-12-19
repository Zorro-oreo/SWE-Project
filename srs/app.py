import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import timedelta
from srs.config import DATABASE_PATH
from srs.controllers.student_controller import student_bp
from srs.controllers.professor_controller import professor_bp
from srs.controllers.admin_controller import admin_bp
from srs.repositories.studentRepo import studentRepo
from srs.repositories.professorRepo import professorRepo
from srs.repositories.adminRepo import adminRepo
from srs.models.student import Student
from srs.models.professor import Professor
from srs.models.admin import Admin
from srs.db import get_db, close_db

def init_db():
    db = get_db()
    with app.open_resource("database\\schema.sql", mode="r") as f:
        db.executescript(f.read())

    with app.open_resource("database\\data.sql", mode="r") as f:
        db.executescript(f.read())
    
    db.commit()

app = Flask(__name__)
app.secret_key = "prjct"
app.config["REMEMBER_COOKIE_DURATION"] = timedelta(days=7)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "home"

@login_manager.user_loader
def LoadUser(UserToken):
    try:
        UserType, UserID = UserToken.split("_")
    except ValueError:
        return None
    db = get_db()
    if UserType == "student":
        UserData = studentRepo(db, UserID).getLogin(UserID)
        if UserData:
            return Student(UserData['stID'], UserData['sname'], UserData['pass'])
    elif UserType == "professor":
        UserData = professorRepo(db, UserID).getLogin(UserID)
        if UserData:
            return Professor(UserData['pID'], UserData['pname'], UserData['pass'])
    elif UserType == "admin":
        UserData = adminRepo(db, UserID).getLogin(UserID)
        if UserData:
            return Admin(UserData['aID'], UserData['aname'], UserData['pass'])
    return None


app.register_blueprint(student_bp)
app.register_blueprint(professor_bp)
app.register_blueprint(admin_bp)

app.teardown_appcontext(close_db)


@app.route("/init")
def init():
    init_db()
    return "DB initialized."

@app.route("/")
def home():
    if current_user.is_authenticated:
        if isinstance(current_user, Student):
            return redirect("/StudentHome")
        elif isinstance(current_user, Professor):
            return redirect("/ProfessorHome")
        elif isinstance(current_user, Admin):
            return redirect("/AdminHome")
    return render_template("index.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route("/StudentLogin.html")
def studentlogin():
    return render_template("StudentLogin.html")

@app.route("/Slogin", methods=["POST"])
def student_login():
    id = request.form["id"]
    password = request.form["password"]

    remember = True

    db = get_db()
    
    studentData = studentRepo(db, id).getLogin(id, password)

    if (studentData):

        User = Student(studentData['stID'], studentData['sname'], studentData['pass'])
        login_user(User, remember=remember)

        return redirect("/StudentHome")
    else:
        return "Credentials incorrect."
    
@app.route("/ProfessorLogin.html")
def professorlogin():
    return render_template("ProfessorLogin.html")

@app.route("/StudentHome")
def sHome():
    if not current_user.is_authenticated:
        return redirect("/")
    return render_template("StudentHome.html", username = current_user.sname)

@app.route("/Plogin", methods=["POST"])
def professor_login():
    id = request.form["id"]
    password = request.form["password"]

    remember = True

    db = get_db()
    
    profData = professorRepo(db, id).getLogin(id, password)

    if (profData):

        User = Professor(profData['pID'], profData['pname'], profData['pass'])
        login_user(User, remember=remember)

        return redirect("/ProfessorHome")
    else:
        return "Credentials incorrect."

@app.route("/ProfessorHome")
def pHome():
    if not current_user.is_authenticated:
        return redirect("/")
    
    db = get_db()
    courses = professorRepo(db, current_user.pID).get_courses()

    return render_template("ProfessorHome.html", username = current_user.pname, courses=courses)

@app.route("/AdminLogin.html")
def adminlogin():
    return render_template("AdminLogin.html")

@app.route("/Alogin", methods=["POST"])
def admin_login():
    id = request.form["id"]
    password = request.form["password"]

    remember = True

    db = get_db()
    
    adminData = adminRepo(db, id).getLogin(id, password)

    if (adminData):

        User = Admin(adminData['aID'], adminData['aname'], adminData['pass'])
        login_user(User, remember=remember)

        return redirect("/AdminHome")
    else:
        return "Credentials incorrect."
    
@app.route("/AdminHome")
def ahome():
    if not current_user.is_authenticated:
        return redirect("/")
    return render_template("AdminHome.html", username = current_user.username)

if __name__ == "__main__":
    app.run(debug=True)

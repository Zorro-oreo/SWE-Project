from flask import Blueprint, render_template, session, request
from flask_login import login_required, current_user
from srs.models.professor import Professor
from srs.repositories.professorRepo import professorRepo
from srs.db import get_db

professor_bp = Blueprint("professor", __name__, url_prefix="/professor")

@professor_bp.route("/courses/<c_id>/students")
@login_required
def get_students_in_course(c_id):
    prof = current_user
    db = get_db()
    repo = professorRepo(db, prof.pID)
    return render_template(
        "view_students.html",
        professor=prof,
        course_id=c_id,
        students=repo.get_students_in_course(c_id)
    )

@professor_bp.route('/assign_grade', methods=['GET', 'POST'])
@login_required
def assign_grade():
    if request.method == 'GET':
        return render_template('Grade.html')
    
    professor_id = current_user.pID
    
    student_id = request.form.get("student_id")
    course_id = request.form.get("course_id")
    grade = request.form.get("grade")
    
    db = get_db()
    repo = professorRepo(db, professor_id)
    result = repo.assign_grade(student_id, course_id, grade)

    return result

@professor_bp.route("/ProfessorHome")
@login_required
def view_courses():
    professor_id = current_user.pID
    
    db = get_db()
    repo = professorRepo(db, professor_id)
    courses = repo.get_courses()
    return render_template("ProfessorHome.html", courses=courses)
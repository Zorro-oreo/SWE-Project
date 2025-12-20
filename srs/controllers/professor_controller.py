from flask import Blueprint, render_template, session, request
from flask_login import login_required, current_user
from srs.models.professor import Professor
from srs.repositories.professorRepo import professorRepo
from srs.db import get_db

professor_bp = Blueprint("professor", __name__, url_prefix="/professor")

@professor_bp.route("/courses/<c_id>/students")
@login_required
def get_students_in_course(c_id):
    db = get_db()
    professor_id = current_user.pID
    repo = professorRepo(db, professor_id)
    students = repo.get_students_in_course(c_id)
    return render_template(
        "view_students.html",
        professor=current_user,
        course_id=c_id,
        students=students,
    )

@professor_bp.route('/assign_grade', methods=['POST'])
@login_required
def assign_grade():
    db = get_db()
    professor_id = current_user.pID
    repo = professorRepo(db, professor_id)
    
    student_id = request.form.get("student_id")
    course_id = request.form.get("course_id")
    grade = request.form.get("grade")
    
    result = repo.assign_grade(student_id, course_id, grade)

    return result

@professor_bp.route('/courses')
@login_required
def view_courses():
    db = get_db()
    professor_id = current_user.pID
    repo = professorRepo(db, professor_id)
    
    courses = repo.get_courses()

    return render_template("ProfessorHome.html", courses=courses)
from flask import Blueprint, render_template, session, request
from flask_login import login_required, current_user
from srs.models.professor import Professor
from srs.repositories.professorRepo import professorRepo

professor_bp = Blueprint("professor", __name__, url_prefix="/professor")

@professor_bp.route("/courses/<c_id>/students")
@login_required
def get_students_in_course(c_id):
    prof = current_user
    students = professorRepo.get_students_in_course(c_id)
    return render_template(
        "view_students.html",
        professor=prof,
        course_id=c_id,
        students=students,
    )

@professor_bp.route('/assign_grade', methods=['POST'])
@login_required
def assign_grade():
    professor_id = current_user.pID
    
    student_id = request.form.get("student_id")
    course_id = request.form.get("course_id")
    grade = request.form.get("grade")
    
    result = professorRepo.assign_grade(student_id, course_id, grade)

    return result

def view_courses():
    professor_id = current_user.pID
    
    courses = professorRepo.get_courses(professor_id)

    return render_template("ProfessorHome.html", courses=courses)
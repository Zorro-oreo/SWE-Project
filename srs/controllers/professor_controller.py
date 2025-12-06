from flask import Blueprint, render_template, session, request
from srs.models import Course
from srs.models.professor import Professor

professor_bp = Blueprint("professor", __name__, url_prefix="/professor")

@professor_bp.route("/<p_id>/courses/<c_id>/students")
def get_students_in_course(p_id, c_id):
    prof = Professor(pID=p_id, pname="", password="")
    students = prof.get_students_in_course(c_id)
    return render_template(
        "professor_students.html",
        professor=prof,
        course_id=c_id,
        students=students,
    )

def assign_grade():
    professor_id = session.get('professor_id')
    if not professor_id:
        return "Not logged in"
    
    student_id = request.form.get("student_id")
    course_id = request.form.get("course_id")
    grade = request.form.get("grade")
    
    professor = Professor(pID=professor_id, pname="", password="")
    result = professor.assign_grade(student_id, course_id, grade)
    return result
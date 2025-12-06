from flask import Blueprint, render_template, session, request
from models.professor import Professor

professor_bp = Blueprint("professor", _name_, url_prefix="/professor")

@professor_bp.route("/courses/<c_id>/students")
def get_students_in_course(c_id):
    p_id = session["userID"]
    p_name = session.get("pname", "")
    prof = Professor(pID=p_id, pname=p_name, password="")
    students = prof.get_students_in_course(c_id)
    return render_template(
        "professor_students.html",
        professor=prof,
        course_id=c_id,
        students=students,
    )

def assign_grade():
    professor_id = session.get('userID')
    if not professor_id:
        return "Not logged in"
    
    student_id = request.form.get("student_id")
    course_id = request.form.get("course_id")
    grade = request.form.get("grade")
    
    professor = Professor(pID=professor_id, pname="", password="")
    result = professor.assign_grade(student_id, course_id, grade)

    return result

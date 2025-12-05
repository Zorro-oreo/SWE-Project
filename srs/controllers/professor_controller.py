from flask import Blueprint, render_template
from professor import Professor

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

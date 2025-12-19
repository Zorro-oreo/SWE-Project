from flask import Blueprint, render_template, request, session
from flask_login import login_required, current_user
from srs.repositories.adminRepo import adminRepo
from srs.db import get_db

admin_bp = Blueprint("admin", __name__)

@admin_bp.route('/ManageUsers')
@login_required
def manage():

    return render_template("ManageUsers.html")

@admin_bp.route("/AddUser", methods=["POST"])
@login_required
def addUser():

    type = request.form["usertype"]
    id = request.form["id"]
    name = request.form["name"]
    password = request.form["password"]
    
    db = get_db()
    admin_id = current_user.id

    status = ""

    if (type == "Student"):

        status = adminRepo(db, admin_id).add_student(id, name, password)

    elif (type == "Professor"):

        status = adminRepo(db, admin_id).add_prof(id, name, password)

    elif (type == "Admin"):

        status = adminRepo(db, admin_id).add_admin(id, name, password)

    return render_template("ManageUsers.html", message = status)
import pytest
from unittest.mock import MagicMock, patch

@patch("srs.controllers.admin_controller.adminRepo")
@patch("srs.controllers.admin_controller.current_user")
def test_admin_add_student(mock_repo_class, mock_current_user, client):
    
    mock_instance = MagicMock()
    mock_repo_class.return_value = mock_instance
    mock_instance.add_student.return_value = "Successfully added Ahmed"

    mock_current_user.id = "A01"
    mock_current_user.is_authenticated = True

    response = client.post("/admin/AddUser", data={
        "usertype": "Student",
        "id": "202401389",
        "name": "Ahmed",
        "password": "123"
    })

    assert response.status_code == 200

@patch("srs.controllers.admin_controller.adminRepo")
@patch("srs.controllers.admin_controller.current_user")
def test_admin_add_prof(mock_repo_class, mock_current_user, client):
    
    mock_instance = MagicMock()
    mock_repo_class.return_value = mock_instance
    mock_instance.add_prof.return_value = "Successfully added Mohammed"

    mock_current_user.id = "A01"
    mock_current_user.is_authenticated = True

    response = client.post("/admin/AddUser", data={
        "usertype": "Professor",
        "id": "20240000",
        "name": "Mohammed",
        "password": "prof123"
    })

    assert response.status_code == 200

@patch("srs.controllers.admin_controller.current_user")
@patch("srs.controllers.admin_controller.adminRepo")
def test_admin_add_admin(mock_repo_class, mock_current_user, client):
    
    mock_instance = MagicMock()
    mock_repo_class.return_value = mock_instance
    mock_instance.add_admin.return_value = "Successfully added George"

    mock_current_user.id = "A01"
    mock_current_user.is_authenticated = True

    response = client.post("/admin/AddUser", data={
        "usertype": "Admin",
        "id": "20240000",
        "name": "George",
        "password": "admin123"
    })

    assert response.status_code == 200
import pytest
from unittest.mock import MagicMock, patch

@patch("srs.controllers.admin_controller.adminRepo")
def test_admin_add_student(mock_repo_class, client):
    
    mock_instance = MagicMock()
    mock_repo_class.return_value = mock_instance
    mock_instance.add_student.return_value = "Successfully added Ahmed"

    with client.session_transaction() as sess:
        sess['userID'] = 1
        sess['type'] = 'Admin'

    response = client.post("/AddUser", data={
        "usertype": "Student",
        "id": "202401389",
        "name": "Ahmed",
        "password": "123"
    })

    assert response.status_code == 200

@patch("srs.controllers.admin_controller.adminRepo")
def test_admin_add_prof(mock_repo_class, client):
    
    mock_instance = MagicMock()
    mock_repo_class.return_value = mock_instance
    mock_instance.add_prof.return_value = "Successfully added Mohammed"

    with client.session_transaction() as sess:
        sess['userID'] = 1
        sess['type'] = 'Admin'

    response = client.post("/AddUser", data={
        "usertype": "Professor",
        "id": "20240000",
        "name": "Mohammed",
        "password": "prof123"
    })

    assert response.status_code == 200

@patch("srs.controllers.admin_controller.adminRepo")
def test_admin_add_admin(mock_repo_class, client):
    
    mock_instance = MagicMock()
    mock_repo_class.return_value = mock_instance
    mock_instance.add_admin.return_value = "Successfully added George"

    with client.session_transaction() as sess:
        sess['userID'] = 1
        sess['type'] = 'Admin'

    response = client.post("/AddUser", data={
        "usertype": "Admin",
        "id": "20240000",
        "name": "George",
        "password": "admin123"
    })

    assert response.status_code == 200
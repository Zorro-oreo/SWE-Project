import pytest
import sys
import os

# Add project root to PYTHONPATH
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from srs.app import app

@pytest.fixture
def app_fixture():
    app.config["TESTING"] = True
    app.config["LOGIN_DISABLED"] = True
    app.config["SECRET_KEY"] = "test_secret"
    yield app


@pytest.fixture
def client(app_fixture):
    return app_fixture.test_client()
import pytest
import os
from app import app, init_db

TEST_DB = "test_jobs.db"

@pytest.fixture
def client():
    app.config["TESTING"] = True
    import app as app_module
    app_module.DATABASE = TEST_DB
    init_db()
    with app.test_client() as client:
        yield client
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200

def test_add_application(client):
    response = client.post("/add", data={
        "company": "Google",
        "position": "Software Engineer",
        "date_applied": "2024-01-15"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Google" in response.data

def test_add_page_loads(client):
    response = client.get("/add")
    assert response.status_code == 200

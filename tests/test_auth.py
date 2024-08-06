from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.database import SessionLocal, engine
from app.models import User, RoleEnum
from app.auth import create_access_token, authenticate_user

#client = TestClient(app)

def test_create_user(client):
    response = client.post(
        "/users/",
        json={"username": "testuser", "password": "testpassword", "full_name": "Test user", "email":"test@user.com", "role": "user"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["role"] == "user"

def test_login_for_access_token(client):
    

    response = client.post(
        "/token",
        data={"username": "testuser", "password": "testpassword"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

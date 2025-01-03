import pytest
from flask import Flask
from app import create_app


@pytest.fixture
def client():
    """Fixture to create a Flask test client."""
    app = create_app()
    app.config['TESTING'] = True  # Enable testing mode
    client = app.test_client()
    yield client


def test_health_check(client):
    """Test the /auth/health-check endpoint."""
    response = client.get('/auth/health-check')
    assert response.status_code == 200
    assert response.json == {"message": "AuthController is up and running!"}


def test_verify_token_missing_token(client):
    """Test the /auth/verify-token endpoint with no token."""
    response = client.post('/auth/verify-token', json={})
    assert response.status_code == 400
    assert response.json == {"error": "Token is required."}


def test_verify_token_invalid_token(client, mocker):
    """Test the /auth/verify-token endpoint with an invalid token."""
    # Mock the Firebase verify_id_token method to raise an exception
    mocker.patch('app.auth.firebase_utils.auth.verify_id_token', side_effect=Exception("Invalid token"))

    response = client.post('/auth/verify-token', json={"token": "invalid-token"})
    assert response.status_code == 401
    assert "Invalid token" in response.json['error']


def test_verify_token_valid_token(client, mocker):
    """Test the /auth/verify-token endpoint with a valid token."""
    # Mock the Firebase verify_id_token method to return a fake user ID
    mocker.patch('app.auth.firebase_utils.auth.verify_id_token', return_value={"uid": "test-user-id"})

    response = client.post('/auth/verify-token', json={"token": "valid-token"})
    assert response.status_code == 200
    assert response.json == {
        "message": "Token verified!",
        "user_id": "test-user-id"
    }

from flask import Blueprint, request, jsonify, redirect, url_for, render_template
from firebase_admin import auth as firebase_auth

auth_bp = Blueprint('auth', __name__)

# Dummy user data (replace with database in production)
USERS = {
    "user@example.com": "password123"
}

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.form
    email = data.get('email')
    password = data.get('password')

    # Check user credentials
    if email in USERS and USERS[email] == password:
        return render_template('welcome.html', email=email)
    else:
        return render_template('index.html', error="Invalid email or password"), 401

@auth_bp.route('/google-login', methods=['GET'])
def google_login():
    # Logic to integrate Google OAuth2
    return jsonify({"message": "Google login coming soon!"})

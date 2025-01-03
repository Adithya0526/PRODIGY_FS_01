from flask import Blueprint, request, jsonify
from .firebase_utils import verify_firebase_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/health-check', methods=['GET'])
def health_check():
    """
    Health-check endpoint to confirm the server is running.
    """
    return jsonify({"message": "AuthController is up and running!"}), 200

@auth_bp.route('/verify-token', methods=['POST'])
def verify_token():
    """
    Verify Firebase ID Token endpoint.
    """
    data = request.get_json()
    if not data or 'token' not in data:
        return jsonify({"error": "Token is required."}), 400

    token = data['token']
    try:
        user_id = verify_firebase_token(token)
        return jsonify({"message": "Token verified!", "user_id": user_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

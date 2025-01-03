from flask import current_app
import firebase_admin
from firebase_admin import auth, credentials

# Initialize Firebase Admin SDK
cred = credentials.Certificate(current_app.config[r"D:\Security Private Key\user---authentication-firebase-adminsdk-lnm0c-e616be44f5.json"])
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

def verify_firebase_token(token):
    """
    Verify the Firebase ID Token and extract the user ID.

    Args:
        token (str): Firebase ID Token to verify.

    Returns:
        str: The user ID extracted from the token.

    Raises:
        Exception: If the token is invalid or cannot be verified.
    """
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token['uid']
    except Exception as e:
        raise Exception(f"Failed to verify token: {e}")

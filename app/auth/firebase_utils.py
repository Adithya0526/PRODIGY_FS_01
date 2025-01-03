from flask import current_app
import firebase_admin
from firebase_admin import auth, credentials

# Firebase app reference
firebase_app = None

def initialize_firebase():
    """
    Initialize Firebase Admin SDK using the service account key from the app config.
    """
    global firebase_app
    if not firebase_app:
        try:
            # Use `current_app.config` to fetch the service account path
            service_account_key_path = current_app.config['SERVICE_ACCOUNT_KEY_PATH']
            cred = credentials.Certificate(service_account_key_path)
            firebase_app = firebase_admin.initialize_app(cred)
            print("Firebase initialized successfully!")
        except Exception as e:
            raise Exception(f"Error initializing Firebase: {e}")


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
        if not firebase_app:
            initialize_firebase()
        decoded_token = auth.verify_id_token(token, app=firebase_app)
        return decoded_token['uid']
    except Exception as e:
        raise Exception(f"Failed to verify token: {e}")

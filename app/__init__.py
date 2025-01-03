from flask import Flask, render_template
from app.auth import auth_bp
from app.config import get_config

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(get_config(env='development'))

    # Serve the index.html file for the root URL
    @app.route('/')
    def index():
        return render_template('login.html')

    # Register the auth blueprint
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app

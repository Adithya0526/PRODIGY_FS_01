from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app.config import Config

db=SQLAlchemy()
bcrypt=Bcrypt()
login_manager=LoginManager()
login_manager.login_view='main.login'
login_manager.login_message_category='info'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Correctly referencing the Config class

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)

    # Create database tables within app context
    with app.app_context():
        db.create_all()

    return app

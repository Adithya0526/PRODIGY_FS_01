from flask import Blueprint

# Create a blueprint for the auth module
auth_bp = Blueprint('auth', __name__)

# Import the controllers to register routes
from . import controllers

import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')
    SERVICE_ACCOUNT_KEY_PATH = os.environ.get(
        'SERVICE_ACCOUNT_KEY_PATH', 
        'instance/serviceAccountKey.json'
    )
    DEBUG = False


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    ENV = 'development'


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    ENV = 'production'


# Define a function to load the appropriate configuration
def get_config(env='development'):
    if env == 'production':
        return ProductionConfig
    return DevelopmentConfig

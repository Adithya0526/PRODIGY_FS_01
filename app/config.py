import os

class Config:
    """Base configuration."""
    SERVICE_ACCOUNT_KEY_PATH = r"D:\Security Private Key\fs-task-1-firebase-adminsdk-og1lj-702a6c0b14.json"


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

import os


class Config(object):
    '''
    Default configuration settings.
    '''
    # Application IP address
    APP_HOST = os.environ.get('HOST', '0.0.0.0')
    APP_PORT = int(os.environ.get('PORT', 5000))
    APP_DEBUG = 'False'
    SECRET_KEY = 'Y\xaf\xc5\x13\xc8\x16\x86v\xc7\x89\x1c\x8b\x0f\x085\xde'


class ProductionConfig(Config):
    '''
    Production configuration settings.
    '''
    pass


class DevelopmentConfig(Config):
    '''
    Development configuration settings.
    '''
    # Enable debugging
    APP_DEBUG = 'True'

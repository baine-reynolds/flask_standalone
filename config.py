class Config(object):
    DEBUG = False
    TESTING = False
    UPLOAD_FOLDER = "app/tmp/"
    SQLALCHEMY_TRACK_MODIFICATIONS = False # silence the deprecation warning

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_PASSWORD = ""

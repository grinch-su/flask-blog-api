import os

class Config():
    DEBUG = False
    SECRET = ''

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True

app_cfg = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod':  ProductionConfig
}
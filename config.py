class Config(object):

    SECRET_KEY = 'analyticalpurpose'

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = True

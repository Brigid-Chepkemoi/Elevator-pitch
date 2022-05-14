import os


class Config:
    SECRET_KEY = 'peeiicdjghsbnasgfwgfbwejhreirmd'

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://brie:Brie1240@localhost/pitches'
    SQLALCHEMY_DATABASE_URI = 'postgres://dvadmddscfveme:5cfb6b05a5f67570f5c16fd5a7f389df480f07fe54f38789fe4af0f056979f8b@ec2-54-165-184-219.compute-1.amazonaws.com:5432/dd4vf49s96dk0s'
    UPLOADED_PHOTOS_DEST='app/static/photos'

    #  email configurations

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'ELEVATOR PITCH-APP!',
    SENDER_EMAIL = 'bchepkemoi2022@gmail.com'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    """
    Production  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    """
    uri = os.getenv('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)

        SQLALCHEMY_DATABASE_URI = uri

DEBUG = True

class TestConfig(Config):
    pass


class DevConfig(Config):
    """
    Development  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    """




config_options = {
    # 'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}

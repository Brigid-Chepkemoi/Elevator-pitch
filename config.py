import os


class Config:
    SECRET_KEY = 'peeiicdjghsbnasgfwgfbwejhreirmd'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://brie:Brie@1240@localhost/pitches'
    # SQLALCHEMY_DATABASE_URI = 'postgres://eefvuyzaqztftv:ad1b1a3fec78e2ef63f6f5d77906fe9657a3eb89725b31e8845639389cbdee66@ec2-54-158-247-210.compute-1.amazonaws.com:5432/d7bf9drp975ag7'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'ELEVATOR PITCH-APP!'
    SENDER_EMAIL = 'briememo95@gmail.com'

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


class TestConfig(Config):
    pass


class DevConfig(Config):
    """
    Development  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    """

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}

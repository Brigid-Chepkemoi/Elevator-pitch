import os


class Config:
    SECRET_KEY = 'superdifficultsecret'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://brie:Brie@1240@localhost/pitches'
    # SQLALCHEMY_DATABASE_URI = 'postgres://eefvuyzaqztftv:ad1b1a3fec78e2ef63f6f5d77906fe9657a3eb89725b31e8845639389cbdee66@ec2-54-158-247-210.compute-1.amazonaws.com:5432/d7bf9drp975ag7'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    pass


class ProdConfig(Config):
    """
    Production  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    """


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

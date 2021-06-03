# import os


class Config:
    SECRET_KEY = 'd339f4678fbbf9d42c40f8022be0d34a'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'stmp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_SERVER = ''
    MAIL_PASSWORD = ''

from os import environ


class Configuration(object):
    DATABASE = {
        'name': environ.get('DATABASE_NAME', ':memory:'),
        'engine': environ.get('DATABASE_ENGINE', 'peewee.SqliteDatabase')
    }

    DEBUG = environ.get('DEBUG', False)

    SECRET_KEY = environ.get('SECRET_KEY', 'SECRET_KEY')

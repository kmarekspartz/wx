from os import environ


DATABASE_USER = environ.get('DATABASE_USER', None)
DATABASE_PASSWD = environ.get('DATABASE_PASSWD', None)
DATABASE_THREADLOCALS = bool(environ.get('DATABASE_THREADLOCALS', None))

DATABASE = {
    'name': environ.get('DATABASE_NAME', ':memory:'),
    'engine': environ.get('DATABASE_ENGINE', 'peewee.SqliteDatabase')
}

if DATABASE_USER:
    DATABASE['user'] = DATABASE_USER
if DATABASE_PASSWD:
    DATABASE['passwd'] = DATABASE_PASSWD
if DATABASE_THREADLOCALS:
    DATABASE['threadlocals'] = DATABASE_THREADLOCALS


class Configuration(object):
    DATABASE = DATABASE
    DEBUG = bool(environ.get('DEBUG', False))
    SECRET_KEY = environ.get('SECRET_KEY', 'SECRET_KEY')

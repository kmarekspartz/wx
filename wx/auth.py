from flask_peewee.auth import Auth

from wx.app import app, database
from wx.models.user import User


auth = Auth(app, database, user_model=User)

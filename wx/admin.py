from flask_peewee.admin import Admin

from wx.app import app
from wx.auth import auth
from wx.models import models


admin = Admin(app, auth)

auth.register_admin(admin)
for model in models:
    admin.register(model)

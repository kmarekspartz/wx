from flask_peewee.rest import RestAPI, RestResource, UserAuthentication, \
    AdminAuthentication

from wx.app import app
from wx.auth import auth

from wx.models import User, Location, Station, Report, Value


user_auth = UserAuthentication(auth)
admin_auth = AdminAuthentication(auth)
api = RestAPI(app, default_auth=user_auth)


class UserResource(RestResource):
    exclude = ('password', 'email',)


api.register(User, UserResource, auth=admin_auth)
api.register(Location)
api.register(Station)
api.register(Report)
api.register(Value)

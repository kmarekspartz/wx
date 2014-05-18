from flask_peewee.rest import RestAPI, RestResource, UserAuthentication, \
    AdminAuthentication

from wx.app import app
from wx.auth import auth
from wx.models import User, Location, Station, Report, Value


# See: http://flask-peewee.readthedocs.org/en/latest/rest-api.html
# Read-only for now. Use the following:
# user_auth = UserAuthentication(auth)
# admin_auth = AdminAuthentication(auth)

api = RestAPI(app)


class UserResource(RestResource):
    exclude = ('password', 'email',)


api.register(User, UserResource)
api.register(Location)
api.register(Station)
api.register(Report)
api.register(Value)

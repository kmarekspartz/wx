from wx.app import database
from wx.models.user import User
from wx.models.location import Location


class Station(database.Model):
    user = ForeignKeyField(User, related_name='stations')
    location = ForeignKeyField(Location, related_name='stations')

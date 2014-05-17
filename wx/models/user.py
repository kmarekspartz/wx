from peewee import PrimaryKeyField, CharField, BooleanField
from flask_peewee.auth import BaseUser

from wx.app import database


class User(database.Model, BaseUser):
    id = PrimaryKeyField()
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    admin = BooleanField()
    active = BooleanField()

    class Meta:
        order_by = ('username',)

    def __unicode__(self):
        return self.username

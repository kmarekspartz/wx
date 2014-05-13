from enum import Enum

from peewee import ForeignKeyField, CharField, DoubleField

from wx.app import database
from wx.models.report import Report


class ValueType(Enum):
    temperature = "temperature"  # Celsius
    pressure = "pressure"  # kPa
    relative_humidity = "relative_humidity"  # percent
    wind_speed = "wind_speed"  # m/s or km/h?
    wind_direction = "wind_direction"  # bearing in degrees
    # visibility = "visibility"  # kilometers
    # precipitation = "precipitation"  # cm/h?


class Value(database.Model):
    report = ForeignKeyField(Report, related_name='values')
    # must be a ValueType (Alternatively, use constraints):
    type = CharField(choices=ValueType)
    value = DoubleField()

    # validation?

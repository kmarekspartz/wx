from datetime import datetime

from wx.app import database
from wx.models.station import Station


class Report(database.Model):
    station = ForeignKeyField(Station, related_name='reports')

    timestamp = DateTimeField(default=datetime.now)

    class Meta:
        order_by = ('-timestamp',)

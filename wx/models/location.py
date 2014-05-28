from wx.app import database


class Location(database.Model):
    latitude = DoubleField()
    longitude = DoubleField()

    # class Meta:
    #    primary_key = CompositeKey('latitude', 'longitude')

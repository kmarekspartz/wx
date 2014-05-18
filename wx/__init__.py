"""
WX

Provides a weather-data website with a REST API.
"""

# See: http://flask-peewee.readthedocs.org/en/latest/gevent.html
from gevent import monkey; monkey.patch_all()

from flask import Flask
from flask_peewee.db import Database
from flask.ext.seasurf import SeaSurf


app = Flask(__name__)
app.config.from_object('wx.config.Configuration')

csrf = SeaSurf(app)

# Jinja should clean up whitespace:
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

database = Database(app)

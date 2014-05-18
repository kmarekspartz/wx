from flask import Flask
from flask_peewee.db import Database


app = Flask(__name__)
app.config.from_object('wx.config.Configuration')

# Jinja should clean up whitespace:
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

database = Database(app)

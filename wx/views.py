from flask import render_template

from wx.app import app
from wx.auth import auth, login_required


@app.route('/')
def home():
    return render_template('home.html')

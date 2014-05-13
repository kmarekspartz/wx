from wx.auth import *
from wx.api import *
from wx.views import *
from wx.admin import *

from wx.models import models
from wx.app import app, database


for model in models:
    model.create_table(fail_silently=True)

admin.setup()
api.setup()

if __name__ == '__main__':
    app.run()

from wx.auth import auth

admin = auth.User(username='admin', email='', admin=True, active=True)
admin.set_password('admin')

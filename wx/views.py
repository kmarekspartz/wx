from wx.app import app
from wx.auth import auth, login_required


@app.route('/private/')
@login_required
def private():
    user = auth.get_logged_in_user()
    return user.username

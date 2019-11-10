from flask import Flask
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from service.login.login_service import LoginService

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
app.config.from_envvar('PROJ_CONFIG')
app.secret_key = 'not_so_secret'
app.config['TESTING'] = False

from setup import bootstrap
bootstrap()


# app.config.update(
#    DEBUG = True,
#    SECRET_KEY = 'super_secret_key',
# )

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

login_service = LoginService()


@login_manager.user_loader
def load_user(user_id):
    return login_service.get_user(user_id)


import routes

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
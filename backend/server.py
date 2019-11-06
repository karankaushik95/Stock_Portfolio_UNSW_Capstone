from flask import Flask
#from flask_login import LoginManager

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
app.config.from_envvar('PROJ_CONFIG')
#login_manager = LoginManager()
#login_manager.init_app(app)

from setup import bootstrap
bootstrap()

import routes

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
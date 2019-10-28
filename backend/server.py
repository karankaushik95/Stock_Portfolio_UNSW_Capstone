from flask import Flask

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
app.config.from_envvar('PROJ_CONFIG')

from setup import bootstrap
bootstrap()

import routes

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

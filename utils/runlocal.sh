#!/usr/bin/env bash
mkdir -p env
python3 -m venv env
source env/bin/activate
pip -q install --upgrade pip
pip -q install -r requirements.txt
export PROJ_CONFIG="config/application-dev.cfg"
export FLASK_APP="app/main.py"
export FLASK_DEBUG=1

flask run

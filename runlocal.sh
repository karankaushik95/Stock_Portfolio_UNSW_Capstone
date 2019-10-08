#!/usr/bin/env bash
mkdir -p env
python3 -m venv env
source env/bin/activate
pip3 install --upgrade pip
pip3 -q install -r requirements.txt
export FLASK_APP="main.py"
export FLASK_DEBUG=1

flask run

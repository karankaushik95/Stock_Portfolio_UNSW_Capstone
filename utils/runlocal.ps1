# Set-ExecutionPolicy AllSigned

$env:PROJ_CONFIG="config/application-dev.cfg"
$env:FLASK_APP="app/run.py"
$env:FLASK_DEBUG=1

$env_path="env"

mkdir env
py -3 -m venv env
env\Scripts\activate

pip -q install --upgrade pip
pip -q install -r requirements.txt

flask run
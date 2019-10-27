# Set-ExecutionPolicy AllSigned

$env_path="env"
New-Item -ItemType Directory -Force -Path $env_path
python -m virtualenv .\env
.\env\Scripts\activate.bat
.\env\Scripts\activate

pip -q install --upgrade pip
pip -q install -r requirements.txt

$env:PROJ_CONFIG="config\application-dev.cfg"
$env:FLASK_APP="backend\server.py"
$env:FLASK_DEBUG=1

flask run
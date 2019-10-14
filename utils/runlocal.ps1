# Set-ExecutionPolicy AllSigned

<<<<<<< HEAD

$env_path="env"
New-Item -ItemType Directory -Force -Path $env_path
python -m virtualenv .\env
.\env\Scripts\activate.bat
.\env\Scripts\activate
=======
$env:PROJ_CONFIG="config/application-dev.cfg"
$env:FLASK_APP="app/run.py"
$env:FLASK_DEBUG=1

$env_path="env"

mkdir env
py -3 -m venv env
env\Scripts\activate
>>>>>>> f2793f34991882b94d00487677948d011ed0e38b

pip -q install --upgrade pip
pip -q install -r ..\requirements.txt

<<<<<<< HEAD
$env:PROJ_CONFIG="config/application-dev.cfg"
$env:FLASK_APP="../app/run.py"
$env:FLASK_DEBUG=1

=======
>>>>>>> f2793f34991882b94d00487677948d011ed0e38b
flask run
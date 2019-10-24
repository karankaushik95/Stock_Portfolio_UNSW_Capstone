# Set-ExecutionPolicy AllSigned

env\Scripts\activate

pip -q install --upgrade pip
pip -q install -r ..\requirements.txt

flask run
cd /d %~dp0
pip install virtualenv
virtualenv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
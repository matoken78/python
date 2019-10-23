cd /d %~dp0
virtualenv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
cd /d "%~dp0"
pip install Django==4.2.3
git clone https://github.com/django/django.git
pip install boto3
python .\manage.py migrate 
python .\manage.py makemigrations
./start.bat
@REM  db 관련 파일은 업로드 하지 않고 이파일을 실행 시킨다
python .\manage.py migrate 
python .\manage.py makemigrations
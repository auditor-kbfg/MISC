@echo off

rem 배치 파일이 위치한 폴더 경로를 상대 경로로 파악합니다.
for %%I in ("%~dp0") do set "parent_dir=%%~fI"
set "python_path=%parent_dir%python3"
rem PATH에 새로운 path 셋팅

rem %parent_dir%Scripts 값을 %scripts_path% 변수에 저장합니다.
set "scripts_path=%parent_dir%python3\Scripts"

rem 기존의 PATH에 %scripts_path%를 추가합니다.
set "PATH=%PATH%;%python_path%"
set "PATH=%PATH%;%scripts_path%"
echo 새로운 경로가 PATH 환경 변수에 추가되었습니다.

rem 변경된 PATH 환경 변수를 확인합니다.
echo %PATH%

rem 시스템 환경변수에 새로운 환경변수로 교체
setx PATH "%PATH%" /M

pause

@echo off

rem ��ġ ������ ��ġ�� ���� ��θ� ��� ��η� �ľ��մϴ�.
for %%I in ("%~dp0") do set "parent_dir=%%~fI"
set "python_path=%parent_dir%python3"
rem PATH�� ���ο� path ����

rem %parent_dir%Scripts ���� %scripts_path% ������ �����մϴ�.
set "scripts_path=%parent_dir%python3\Scripts"

rem ������ PATH�� %scripts_path%�� �߰��մϴ�.
set "PATH=%python_path%;%PATH%"
set "PATH=%scripts_path%;%PATH%"
echo ���ο� ��ΰ� PATH ȯ�� ������ �߰��Ǿ����ϴ�.

rem ����� PATH ȯ�� ������ Ȯ���մϴ�.
echo %PATH%

rem �ý��� ȯ�溯���� ���ο� ȯ�溯���� ��ü
setx PATH "%PATH%" /M

pause
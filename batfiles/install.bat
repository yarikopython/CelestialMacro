@echo off
:: Check if Python is installed
py --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please visit the following link to install Python 3.12.8:
    echo https://www.python.org/downloads/release/python-3128/
    start https://www.python.org/downloads/release/python-3128/
    pause
    exit /b
)

cls
cd..
IF NOT EXIST ".venv" (
    echo .venv not exist. Creating .venv ...
    py -m venv .venv
    cls

    echo created .venv ...

) ELSE (
    echo .venv already exists, activating it.
)


call .venv/Scripts/activate

:: Proceed with the rest of the script if Python is installed
echo Python is already installed. Proceeding with installing requirements...
pip install -r requirements.txt

pip freeze > requirements.txt
cls
echo Installed requirements.

pause
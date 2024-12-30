@echo off
:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please visit the following link to install Python 3.12.8:
    echo https://www.python.org/downloads/release/python-3128/
    start https://www.python.org/downloads/release/python-3128/
    pause
    exit /b
)

cls

:: Proceed with the rest of the script if Python is installed
echo Python is already installed. Proceeding with installing requirements...
pip install -r requirements.txt

cls

echo Running main.py...
python main.py

pause

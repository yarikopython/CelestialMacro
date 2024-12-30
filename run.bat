@echo off
:: Define the path to the installer and the folder
set INSTALLER_FOLDER=pythonexe
set INSTALLER_PATH=%INSTALLER_FOLDER%\python-3.12.8-amd64.exe

:: Check if the folder exists
if not exist "%INSTALLER_FOLDER%" (
    echo Folder "%INSTALLER_FOLDER%" does not exist.
    pause
    exit /b
)

:: Check if the installer exists in the folder
if not exist "%INSTALLER_PATH%" (
    echo Installer not found in "%INSTALLER_FOLDER%". Please ensure "python-3.12.8-amd64.exe" is in that folder.
    pause
    exit /b
)

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Installing Python 3.12.8...
    "%INSTALLER_PATH%" /quiet InstallAllUsers=1 PrependPath=1
    if %errorlevel% neq 0 (
        echo Failed to install Python. Please install it manually.
        pause
        exit /b
    )
    echo Python installed successfully.
)

cls

:: Proceed with the rest of the script (installing requirements and running the script)
echo Python is installed. Proceeding with installing requirements...
pip install -r requirements.txt

cls

echo Running main.py...
python main.py

pause

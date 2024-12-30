import sys
import subprocess

def install_requirements():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("requirements has been installed.")

install_requirements()
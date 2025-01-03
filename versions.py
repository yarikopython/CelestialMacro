import packaging.version, git, os, shutil
import requests
from colorama import Fore, init

init(autoreset=True)

current_dir = os.getcwd() # getting current directory
current_dir_name = os.path.basename(current_dir) # getting name of it

repo_url = "https://github.com/yarikopython/CelestialMacro.git"

def get_current_version():
    try:
        with open("version.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print(Fore.RED + "Error: version.txt not found.")
        return None

def get_latest_version():
    url = "https://raw.githubusercontent.com/yarikopython/CelestialMacro/refs/heads/main/version.txt"
    try:
        response = requests.get(url=url)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException:
        print(Fore.RED + "Failed to get version from repo.")
        return None

def check_for_updates():
    current_version = get_current_version()
    latest_version = get_latest_version()
    if current_version and latest_version:
        if packaging.version.Version(latest_version) > packaging.version.Version(current_version):
            print(Fore.YELLOW + f"\nUpdate available: {latest_version}")
            return True
        else:
            print(Fore.GREEN + f"\nYou are using the current version: {current_version}")
            return False
    return False

def get_and_install_update(url, target_folder):
    check_update = check_for_updates()
    if check_update:
        print(Fore.YELLOW + "Cloning repo...")

        # Backup the current folder
        backup_folder = target_folder + "_backup"
        if os.path.exists(target_folder):
            shutil.copytree(target_folder, backup_folder)

        # Remove the current folder and clone the latest repo
        if os.path.exists(target_folder):
            shutil.rmtree(target_folder)

        git.Repo.clone_from(url=url, to_path=target_folder)
        print(f"Cloned repo to {target_folder}")

    else:
        print(Fore.GREEN + "No update needed. You are on the latest version.")

## running it
get_and_install_update(repo_url, current_dir_name)

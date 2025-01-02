import configparser
from tkinter import messagebox

from config import create_config

config = configparser.ConfigParser()

config.read("config.ini")
try:
    aura = config["Settings"]["auratoequip"]
    webhook_url = config["Settings"]["webhookurl"]
    userid = config["Settings"]["userid"]
except KeyError:
    create_config()
    if "Settings" not in config.sections():
        config.add_section("Settings")
    config.set("Settings", "AURATOEQUIP", " ")
    config.set("Settings", "WEBHOOKURL", " ")
    config.set("Settings", "USERID", "")

finally:
    aura = config["Settings"]["auratoequip"]
    webhook_url = config["Settings"]["webhookurl"]
    userid = config["Settings"]["userid"]

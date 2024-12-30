import configparser
from config import create_config

config = configparser.ConfigParser()

config.read("config.ini")
try:
    aura = config["Settings"]["auratoequip"]
    webhook_url = config["Settings"]["webhookurl"]
except KeyError:
    create_config()
    if "Settings" not in config.sections():
        config.add_section("Settings")
    config.set("Settings", "AURATOEQUIP", "Nonee")
    config.set("Settings", "WEBHOOKURL", "Nonee")

finally:
    aura = config["Settings"]["auratoequip"]
    webhook_url = config["Settings"]["webhookurl"]
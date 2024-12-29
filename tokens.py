import configparser

config = configparser.ConfigParser()

config.read("config.ini")

aura = config["Settings"]["auratoequip"]
item = config["Settings"]["itemtoequip"]
webhook_url = config["Settings"]["webhookurl"]

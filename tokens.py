import configparser

config = configparser.ConfigParser()

config.read("config.ini")

aura = config["Settings"]["auratoequip"]
webhook_url = config["Settings"]["webhookurl"]

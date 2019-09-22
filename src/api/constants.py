import configparser

config = configparser.ConfigParser()
config.read("loocal-settings.ini")

GENIUS_ACCESS_TOKEN = config.get("Genius", "client_access_token")

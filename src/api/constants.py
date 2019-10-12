import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), "./local-settings.ini")))

GENIUS_ACCESS_TOKEN = config.get("Genius", "client_access_token")

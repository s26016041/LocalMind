import json
import os
from src.const import const

API_KEY = "api_key"

def save_api(api_key:str):
    data = {API_KEY: api_key}
    with open(const.CONFIG_FILE, "w") as f:
        json.dump(data, f)

def load_config():
    if os.path.exists(const.CONFIG_FILE):
        with open(const.CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def get_api()->str:
    config = load_config()
    return config.get(API_KEY, "")
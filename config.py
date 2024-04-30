import json

CONFIG_FILE = 'config.json'


def load_config() -> json:
    with open(CONFIG_FILE) as f:
        return json.load(f)

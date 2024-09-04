import json

class ConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_config(self):
        with open(self.config_file, "w") as f:
            json.dump(self.config, f)

    def get_config(self):
        return self.config

    def update_config(self, key, value):
        self.config[key] = value
        self.save_config()
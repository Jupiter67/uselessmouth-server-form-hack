from yaml import load_all
from yaml.loader import SafeLoader


class Settings:
    def __init__(self):
        with open('settings.yaml', 'r') as f:
            data = list(load_all(f, Loader=SafeLoader))[0]
            self.form_url = data.get('form_url')
            self.retry_count = data.get('retry_count', 10)

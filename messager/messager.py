import json
from datetime import datetime

def send_message(env: str, config_path: str) -> str:
    with open(config_path, 'r') as file:
        config = json.load(file)
    return f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - [{env}] - [{config['message']}]"

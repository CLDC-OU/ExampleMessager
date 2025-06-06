import json
from datetime import datetime

def send_message(env: str, cfg_file: str) -> str:
    with open(cfg_file, 'r') as file:
        config = json.load(file)
    return f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - [{env}] - [{config['message']}]"

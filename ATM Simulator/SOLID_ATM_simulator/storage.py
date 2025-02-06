import json
import os
from interfaces import IStorageProvider

class JsonStorageProvider(IStorageProvider):
    def __init__(self, base_path: str):
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)

    def save(self, data: dict, key: str) -> None:
        file_path = os.path.join(self.base_path, f"{key}.json")
        temp_path = f"{file_path}.tmp"

        with open(temp_path, 'w') as f:
            json.dump(data, f, indent=4)
        os.replace(temp_path, file_path)

    def load(self, key: str) -> dict:
        file_path = os.path.join(self.base_path, f"{key}.json")
        if not os.path.exists(file_path):
            return {}

        with open(file_path, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

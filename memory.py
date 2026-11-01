import json
import os


class Memory:
    def __init__(self, file_path="data/memory.json"):
        self.file_path = file_path
        self.data = self._load()

    def _load(self):
        if not os.path.exists(self.file_path):
            return {
                "facts": {},
                "preferences": {},
                "history": []
            }

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return {
                "facts": {},
                "preferences": {},
                "history": []
            }

    def save(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)

    def remember_fact(self, key, value):
        self.data["facts"][key] = value
        self.save()

    def remember_preference(self, key, value):
        self.data["preferences"][key] = value
        self.save()

    def get_fact(self, key):
        return self.data["facts"].get(key)

    def get_preference(self, key):
        return self.data["preferences"].get(key)

    def add_history(self, user_message, ai_response):
        self.data["history"].append({
            "user": user_message,
            "ai": ai_response
        })

        self.save()
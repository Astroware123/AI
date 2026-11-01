class Personality:
    def __init__(self, memory):
        self.memory = memory

    def get_style(self):
        preferences = self.memory.data.get("preferences", {})

        length = preferences.get("response_length", "normal")
        level = preferences.get("explanation_level", "normal")

        return {
            "length": length,
            "level": level
        }

    def instructions(self):
        style = self.get_style()

        instructions = []

        if style["length"] == "short":
            instructions.append("Keep responses short and direct.")

        elif style["length"] == "detailed":
            instructions.append("Give detailed explanations.")

        if style["level"] == "simple":
            instructions.append("Use simple language and explain difficult terms.")

        elif style["level"] == "advanced":
            instructions.append("Use technical and advanced explanations.")

        return instructions
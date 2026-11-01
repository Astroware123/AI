from .memory import Memory


class Learner:
    def __init__(self, memory=None):
        self.memory = memory or Memory()

    def learn(self, message):
        text = message.lower().strip()

        # User wants shorter answers
        if any(word in text for word in [
            "too long",
            "shorter",
            "keep it short",
            "be brief"
        ]):
            self.memory.remember_preference(
                "response_length",
                "short"
            )
            return "learned"

        # User wants more detail
        if any(word in text for word in [
            "more detail",
            "explain more",
            "go deeper",
            "more detailed"
        ]):
            self.memory.remember_preference(
                "response_length",
                "detailed"
            )
            return "learned"

        # User wants simpler explanations
        if any(word in text for word in [
            "simpler",
            "make it simple",
            "explain simply",
            "too complicated"
        ]):
            self.memory.remember_preference(
                "explanation_level",
                "simple"
            )
            return "learned"

        # User wants technical explanations
        if any(word in text for word in [
            "technical",
            "advanced",
            "technical explanation"
        ]):
            self.memory.remember_preference(
                "explanation_level",
                "advanced"
            )
            return "learned"

        return "nothing_new"

    def get_learning_profile(self):
        return self.memory.data["preferences"]
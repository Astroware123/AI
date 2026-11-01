from .memory import Memory
from .learner import Learner
from .personality import Personality


class Brain:
    def __init__(self):
        self.memory = Memory()
        self.learner = Learner(self.memory)
        self.personality = Personality(self.memory)

    def process(self, message):
        # First, check whether the user is teaching the AI something
        learning_result = self.learner.learn(message)

        # Get the AI's current learned personality
        instructions = self.personality.instructions()

        # Build a basic response
        response = self.generate_response(message, instructions)

        # Save the conversation
        self.memory.add_history(message, response)

        return response

    def generate_response(self, message, instructions):
        text = message.lower()

        if "hello" in text or "hi" in text:
            response = "Hello! I'm AdaptiveAI."

        elif "who are you" in text:
            response = "I'm AdaptiveAI, a Python AI designed to learn from interaction."

        elif "what can you do" in text:
            response = (
                "I can remember information, learn preferences, "
                "and adapt how I respond."
            )

        else:
            response = (
                f"You said: {message}\n"
                f"My current behavior settings: {instructions}"
            )

        return response
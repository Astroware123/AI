from AI.brain import Brain


def main():
    print("=" * 45)
    print("           ADAPTIVE AI v1")
    print("=" * 45)
    print("Type 'exit' to stop.")
    print()

    brain = Brain()

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() == "exit":
                print("AdaptiveAI: Goodbye!")
                break

            response = brain.process(user_input)

            print(f"AI: {response}")
            print()

        except KeyboardInterrupt:
            print("\nAdaptiveAI: Goodbye!")
            break


if __name__ == "__main__":
    main()
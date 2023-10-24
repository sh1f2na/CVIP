import random
import time

# List of quotes for typing practice
quotes = [
    "Slow but Steady wins the race.",
    "How's the josh buddy?!",
    "Be your own Therapy, you can heal yourself better than anyone can.",
    "Work until you feel Dubai is cheap.",
    "you haven't understood the things well if you cannot explain it in 5 minutes.",
    "Blood is thicker than water.",
    "Nothing is as expensive as an missed opportunity.",
]


# generate random quotes from what is fed
def get_random_quote():
    return random.choice(quotes)


# calculates the typing speed of a user
def calculate_typing_speed(input_text, time_taken):
    words = input_text.split()
    word_count = len(words)
    minutes = time_taken / 60
    typing_speed = word_count / minutes
    return round(typing_speed, 2)


def main():
    print("Welcome to the Typing Speed Tester!")
    input("Press Enter to start the test...")
    quote = get_random_quote()
    print(f"Type the following:\n{quote}")

    start_time = time.time()

    user_input = input("Start typing: ")

    end_time = time.time()
    time_taken = end_time - start_time

    typing_speed = calculate_typing_speed(user_input, time_taken)

    print(f"\nYour typing speed: {typing_speed} words per minute (WPM)")

    accuracy = (
        sum([1 for a, b in zip(quote, user_input) if a == b])
        / max(len(quote), len(user_input))
        * 100
    )
    print(f"Accuracy: {round(accuracy, 2)}%")


if __name__ == "__main__":
    main()

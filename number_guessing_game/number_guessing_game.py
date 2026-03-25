import random


def get_user_input(prompt, valid_options=None, is_int=False):
    """
    Handles user input with validation.
    - valid_options: list of acceptable string inputs (e.g., ['y', 'n'])
    - is_int: whether input should be an integer
    """
    while True:
        user_input = input(prompt).strip()
        if is_int:
            try:
                return int(user_input)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif valid_options:
            if user_input.lower() in valid_options:
                return user_input.lower()
            else:
                print(
                    f"Invalid input. Enter one of: {', '.join(valid_options)}")
        else:
            return user_input


def play_round():
    """Plays a single round of the guessing game and returns the number of attempts."""
    secret_no = random.randint(1, 10)
    guess = None
    attempts = 0

    print("\nI have selected a number between 1 and 10. Can you guess it?")

    while guess != secret_no:
        guess = get_user_input("Enter your guess: ", is_int=True)
        attempts += 1

        if guess < secret_no:
            print("Too low! Try again.")
        elif guess > secret_no:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! {secret_no} is correct!")
            print(f"You guessed it in {attempts} attempts.")
            return attempts


def guessing_game():
    """Main function to run the guessing game."""
    print("Welcome to the Number Guessing Game!")

    high_score = None

    while True:
        play_game = get_user_input(
            "Do you want to play? (y/n): ", valid_options=['y', 'n'])
        if play_game == 'n':
            break

        attempts = play_round()

        if high_score is None or attempts < high_score:
            high_score = attempts
            print(f"🏆 New high score: {high_score} attempts!")

    print("Thanks for playing! Goodbye!")


if __name__ == "__main__":
    guessing_game()

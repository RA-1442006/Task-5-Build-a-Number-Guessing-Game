"""
Number Guessing Game
Task 5 - Python Programming Track (Level 1)

A terminal-based number guessing game where the player attempts to guess
a randomly generated number within a specified range. Includes input validation,
multiple difficulty settings, attempt tracking, session best score tracking,
and replay options.
"""

import random


def choose_difficulty():
    """
    Prompts the player to select a difficulty level.

    Returns:
        tuple: (min_val, max_val, max_attempts, level_name)
               max_attempts is None for unlimited attempts.
    """
    levels = {
        "1": {"name": "Easy", "range": (1, 50), "max_attempts": None},
        "2": {"name": "Medium", "range": (1, 100), "max_attempts": 10},
        "3": {"name": "Hard", "range": (1, 200), "max_attempts": 7},
    }

    print("\nSelect a Difficulty Level:")
    print("  1. Easy   (Range: 1 - 50,  Attempts: Unlimited)")
    print("  2. Medium (Range: 1 - 100, Attempts: 10) [Default]")
    print("  3. Hard   (Range: 1 - 200, Attempts: 7)")

    while True:
        choice = input("Enter difficulty (1, 2, or 3) [Press Enter for 2]: ").strip()
        if choice == "":
            choice = "2"

        if choice in levels:
            selected = levels[choice]
            min_val, max_val = selected["range"]
            return min_val, max_val, selected["max_attempts"], selected["name"]

        print("Invalid choice! Please enter 1, 2, or 3.")


def get_valid_guess(min_val, max_val):
    """
    Prompts the user for a guess and validates the input.
    Handles non-numeric inputs and out-of-range numbers gracefully
    using try/except without incrementing the game attempt counter.

    Args:
        min_val (int): Minimum valid guess value.
        max_val (int): Maximum valid guess value.

    Returns:
        int: A valid integer guess within [min_val, max_val].
    """
    while True:
        raw_input = input(f"Enter your guess ({min_val}-{max_val}): ").strip()
        try:
            guess = int(raw_input)
            if min_val <= guess <= max_val:
                return guess
            print(f"[!] Out of range! Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("[!] Invalid input! Please enter a valid whole number (no letters or symbols).")


def play_game(min_val, max_val, max_attempts, level_name):
    """
    Runs a single round of the number guessing game.

    Args:
        min_val (int): Lower bound of random range.
        max_val (int): Upper bound of random range.
        max_attempts (int or None): Maximum guesses allowed, or None if unlimited.
        level_name (str): The name of the difficulty level.

    Returns:
        tuple: (won: bool, attempts: int)
    """
    # Generate the secret target number
    target_number = random.randint(min_val, max_val)
    attempts = 0

    print(f"\n--- New Game: {level_name} Mode ---")
    print(f"I'm thinking of a number between {min_val} and {max_val}.")
    if max_attempts:
        print(f"You have {max_attempts} attempts to find it. Good luck!\n")
    else:
        print("You have unlimited attempts. Take your time!\n")

    # =========================================================================
    # WHY A WHILE LOOP IS BETTER THAN A FOR LOOP HERE:
    # -------------------------------------------------------------------------
    # In a number guessing game, the exact number of iterations is indeterminate
    # because it depends on the user's guessing efficiency, especially when
    # attempts are unlimited (Easy mode).
    #
    # While a `for` loop is designed to iterate over a predetermined sequence or
    # fixed range, a `while` loop is condition-driven. It allows the game loop
    # to continue until a specific condition is met (either the player guesses
    # the correct number or they exhaust their allowed attempts).
    # Furthermore, handling invalid inputs without consuming valid game turns
    # fits naturally within a condition-controlled while architecture.
    # =========================================================================

    while True:
        # Show remaining attempts if restricted
        if max_attempts is not None:
            attempts_left = max_attempts - attempts
            print(f"Attempts remaining: {attempts_left}")

        # Get a validated guess (invalid attempts are filtered inside get_valid_guess)
        guess = get_valid_guess(min_val, max_val)
        attempts += 1

        # Evaluate the guess
        if guess < target_number:
            print(">> Too low! Try a higher number.\n")
        elif guess > target_number:
            print(">> Too high! Try a lower number.\n")
        else:
            print(f"\n[+] Congratulations! You found the correct number: {target_number}!")
            print(f"[+] Total attempts: {attempts}\n")
            return True, attempts

        # Check if the player has exhausted allowed attempts
        if max_attempts is not None and attempts >= max_attempts:
            print(f"[x] Game Over! You've used all {max_attempts} attempts.")
            print(f"The secret number was: {target_number}\n")
            return False, attempts


def display_best_scores(best_scores):
    """
    Displays the best scores (fewest attempts) achieved across all difficulty levels.

    Args:
        best_scores (dict): Dictionary mapping difficulty names to best attempt counts.
    """
    print("\n========== Session Best Scores (Fewest Attempts) ==========")
    for level, score in best_scores.items():
        score_text = f"{score} attempt(s)" if score is not None else "No wins yet"
        print(f"  - {level:<8}: {score_text}")
    print("===========================================================\n")


def main():
    """
    Main entry point for the Number Guessing Game.
    Controls game sessions, best score tracking, and replay prompts.
    """
    print("==================================================")
    print("         WELCOME TO THE NUMBER GUESSING GAME       ")
    print("==================================================")

    best_scores = {
        "Easy": None,
        "Medium": None,
        "Hard": None,
    }

    while True:
        # 1. Select difficulty
        min_val, max_val, max_attempts, level_name = choose_difficulty()

        # 2. Play game round
        won, attempts = play_game(min_val, max_val, max_attempts, level_name)

        # 3. Update session best score if player won
        if won:
            current_best = best_scores[level_name]
            if current_best is None or attempts < current_best:
                best_scores[level_name] = attempts
                print(f"[*] NEW RECORD for {level_name} mode: {attempts} attempt(s)!")

        # 4. Show current best scores
        display_best_scores(best_scores)

        # 5. Play again prompt
        while True:
            play_again = input("Would you like to play again? (y/n): ").strip().lower()
            if play_again in ("y", "yes", "n", "no"):
                break
            print("Please enter 'y' for yes or 'n' for no.")

        if play_again in ("n", "no"):
            print("\nThank you for playing! Have a great day!\n")
            break


if __name__ == "__main__":
    main()

# Number Guessing Game (Python)

> **Task 5: Build a Number Guessing Game**  
> *Python Programming Track — Level 1 Internship Task*  
> 🔗 **LinkedIn Post**: [View Post](https://lnkd.in/p/g-UM2qBM)

An interactive, terminal-based number guessing game developed in pure Python. The computer selects a random secret number within a chosen range, and the player receives real-time directional hints ("Too high" or "Too low") until finding the correct number or exhausting their attempts.

---

## 🎯 Objectives

This project reinforces essential core Python programming foundations:
- **Random Number Generation**: Utilizing Python's built-in `random` module (`random.randint`).
- **Control Flow & Loops**: Implementing condition-controlled `while` loops for indeterminate game states.
- **Conditional Branching**: Comparing guesses against target values (`if / elif / else`).
- **Input Validation & Exception Handling**: Employing `try / except ValueError` blocks to cleanly catch invalid non-numeric inputs and range violations without penalizing player attempts.
- **State & Score Tracking**: Managing attempt counts, remaining turns, and session-wide high scores across multiple rounds.
- **Modular Code Architecture**: Structuring logic into dedicated functions (`get_valid_guess`, `choose_difficulty`, `play_game`, `main`) guarded by `if __name__ == "__main__":`.

---

## 🛠️ Tech Stack

- **Language**: Python 3 (standard library only)
- **Built-in Modules**: `random`
- **Dependencies**: None (Zero external libraries required)

---

## 🚀 How to Run

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/RA-1442006/Task-5-Build-a-Number-Guessing-Game.git
   cd Task-5-Build-a-Number-Guessing-Game
   ```

2. **Run the Game**:
   ```bash
   python number_guessing_game.py
   ```

*(Requires Python 3.6 or newer)*

---

## ✨ Features

- 🎲 **Random Target Generation**: Generates numbers using `random.randint(min_val, max_val)`.
- 🧭 **Intelligent Directional Clues**: Provides immediate "Too high!" or "Too low!" feedback.
- 🛡️ **Robust Input Sanitization**:
  - Catches non-numeric inputs (strings, symbols) via `try / except ValueError`.
  - Flags out-of-range guesses.
  - **Does not penalize** attempts for invalid or out-of-bound inputs.
- 🎚️ **Multiple Difficulty Levels**:
  - **Easy**: Range `1 - 50`, Unlimited attempts.
  - **Medium** *(Default)*: Range `1 - 100`, `10` attempts limit.
  - **Hard**: Range `1 - 200`, `7` attempts limit.
- ⏱️ **Attempt Counter**: Live remaining-attempt display and final summary upon victory or game over.
- 🏆 **Session Best Score Tracker**: Retains and displays the fewest attempts taken per difficulty level across multiple games.
- 🔁 **Replay Option**: Simple "Play again?" prompt (`y/n`) allows seamless multi-round sessions.

---

## 🎮 Sample Gameplay Output

Here is a real terminal transcript showing difficulty selection, invalid string input handling, out-of-range boundary checking, directional hints, score tracking, and victory:

```text
==================================================
         WELCOME TO THE NUMBER GUESSING GAME       
==================================================

Select a Difficulty Level:
  1. Easy   (Range: 1 - 50,  Attempts: Unlimited)
  2. Medium (Range: 1 - 100, Attempts: 10) [Default]
  3. Hard   (Range: 1 - 200, Attempts: 7)
Enter difficulty (1, 2, or 3) [Press Enter for 2]: 2

--- New Game: Medium Mode ---
I'm thinking of a number between 1 and 100.
You have 10 attempts to find it. Good luck!

Attempts remaining: 10
Enter your guess (1-100): abc
[!] Invalid input! Please enter a valid whole number (no letters or symbols).

Enter your guess (1-100): 125
[!] Out of range! Please enter a number between 1 and 100.

Enter your guess (1-100): 25
>> Too low! Try a higher number.

Attempts remaining: 9
Enter your guess (1-100): 80
>> Too high! Try a lower number.

Attempts remaining: 8
Enter your guess (1-100): 54

[+] Congratulations! You found the correct number: 54!
[+] Total attempts: 3

[*] NEW RECORD for Medium mode: 3 attempt(s)!

========== Session Best Scores (Fewest Attempts) ==========
  - Easy    : No wins yet
  - Medium  : 3 attempt(s)
  - Hard    : No wins yet
===========================================================

Would you like to play again? (y/n): n

Thank you for playing! Have a great day!
```

---

## 💡 Interview Questions & Answers

### a) What is the `random` module?
The `random` module is part of Python's standard library. It provides pseudo-random number generators powered by the **Mersenne Twister** core algorithm. Key functions include:
- `random.randint(a, b)`: Returns a random integer $N$ such that $a \le N \le b$ (both endpoints inclusive).
- `random.random()`: Returns a random floating-point number in the range $[0.0, 1.0)$.
- `random.choice(seq)`: Randomly selects an element from a non-empty sequence.
- `random.shuffle(seq)`: Shuffles the elements of a mutable sequence in-place.

Because it is built into Python, no external installation (e.g., via `pip`) is needed.

### b) What is the difference between `while` and `for` loops?
- **`for` loop (Definite Iteration)**: Used when the number of iterations or the collection to traverse is known beforehand (e.g., iterating through items in a list or across a fixed `range(n)`).
- **`while` loop (Indefinite Iteration)**: Used when the repetition depends on a boolean condition being evaluated dynamically during runtime. It repeats until that condition evaluates to `False`.

**Why `while` is better for this game:**
In a guessing game, the number of turns required is indeterminate—it depends on player skill and guess correctness. Furthermore, invalid inputs (non-numeric strings or out-of-range numbers) must prompt the user again without consuming attempts or advancing loop steps. A condition-controlled `while` loop cleanly handles this event-driven behavior.

### c) How would you limit the number of attempts?
To limit attempts:
1. Define a maximum attempts variable (e.g., `max_attempts = 10`).
2. Track valid guesses with an `attempts` counter variable initialized to `0`.
3. Increment `attempts += 1` strictly when a valid numerical guess is received.
4. After each incorrect guess, evaluate `if attempts >= max_attempts:`. If true, print a game over message revealing the secret number and terminate the round using `break` or `return`.
5. Optionally display remaining attempts (`max_attempts - attempts`) prior to each guess to keep the player informed.

---

## 📐 Approach & Outcome

### Approach
1. **Requirements Decomposition**: Began by identifying inputs, conditions, outputs, edge cases (strings, out-of-range integers), and replay mechanisms.
2. **Defensive Programming**: Created `get_valid_guess()` to isolate user input handling. Using a `try / except ValueError` block guarantees that bad inputs never crash the program or consume player attempts.
3. **Flexible Architecture**: Designed difficulty settings as a dictionary containing ranges and attempt allowances, making it easy to add custom difficulty tiers in the future.
4. **Clean Code & Readability**: Followed PEP 8 conventions, wrote descriptive docstrings, meaningful variable names, and implemented the standard `if __name__ == "__main__":` entry point.

### Outcome
The final game is clean, self-contained, and resilient against unexpected user actions. It fulfills all Level 1 requirements and delivers bonus features including difficulty tiers, attempt limits, session high-score tracking, and clean replay capabilities.

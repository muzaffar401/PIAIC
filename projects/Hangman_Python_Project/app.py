import random
import time
import os
from termcolor import colored
import pyfiglet

def hangman():
    # Clear screen and show title
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(pyfiglet.figlet_format("HANGMAN", font="slant"), "red"))
    print(colored("~ A Deadly Game of Letters ~", "yellow"))
    print(colored("Guess the word before the man hangs!", "cyan"))
    time.sleep(1.5)
    
    # Categories and words
    word_categories = {
        "Programming": ["python", "javascript", "algorithm", "function", "variable", "boolean"],
        "Animals": ["elephant", "kangaroo", "chameleon", "rhinoceros", "platypus", "octopus"],
        "Countries": ["canada", "brazil", "japan", "australia", "ethiopia", "madagascar"],
        "Movies": ["inception", "avatar", "titanic", "jaws", "frozen", "gladiator"]
    }
    
    # Let player choose category
    print("\nChoose a category:")
    for i, category in enumerate(word_categories.keys(), 1):
        print(f"{i}. {category}")
    
    while True:
        try:
            choice = int(input("\nEnter category number: ")) - 1
            if 0 <= choice < len(word_categories):
                category = list(word_categories.keys())[choice]
                word_list = word_categories[category]
                break
            print(colored("Invalid choice! Try again.", "red"))
        except ValueError:
            print(colored("Please enter a number.", "red"))
    
    secret_word = random.choice(word_list).lower()
    correct_letters = set()
    incorrect_letters = set()
    max_attempts = 6  # Changed from 7 to 6 to match stages count
    attempts_left = max_attempts
    hints_left = 2
    score = 0
    
    # Game introduction
    print(colored(f"\nCategory: {category}", "magenta"))
    print(colored(f"The word has {len(secret_word)} letters.", "blue"))
    print(colored(f"You have {attempts_left} attempts and {hints_left} hints.", "green"))
    time.sleep(1)
    
    # Main game loop
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("\nCurrent Status:", "yellow", attrs=["bold"]))
        
        # Display word with colors
        display_word = []
        for letter in secret_word:
            if letter in correct_letters:
                display_word.append(colored(letter, "green"))
            else:
                display_word.append(colored("_", "red"))
        print("Word: " + " ".join(display_word))
        
        # Display incorrect guesses
        if incorrect_letters:
            print(colored("\nIncorrect guesses:", "yellow") + 
                  colored(" ".join(incorrect_letters), "red"))
        
        # Display attempts and score
        print(colored(f"\nAttempts left: {attempts_left}", "cyan"))
        print(colored(f"Hints left: {hints_left}", "blue"))
        print(colored(f"Score: {score}", "magenta"))
        
        # Draw the hangman
        draw_hangman(attempts_left)
        
        # Check win condition
        if all(letter in correct_letters for letter in secret_word):
            score += attempts_left * 10  # Bonus for remaining attempts
            print(colored("\nCONGRATULATIONS!", "green", attrs=["bold"]))
            print(colored(f"You guessed the word: {secret_word.upper()}", "green"))
            print(colored(f"Final Score: {score}", "yellow", attrs=["bold"]))
            print(colored("You saved the hangman!", "green"))
            break
        
        # Check lose condition
        if attempts_left <= 0:
            print(colored("\nGAME OVER!", "red", attrs=["bold"]))
            print(colored(f"The word was: {secret_word.upper()}", "red"))
            print(colored("The hangman has been hanged!", "red"))
            break
        
        # Get player's guess
        print("\nOptions:")
        print("1. Guess a letter")
        print("2. Ask for a hint")
        print("3. Guess the whole word")
        
        while True:
            option = input("\nChoose an option (1-3): ")
            
            # Option 1: Guess a letter
            if option == "1":
                guess = input("Guess a letter: ").lower()
                
                # Validate input
                if len(guess) != 1:
                    print(colored("Please enter a single letter.", "red"))
                elif not guess.isalpha():
                    print(colored("Please enter a letter (a-z).", "red"))
                elif guess in correct_letters or guess in incorrect_letters:
                    print(colored("You've already guessed that letter.", "yellow"))
                else:
                    # Check if guess is correct
                    if guess in secret_word:
                        correct_letters.add(guess)
                        print(colored("Correct!", "green"))
                        score += 5
                    else:
                        incorrect_letters.add(guess)
                        attempts_left -= 1
                        print(colored("Incorrect!", "red"))
                    break
            
            # Option 2: Ask for a hint
            elif option == "2":
                if hints_left > 0:
                    hints_left -= 1
                    # Reveal a random letter not yet guessed
                    unrevealed = [letter for letter in secret_word if letter not in correct_letters]
                    if unrevealed:
                        hint = random.choice(unrevealed)
                        correct_letters.add(hint)
                        print(colored(f"Hint: The letter '{hint}' is in the word!", "blue"))
                        score -= 3  # Penalty for using hint
                        time.sleep(2)
                        break
                    else:
                        print(colored("No letters left to reveal!", "yellow"))
                else:
                    print(colored("No hints left!", "red"))
            
            # Option 3: Guess the whole word
            elif option == "3":
                word_guess = input("Guess the whole word: ").lower()
                if word_guess == secret_word:
                    correct_letters.update(secret_word)
                    score += 20  # Big bonus for full word guess
                    print(colored("Correct!", "green"))
                    time.sleep(1)
                    break
                else:
                    attempts_left -= 2  # Big penalty for wrong word guess
                    print(colored("Wrong guess! You lose 2 attempts.", "red"))
                    time.sleep(1)
                    break
            
            else:
                print(colored("Invalid option! Choose 1-3.", "red"))

def draw_hangman(attempts_left):
    # Enhanced ASCII art with colors
    stages = [
        colored("""
           -----
           |   |
               |
               |
               |
               |
        =========
        """, "blue"),
        colored("""
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """, "green"),
        colored("""
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """, "green"),
        colored("""
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """, "yellow"),
        colored("""
           -----
           |   |
           O   |
          /|\  |
               |
               |
        =========
        """, "yellow"),
        colored("""
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        """, "red"),
        colored("""
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        """, "red")
    ]
    
    # Print the appropriate stage (reverse order)
    print(stages[len(stages) - 1 - attempts_left])

if __name__ == "__main__":
    while True:
        hangman()
        play_again = input(colored("\nPlay again? (y/n): ", "cyan")).lower()
        if play_again != 'y':
            print(colored("\nThanks for playing Hangman!", "magenta"))
            break
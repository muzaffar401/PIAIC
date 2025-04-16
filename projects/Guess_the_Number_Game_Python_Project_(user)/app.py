import random
import time
from termcolor import colored
import pyfiglet
from enum import Enum, auto

class Difficulty(Enum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()
    EXTREME = auto()

def display_welcome():
    """Show animated welcome message"""
    print(colored(pyfiglet.figlet_format("Number Wizard"), 'cyan'))
    print(colored("~ The Ultimate Guessing Challenge ~", 'yellow'))
    time.sleep(1)
    print("\nI'm thinking of a secret number... can you guess it?\n")

def select_difficulty():
    """Let player choose game difficulty"""
    print(colored("Select difficulty:", 'magenta'))
    for i, level in enumerate(Difficulty, 1):
        print(f"{i}. {level.name.title()}")
    
    while True:
        choice = input("Enter choice (1-4): ")
        if choice in {'1', '2', '3', '4'}:
            return list(Difficulty)[int(choice)-1]

def get_range(difficulty):
    """Return number range based on difficulty"""
    ranges = {
        Difficulty.EASY: (1, 10),
        Difficulty.MEDIUM: (1, 50),
        Difficulty.HARD: (1, 100),
        Difficulty.EXTREME: (1, 1000)
    }
    return ranges[difficulty]

def get_hint(secret: int, guess: int, attempts: int) -> str:
    """Return creative hints based on guess"""
    difference = abs(secret - guess)
    
    if guess == secret:
        return colored("✨ Bullseye! You got it!", 'green')
    
    hints = {
        (0, 2): [
            "🔥 Burning hot!",
            "🧨 Almost there!",
            "⚡ On fire!"
        ],
        (3, 5): [
            "🔥 Warm!",
            "♨️ Getting closer",
            "☀️ Toasty"
        ],
        (6, 10): [
            "🌤️ Lukewarm",
            "🍃 Mild",
            "💨 Breezy"
        ],
        (11, float('inf')): [
            "❄️ Ice cold!",
            "🧊 Freezing!",
            "🥶 Arctic chill!"
        ]
    }
    
    for (low, high), messages in hints.items():
        if low <= difference <= high:
            hint = random.choice(messages)
            if guess < secret:
                return f"{hint} (Try higher)"
            return f"{hint} (Try lower)"

def animate_thinking():
    """Show cool thinking animation"""
    symbols = ["🔮", "🧠", "💭", "🌀"]
    print("\n" + colored("Deciphering your guess...", 'blue'), end=' ')
    for _ in range(5):
        print(colored(random.choice(symbols), 'magenta'), end=' ', flush=True)
        time.sleep(0.3)
    print()

def play_round(difficulty):
    """Play one round of the game"""
    low, high = get_range(difficulty)
    secret = random.randint(low, high)
    attempts = 0
    guess_history = []
    
    print(f"\nI'm thinking of a number between {low} and {high}...")
    
    while True:
        try:
            guess = int(input(f"\nEnter guess ({low}-{high}): "))
            if guess < low or guess > high:
                print(f"Please stay between {low} and {high}!")
                continue
        except ValueError:
            print("Numbers only please!")
            continue
            
        attempts += 1
        guess_history.append(guess)
        animate_thinking()
        
        hint = get_hint(secret, guess, attempts)
        print(hint)
        
        if guess == secret:
            print(colored(f"\n🎉 Victory! You guessed it in {attempts} attempts!", 'yellow'))
            print(f"Your guesses: {guess_history}")
            
            # Performance rating
            max_attempts = {
                Difficulty.EASY: 4,
                Difficulty.MEDIUM: 7,
                Difficulty.HARD: 10,
                Difficulty.EXTREME: 15
            }[difficulty]
            
            if attempts <= max_attempts // 2:
                print(colored("🏆 Legendary Guess Master!", 'cyan'))
            elif attempts <= max_attempts:
                print(colored("👍 Solid performance!", 'green'))
            else:
                print(colored("💪 Keep practicing!", 'blue'))
            break

def main():
    """Game entry point"""
    display_welcome()
    
    while True:
        difficulty = select_difficulty()
        play_round(difficulty)
        
        if input("\nPlay again? (y/n): ").lower() != 'y':
            print(colored("\nThanks for playing Number Wizard!", 'yellow'))
            print(colored("Come back for more guessing adventures!", 'cyan'))
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(colored("\n\nGame exited. See you next time!", 'red'))
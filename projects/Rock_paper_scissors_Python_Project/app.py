import random
import time
import sys
from termcolor import colored
import pyfiglet
from enum import Enum, auto

class Choice(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()
    LIZARD = auto()
    SPOCK = auto()

class Result(Enum):
    WIN = auto()
    LOSE = auto()
    DRAW = auto()

# Game rules matrix (who beats whom)
RULES = {
    Choice.ROCK: [Choice.SCISSORS, Choice.LIZARD],
    Choice.PAPER: [Choice.ROCK, Choice.SPOCK],
    Choice.SCISSORS: [Choice.PAPER, Choice.LIZARD],
    Choice.LIZARD: [Choice.SPOCK, Choice.PAPER],
    Choice.SPOCK: [Choice.SCISSORS, Choice.ROCK]
}

# Special move effects
MOVE_EFFECTS = {
    (Choice.ROCK, Choice.SCISSORS): "🪨 crushes ✂️",
    (Choice.ROCK, Choice.LIZARD): "🪨 crumbles 🦎",
    (Choice.PAPER, Choice.ROCK): "📄 covers 🪨",
    (Choice.PAPER, Choice.SPOCK): "📄 disproves 🖖",
    (Choice.SCISSORS, Choice.PAPER): "✂️ cuts 📄",
    (Choice.SCISSORS, Choice.LIZARD): "✂️ decapitates 🦎",
    (Choice.LIZARD, Choice.SPOCK): "🦎 poisons 🖖",
    (Choice.LIZARD, Choice.PAPER): "🦎 eats 📄",
    (Choice.SPOCK, Choice.SCISSORS): "🖖 smashes ✂️",
    (Choice.SPOCK, Choice.ROCK): "🖖 vaporizes 🪨"
}

def display_intro():
    """Show animated game intro"""
    print(colored(pyfiglet.figlet_format("RPSLS"), "cyan"))
    print(colored("~ The Ultimate Rock-Paper-Scissors-Lizard-Spock Showdown ~", "yellow"))
    time.sleep(1)
    print("\n" + colored("Classic game with a Big Bang Theory twist!", "magenta"))
    print(colored("Now with 5 moves instead of 3 for extra excitement!\n", "blue"))
    time.sleep(1)

def show_rules():
    """Display the game rules"""
    print(colored("\nGame Rules:", "green", attrs=["underline"]))
    rules = [
        "🪨 Rock crushes ✂️ Scissors",
        "🪨 Rock crumbles 🦎 Lizard",
        "📄 Paper covers 🪨 Rock",
        "📄 Paper disproves 🖖 Spock",
        "✂️ Scissors cut 📄 Paper",
        "✂️ Scissors decapitate 🦎 Lizard",
        "🦎 Lizard poisons 🖖 Spock",
        "🦎 Lizard eats 📄 Paper",
        "🖖 Spock smashes ✂️ Scissors",
        "🖖 Spock vaporizes 🪨 Rock"
    ]
    for rule in rules:
        print(colored(f"• {rule}", "cyan"))
        time.sleep(0.2)
    print()

def get_player_choice():
    """Get and validate player's move choice"""
    choices = {
        "1": Choice.ROCK,
        "2": Choice.PAPER,
        "3": Choice.SCISSORS,
        "4": Choice.LIZARD,
        "5": Choice.SPOCK
    }
    
    while True:
        print(colored("\nChoose your move:", "yellow"))
        print("1. 🪨 Rock")
        print("2. 📄 Paper")
        print("3. ✂️ Scissors")
        print("4. 🦎 Lizard")
        print("5. 🖖 Spock")
        
        choice = input("Enter your choice (1-5): ").strip()
        if choice in choices:
            return choices[choice]
        print(colored("Invalid choice! Please enter 1-5.", "red"))

def get_computer_choice():
    """Generate computer's move with dramatic effect"""
    print(colored("\nComputer is choosing...", "magenta"), end=" ")
    for _ in range(3):
        time.sleep(0.3)
        print(colored("💻", "blue"), end=" ", flush=True)
    print()
    
    return random.choice(list(Choice))

def determine_winner(player, computer):
    """Determine round winner based on rules"""
    if player == computer:
        return Result.DRAW
    return Result.WIN if computer in RULES[player] else Result.LOSE

def animate_battle(player_choice, computer_choice):
    """Show animated battle sequence"""
    print(colored("\n🔄 The battle begins!", "yellow"))
    moves = ["🪨", "📄", "✂️", "🦎", "🖖"]
    
    for _ in range(3):
        print(colored(random.choice(moves), "red"), end=" vs ", flush=True)
        print(colored(random.choice(moves), "blue"))
        time.sleep(0.2)
        sys.stdout.write("\033[F\033[K")  # Move cursor up and clear line
    
    print(colored(player_choice.name, "green"), end=" vs ")
    print(colored(computer_choice.name, "red"))

def show_result(result, player_choice, computer_choice):
    """Display round result with flair"""
    print()
    if result == Result.DRAW:
        print(colored("🤝 It's a draw!", "yellow"))
    elif result == Result.WIN:
        effect = MOVE_EFFECTS.get((player_choice, computer_choice), "beats")
        print(colored(f"🎉 You win! {player_choice.name} {effect} {computer_choice.name}", "green"))
    else:
        effect = MOVE_EFFECTS.get((computer_choice, player_choice), "beats")
        print(colored(f"💻 Computer wins! {computer_choice.name} {effect} {player_choice.name}", "red"))

def play_round(score):
    """Play one round of the game"""
    player = get_player_choice()
    computer = get_computer_choice()
    
    animate_battle(player, computer)
    result = determine_winner(player, computer)
    show_result(result, player, computer)
    
    if result == Result.WIN:
        score["player"] += 1
    elif result == Result.LOSE:
        score["computer"] += 1
    
    return score

def show_score(score):
    """Display current score"""
    print(colored(f"\n📊 Score: You {score['player']} - {score['computer']} Computer", "cyan"))

def play_game():
    """Main game loop"""
    display_intro()
    show_rules()
    
    score = {"player": 0, "computer": 0}
    rounds = 0
    
    while True:
        rounds += 1
        print(colored(f"\n=== Round {rounds} ===", "white", attrs=["bold"]))
        
        score = play_round(score)
        show_score(score)
        
        if input(colored("\nPlay another round? (y/n): ", "yellow")).lower() != "y":
            print(colored("\n🎮 Final Score:", "magenta", attrs=["bold"]))
            print(colored(f"You: {score['player']}  |  Computer: {score['computer']}", "cyan"))
            
            if score["player"] > score["computer"]:
                print(colored("🏆 You are the Ultimate Champion! �", "green", attrs=["bold"]))
            elif score["player"] < score["computer"]:
                print(colored("🤖 The machines win this time...", "red"))
            else:
                print(colored("🤝 It's a tie! The battle continues...", "yellow"))
            
            print(colored("\nThanks for playing!", "cyan"))
            break

if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print(colored("\n\nGame exited. Challenge me again soon!", "red"))
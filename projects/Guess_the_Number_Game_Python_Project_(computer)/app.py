import random
import time
from termcolor import colored
import pyfiglet  # For ASCII art

def display_welcome():
    """Show fancy welcome message with ASCII art"""
    print(colored(pyfiglet.figlet_format("Guess Master"), color='cyan'))
    print(colored("~ The Computer Number Guessing Challenge ~", 'yellow'))
    print("\nThink of a secret number between 1-100")
    print("I'll try to guess it with my computer brain!\n")
    time.sleep(1)

def get_user_feedback(guess):
    """Get and validate user feedback with colorful prompts"""
    while True:
        feedback = input(colored(
            f"\nMy guess is: {colored(guess, 'green', attrs=['bold'])} "
            f"\n[Higher/Lower/Correct]? ", 'yellow')).strip().lower()
        
        if feedback in {'h', 'higher'}:
            return 'higher'
        elif feedback in {'l', 'lower'}:
            return 'lower'
        elif feedback in {'c', 'correct'}:
            return 'correct'
        else:
            print(colored("⚠️ Please enter: (H)igher, (L)ower, or (C)orrect", 'red'))

def show_guess_animation(guess):
    """Display animated guessing effect"""
    print(colored("\nCalculating...", 'magenta'), end=' ')
    for _ in range(3):
        time.sleep(0.3)
        print(colored("•", 'blue'), end=' ', flush=True)
    print(colored(f"\nI choose: {guess}!", 'green', attrs=['bold']))

def computer_guesses_number():
    display_welcome()
    
    low, high = 1, 100
    attempts = 0
    guess_history = []
    strategy = "binary"  # Can switch to random if binary fails
    
    while True:
        # Alternate between strategies for variety
        if strategy == "binary":
            guess = (low + high) // 2
        else:
            guess = random.randint(low, high)
        
        show_guess_animation(guess)
        attempts += 1
        guess_history.append(guess)
        
        feedback = get_user_feedback(guess)
        
        if feedback == 'correct':
            print(colored(f"\n🎉 Computer Victory! Guessed in {attempts} attempts!", 'green'))
            print(colored(f"📊 Guess history: {guess_history}", 'cyan'))
            
            # Performance rating
            if attempts <= 6:
                print(colored("🏆 Mastermind Computer! Perfect binary search!", 'yellow'))
            elif attempts <= 10:
                print(colored("👍 Good job! Better than random!", 'blue'))
            else:
                print(colored("🤖 I'll get better next time!", 'magenta'))
            break
        
        # Adjust range based on feedback
        if feedback == 'higher':
            low = guess + 1
            print(colored(f"🔍 Okay, searching {low}-{high}...", 'cyan'))
        else:
            high = guess - 1
            print(colored(f"🔍 Okay, searching {low}-{high}...", 'cyan'))
        
        # Switch strategy if binary search seems inconsistent
        if attempts > 7 and random.random() < 0.3:
            strategy = "random"
            print(colored("\n💡 Switching to random probe strategy!", 'yellow'))
        
        # Check for cheating
        if low > high:
            print(colored("\n🤨 Hold on! Your feedback doesn't make sense!", 'red'))
            print(colored("I think you changed your number! Let's start over.\n", 'red'))
            time.sleep(2)
            computer_guesses_number()
            return

if __name__ == "__main__":
    try:
        computer_guesses_number()
        print(colored("\nThanks for playing Guess Master!", 'cyan'))
        print(colored("Want to challenge me again? Run the program!", 'yellow'))
    except KeyboardInterrupt:
        print(colored("\n\n👋 Game exited. Challenge me again soon!", 'red'))

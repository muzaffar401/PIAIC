import random
import string
import argparse
import pyfiglet
from colorama import init, Fore, Back, Style
import time
import sys
import os

# Initialize colorama
init(autoreset=True)

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    """Show a fancy banner"""
    clear_screen()
    banner = pyfiglet.figlet_format("PASSWORD  GEN", font="slant")
    print(Fore.CYAN + banner)
    print(Fore.YELLOW + "🔐 Create ultra-secure passwords with custom complexity 🔐")
    print(Fore.GREEN + "-" * 60 + "\n")

def animate_loading(message, duration=2):
    """Show a simple loading animation"""
    symbols = ["⣾","⣽","⣻","⢿","⡿","⣟","⣯","⣷"]
    end_time = time.time() + duration
    while time.time() < end_time:
        for symbol in symbols:
            sys.stdout.write(f"\r{Fore.MAGENTA}{message} {symbol} {Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.1)
    print("\r" + " " * (len(message) + 4) + "\r", end="")

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    """
    Generate a random secure password with customizable complexity.
    """
    # Define character sets with visual distinction
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special = '!@#$%^&*()_+-=[]{}|;:,.<>?/' if use_special else ''

    # Combine allowed characters based on user preferences
    all_chars = lowercase + uppercase + digits + special

    # Ensure at least one character from each selected set is included
    password = []
    if use_uppercase:
        password.append(Fore.BLUE + random.choice(uppercase))
    if use_digits:
        password.append(Fore.GREEN + random.choice(digits))
    if use_special:
        password.append(Fore.RED + random.choice(special))

    # Fill remaining length with random choices from all allowed characters
    remaining_length = length - len(password)
    colors = [Fore.WHITE, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]
    password.extend(random.choice(colors) + random.choice(all_chars) 
                for _ in range(remaining_length))

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    # Convert list to string and reset color at the end
    return ''.join(password) + Style.RESET_ALL

def calculate_strength(length, upper, digits, special):
    """Calculate password strength with visual indicators"""
    strength = 0
    if length >= 16: strength += 2
    elif length >= 12: strength += 1
    
    if upper: strength += 1
    if digits: strength += 1
    if special: strength += 2
    
    # Strength meter visualization
    if strength >= 6:
        meter = Fore.GREEN + "██████████" + Style.RESET_ALL
        rating = "Excellent"
    elif strength >= 4:
        meter = Fore.YELLOW + "██████▁▁▁▁" + Style.RESET_ALL
        rating = "Good"
    elif strength >= 2:
        meter = Fore.RED + "████▁▁▁▁▁▁" + Style.RESET_ALL
        rating = "Weak"
    else:
        meter = Fore.RED + "██▁▁▁▁▁▁▁▁" + Style.RESET_ALL
        rating = "Poor"
    
    return meter, rating

def get_user_preferences():
    """Get password generation preferences from user"""
    display_banner()
    
    # Get password length
    while True:
        try:
            length = int(input(f"{Fore.CYAN}Password length (8-32, 12-16 recommended): {Style.RESET_ALL}"))
            if 8 <= length <= 32:
                break
            print(Fore.RED + "Please enter between 8 and 32")
        except ValueError:
            print(Fore.RED + "Please enter a valid number")

    # Get complexity options with default suggestions
    print(f"\n{Fore.YELLOW}Complexity options (recommend Y for all):")
    use_uppercase = input(f"{Fore.CYAN}Include uppercase letters? (Y/n): {Style.RESET_ALL}").lower() in ('', 'y', 'yes')
    use_digits = input(f"{Fore.CYAN}Include digits? (Y/n): {Style.RESET_ALL}").lower() in ('', 'y', 'yes')
    use_special = input(f"{Fore.CYAN}Include special characters? (Y/n): {Style.RESET_ALL}").lower() in ('', 'y', 'yes')

    return length, use_uppercase, use_digits, use_special

def main():
    """Main program entry point."""
    while True:
        # Get user preferences
        length, upper, digits, special = get_user_preferences()
        
        # Generate with animation
        animate_loading("Generating secure password")
        
        # Generate and display password
        password = generate_password(length, upper, digits, special)
        
        # Display results
        display_banner()
        print(f"\n{Fore.GREEN}🔒 Your secure password: {Style.BRIGHT}{password}{Style.RESET_ALL}")
        
        # Show strength meter
        meter, rating = calculate_strength(length, upper, digits, special)
        print(f"\n{Fore.WHITE}Password strength: {meter} {rating}")
        
        # Additional info
        print(f"\n{Fore.YELLOW}📊 Password details:")
        print(f"{Fore.CYAN}Length:{Fore.WHITE} {length} characters")
        print(f"{Fore.CYAN}Complexity:{Fore.WHITE} {'✅' if upper else '❌'} Uppercase | {'✅' if digits else '❌'} Digits | {'✅' if special else '❌'} Special chars")
        
        # Safety tips
        print(f"\n{Fore.RED}⚠️ Important security tips:")
        print(f"{Fore.WHITE}• Never share passwords")
        print(f"{Fore.WHITE}• Use a password manager")
        print(f"{Fore.WHITE}• Enable two-factor authentication")
        print(f"{Fore.WHITE}• Change passwords periodically")
        
        # Ask to generate another
        if input(f"\n{Fore.MAGENTA}Generate another password? (Y/n): {Style.RESET_ALL}").lower() in ('n', 'no'):
            print(f"\n{Fore.GREEN}🚀 Stay secure! Goodbye!")
            time.sleep(1)
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}⏹ Operation cancelled")
        sys.exit(0)
import sys
import time
from datetime import datetime, timedelta
import winsound  # Windows only for beeps
import os
import random
from colorama import init, Fore, Back, Style
import pyfiglet

# Initialize colorama
init(autoreset=True)

def play_sound(duration_ms=500, freq=880):
    """Play a simple beep sound (Windows only)"""
    try:
        winsound.Beep(freq, duration_ms)
    except:
        pass  # Silently fail on non-Windows systems

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    """Display a fancy banner"""
    clear_screen()
    banner = pyfiglet.figlet_format("COUNTDOWN TIMER", font="slant")
    print(Fore.CYAN + banner)
    print(Fore.YELLOW + "🚀 Enhanced Countdown Timer with Visual Effects 🎆")
    print(Fore.GREEN + "Enter time in seconds (e.g., '10') or MM:SS (e.g., '1:30')\n")

def get_emoji_progress(progress):
    """Return progress bar using emojis"""
    bars = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪"]
    filled = int(progress * 20)
    return "".join([bars[i % len(bars)] for i in range(filled)]) + "⬜" * (20 - filled)

def countdown_timer():
    """Enhanced countdown timer with visual effects"""
    show_banner()
    
    while True:
        # Smart input parsing
        user_input = input(f"\n{Fore.MAGENTA}Set timer: {Style.RESET_ALL}").strip()

        # Handle MM:SS format
        if ':' in user_input:
            try:
                parts = user_input.split(':')
                if len(parts) == 2:  # MM:SS
                    m, s = map(int, parts)
                    if s >= 60 or m < 0 or s < 0:
                        print(Fore.RED + "❌ Invalid! Use MM:SS (0-59 seconds)")
                        continue
                    duration = m * 60 + s
                elif len(parts) == 3:  # HH:MM:SS
                    h, m, s = map(int, parts)
                    if s >= 60 or m >= 60 or h < 0 or m < 0 or s < 0:
                        print(Fore.RED + "❌ Invalid! Use HH:MM:SS format")
                        continue
                    duration = h * 3600 + m * 60 + s
            except ValueError:
                print(Fore.RED + "❌ Invalid format! Try '1:30' or '90'")
                continue
        # Handle seconds format
        else:
            try:
                duration = int(user_input)
                if duration <= 0:
                    print(Fore.RED + "❌ Must be positive number!")
                    continue
            except ValueError:
                print(Fore.RED + "❌ Numbers only please!")
                continue

        # Calculate end time
        end_time = datetime.now() + timedelta(seconds=duration)
        print(f"\n{Fore.BLUE}⏱ Counting down {duration} seconds... (Ctrl+C to stop){Style.RESET_ALL}")
        time.sleep(1)

        try:
            while datetime.now() < end_time:
                clear_screen()
                show_banner()
                
                remaining = (end_time - datetime.now()).total_seconds()
                progress = 1 - (remaining / duration)
                
                # Calculate time components
                mins, secs = divmod(int(remaining), 60)
                hours, mins = divmod(mins, 60)
                
                # Display fancy timer
                print(f"\n{Fore.GREEN}Time remaining:{Style.RESET_ALL}")
                if hours > 0:
                    print(f"{Fore.YELLOW}{hours:02d}:{mins:02d}:{secs:02d}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.YELLOW}{mins:02d}:{secs:02d}{Style.RESET_ALL}")
                
                # Visual progress
                print(f"\n{get_emoji_progress(progress)} {progress*100:.1f}%")
                
                # Random motivational messages
                if remaining < 10:
                    print(f"\n{Fore.RED}HURRY! Almost there! ⏰")
                elif progress > 0.8:
                    print(f"\n{Fore.YELLOW}Final stretch! 💪")
                elif progress > 0.5:
                    print(f"\n{Fore.CYAN}Keep going! 🚀")
                else:
                    print(f"\n{Fore.GREEN}You've got this! 👍")
                
                # Play ticking sound in last 10 seconds
                if remaining < 10:
                    play_sound(200, 800 + int(remaining * 20))
                
                time.sleep(0.1)

            # Timer complete effects
            clear_screen()
            print(Fore.RED + pyfiglet.figlet_format("TIME'S UP!", font="banner"))
            print(Fore.YELLOW + "🔔" * 20 + Style.RESET_ALL)
            
            # Celebration sound
            for freq in [440, 660, 880, 660, 880, 1320]:
                play_sound(200, freq)
                time.sleep(0.1)

        except KeyboardInterrupt:
            print(f"\n\n{Fore.YELLOW}⏹ Timer stopped{Style.RESET_ALL}")

        # Ask to continue
        if input(f"\n{Fore.MAGENTA}New timer? (y/n): {Style.RESET_ALL}").lower() != 'y':
            print(Fore.CYAN + "\n👋 Goodbye!")
            time.sleep(1)
            clear_screen()
            break

if __name__ == "__main__":
    countdown_timer()
import random, time, sys
from collections import defaultdict
from string import Formatter

# Expanded dictionary of story templates with more themes and variations
TEMPLATES = {
    "fantasy": [
        "The {adjective} {noun} {verb} through the enchanted forest, leaving a trail of sparkling {noun_2}.",
        "A {adjective} wizard summoned a {noun} that could {verb} with unimaginable power.",
        "The {noun} of {adjective} destiny began to {verb} when the {noun_2} prophecy was fulfilled.",
        "In the kingdom of {noun}, the {adjective} knight had to {verb} the magical {noun_2} to save the princess.",
        "The {adjective} dragon {verb} over the mountains, guarding its treasure of {noun} and {noun_2}."
    ],
    "sci-fi": [
        "On planet {noun}, the {adjective} aliens learned to {verb} in zero gravity using {noun_2}.",
        "The {adjective} quantum {noun} started to {verb}, causing a paradox in the {noun_2} continuum.",
        "Commander {noun} ordered the crew to {verb} the {adjective} hyperdrive before the {noun_2} collapsed.",
        "The {adjective} AI {verb} its way into the {noun} network, threatening all {noun_2} in the system.",
        "Agent {noun} had to {verb} the {adjective} device before the {noun_2} could destroy the space station."
    ],
    "horror": [
        "In the {adjective} house on {noun} street, something began to {verb} in the {noun_2}.",
        "The {adjective} {noun} {verb} through the fog, searching for its next {noun_2}.",
        "When the {noun} {verb}, the {adjective} figure appeared holding a {noun_2}.",
        "The {adjective} curse caused anyone who {verb} near the {noun} to become {noun_2}.",
        "Dr. {noun}'s {adjective} experiment started to {verb}, creating monstrous {noun_2}."
    ],
    "adventure": [
        "The {adjective} explorer {verb} into the unknown {noun}, discovering ancient {noun_2}.",
        "After {verb} for days, we found the {adjective} {noun} hidden beneath the {noun_2}.",
        "The map to the {adjective} {noun} {verb} just when we needed it most, leading to {noun_2}.",
        "Our {adjective} guide told us to {verb} before approaching the sacred {noun} of {noun_2}.",
        "The {noun} {verb} violently as we tried to cross the {adjective} river of {noun_2}."
    ],
    "romance": [
        "When our eyes met across the {noun}, I knew this {adjective} feeling would make me {verb}.",
        "The {adjective} letter from {noun} made my heart {verb} like never before, despite the {noun_2}.",
        "On our {adjective} date, we {verb} under the {noun} while sharing a {noun_2}.",
        "The {noun} of our love began to {verb} when we discovered our shared passion for {adjective} {noun_2}.",
        "After {verb} through the park, we found the most {adjective} {noun} that reminded us of our first {noun_2}."
    ],
    "mystery": [
        "The {adjective} case of the missing {noun} took a turn when the detective found the victim had {verb} the {noun_2}.",
        "In the {noun} mansion, the {adjective} clue made us {verb} the butler's connection to the {noun_2}.",
        "The {noun} {verb} mysteriously every night at exactly {noun_2}, but no one knew why it was so {adjective}.",
        "When the {adjective} {noun} started to {verb}, we realized the {noun_2} held the answer to the crime.",
        "Journalist {noun} discovered the {adjective} conspiracy that made even the police {verb} about the {noun_2}."
    ]
}

# Special effects dictionary for each theme
THEME_EFFECTS = {
    "fantasy": "✨",
    "sci-fi": "🚀",
    "horror": "👻",
    "adventure": "🗺️",
    "romance": "💖",
    "mystery": "🕵️"
}

# Dictionary to track word types with examples
WORD_EXAMPLES = {
    "noun": ["dragon", "castle", "sword", "wizard"],
    "adjective": ["sparkling", "mysterious", "ancient", "powerful"],
    "verb": ["fly", "disappear", "transform", "whisper"],
    "noun_2": ["artifact", "prophecy", "kingdom", "treasure"]
}

def typewriter(text, delay=0.03, theme=None):
    """Enhanced typewriter effect with theme decorations"""
    if theme and theme in THEME_EFFECTS:
        sys.stdout.write(THEME_EFFECTS[theme] + " ")
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        # Vary delay slightly for more natural effect
        time.sleep(delay * random.uniform(0.8, 1.2))
    print()

def get_input(prompt, word_type=None):
    """Improved input function with word type hints"""
    if word_type:
        examples = random.sample(WORD_EXAMPLES.get(word_type, []), 2)
        prompt += f" (e.g., {', '.join(examples)}): "
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input.lower()
        print("Please enter a value!")

def generate(theme, words):
    """Generate story with error handling"""
    try:
        template = random.choice(TEMPLATES[theme])
        # Count placeholders to ensure we have enough words
        required_words = set([name for _, name, _, _ in Formatter().parse(template) if name])
        if all(word in words for word in required_words):
            return template.format(**words)
        return "Oops! Missing some words to complete the story."
    except KeyError:
        return "Invalid theme selected!"

def show_theme_intro(theme):
    """Display themed introduction"""
    if theme in THEME_EFFECTS:
        decor = THEME_EFFECTS[theme] * 3
        print(f"\n{decor} {theme.upper()} STORY {decor}\n")

def main():
    print("\n📝✨ Welcome to Enhanced CLI Mad Libs! ✨📝\n")
    print("Create hilarious stories by filling in the blanks.\n")
    
    score = 0
    story_count = 0
    
    while True:
        # Display theme options with decorations
        themes = list(TEMPLATES.keys())
        print("\nChoose a story theme:")
        for i, t in enumerate(themes, 1):
            print(f"{i}. {THEME_EFFECTS.get(t, '')} {t.capitalize()}")

        # Get theme choice with validation
        choice = get_input("\nEnter theme number (1-{}): ".format(len(themes)))
        if not choice.isdigit() or not (1 <= int(choice) <= len(themes)):
            print("Please enter a valid number!")
            continue

        theme = themes[int(choice)-1]
        show_theme_intro(theme)
        
        # Collect words with helpful prompts
        words = {
            "noun": get_input("Enter a noun", "noun"),
            "adjective": get_input("Enter an adjective", "adjective"),
            "verb": get_input("Enter a verb", "verb")
        }
        
        # Some themes need additional words
        if random.random() > 0.3:  # 70% chance of needing extra word
            words["noun_2"] = get_input("Enter another noun", "noun_2")
        
        # Generate and display story
        story = generate(theme, words)
        print("\nYour masterpiece:\n" + "="*50)
        typewriter(story, theme=theme)
        print("="*50)
        
        story_count += 1
        score += len(story.split())  # Score based on story length
        
        # Offer to play again or quit
        again = get_input("\nPlay again? (y/n): ")
        if again not in ["y", "yes"]:
            print(f"\n🌟 You created {story_count} stories with a total score of {score}! 🌟")
            print("\nThanks for playing Enhanced CLI Mad Libs! Come back soon!\n")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Hope you had fun!")
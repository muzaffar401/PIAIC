# Hangman Game - Python Terminal Edition

## Overview
A colorful, interactive Hangman game built with Python that runs in your terminal. This version features enhanced ASCII art, multiple word categories, scoring system, and hint functionality.

## Features

🎨 **Colorful Interface**: Uses termcolor and pyfiglet for an engaging visual experience  
📚 **Multiple Categories**: Choose from Programming, Animals, Countries, or Movies  
💡 **Hint System**: Get help when you're stuck (limited hints available)  
📊 **Scoring**: Earn points for correct guesses, lose points for hints  
🎭 **ASCII Art**: Animated hangman that progresses with each wrong guess  
🔄 **Play Again**: Option to restart the game after each round  

## Gameplay Mechanics

- Guess letters one at a time or attempt the whole word
- Limited attempts before the hangman is complete
- Receive visual feedback on correct/incorrect guesses
- Track your score based on performance
- Category selection adds replay value

## Requirements

- Python 3.x
- Required packages:
  - `termcolor`
  - `pyfiglet`
  - `random` (standard library)
  - `time` (standard library)
  - `os` (standard library)

## How to Play

1. Run the Python script in your terminal
2. Select a word category from the menu
3. Guess letters to reveal the hidden word
4. Use hints strategically when needed
5. Try to solve the puzzle before the hangman drawing is complete!

## Scoring System

- +5 points for each correct letter guess
- +20 points for correct word guess
- -3 points for using a hint
- Bonus points for remaining attempts when you win

Enjoy this classic word game with a modern terminal twist!
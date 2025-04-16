# 🔢 Mind Reader: The Number Guessing Game 🎯

Welcome to **Mind Reader**, where your computer tries to guess your secret number through binary magic! This Python-powered CLI game turns the classic number guessing concept upside down - you think of a number, and the computer figures it out!

## ✨ Key Features

### 🧩 Clever Number Detection
- **Binary Search Algorithm**: Efficiently narrows down possibilities
- **Adaptive Strategy**: Switches approaches when needed
- **Guess History**: See the computer's thought process

### 🎮 Interactive Gameplay
- **Simple Commands**: Respond with Higher (H), Lower (L), or Correct (C)
- **Cheat Detection**: Catches inconsistent player feedback
- **Performance Rating**: Evaluates the computer's guessing efficiency

### 🖥️ Terminal Magic
- Colorful console interface
- Animated guessing effects
- ASCII art title screen
- Emoji-enhanced feedback

## 📊 How It Works

```text
1. You think of a number (1-100)
2. Computer makes guesses
3. You provide feedback:
   - Higher (number is greater)
   - Lower (number is smaller)
   - Correct (guessed right)
4. Computer narrows down range
5. Repeat until correct guess!
```

## 🏆 Performance Tiers

| Attempts | Rating          | Badge  |
|----------|-----------------|--------|
| ≤ 6      | Binary Wizard   | 🏆     |
| ≤ 10     | Skilled Guesser | 👍     |
| > 10     | Still Learning  | 🔍     |

## 🎯 Sample Gameplay

```text
💭 Computer is thinking...
My guess is: 50 
[Higher/Lower/Correct]? h
🔍 Okay, searching 51-100...

🎉 Correct! Guessed in 5 attempts!
📊 Guess history: [50, 75, 88, 94, 97]
🏆 Binary Wizard! Perfect performance!
```

## 🚀 Getting Started

1. Install requirements:
   ```bash
   pip install termcolor pyfiglet
   ```
2. Run the game:
   ```bash
   python number_guesser.py
   ```

## 💡 Why This Game?

- Demonstrates **binary search** in action
- Great for **quick mental challenges**
- Clean **Python code example**
- Fun **human-computer interaction**

---

<div align="center">
Made with ❤️ using Python<br>
"The computer knows what number you're thinking of!"
</div>
```

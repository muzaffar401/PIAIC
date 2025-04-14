# 🐍 Hello World - Python Greeter (Task 1)

This project is a beginner-friendly Python task demonstrating how to use object-oriented programming and testing in Python.

## ✅ Objective

Create a Python program that prints a personalized "Hello, World" message using a class and test it using `pytest`.

---

## 🚀 Features

- Uses a `Greeter` class built with Python's `@dataclass` decorator.
- Supports custom greeting names (e.g., "Hello, Muzaffar").
- Includes unit tests with `pytest` to verify functionality.

---

## 📂 Project Structure

task-1/
├── hello_world/
│   ├── main.py           # Contains the Greeter class
│   └── __init__.py       # Makes it a Python package
├── test/
│   ├── __init__.py       # Makes the test folder a Python package
│   └── test_greeter.py   # Contains test cases for the Greeter class
├── requirements.txt      # (Optional) List of dependencies
└── README.md             # Project description


---

## 🧪 Testing

Test cases are written using `pytest`. They verify that:
- The default greeting is `"Hello, World"`.
- A custom name (like `"Muzaffar"`) returns `"Hello, Muzaffar"`.

---

## 🧠 Concepts Covered

- Python `@dataclass`
- Writing clean class-based code
- Creating and running unit tests with `pytest`
- Basic Python packaging and module structure

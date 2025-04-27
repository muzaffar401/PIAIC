# 📚 Grading System & Age Checker Program (Python Beginner Project)

## 📌 About This Project

This project includes **two small Python programs**:
1. **Grading System** ➔ It asks the user for their percentage and shows their grade (A1, A, B, C, D, F).
2. **Age Checker** ➔ It asks the user for their age and tells whether they are a child, teenager, adult, or senior citizen.

Both programs use **`if`, `elif`, and `else`** statements.  
This project is **perfect for beginners** who are learning decision-making in Python!

---

## 🖥️ Grading System Program

```python
percentage = int(input("Enter Your Percentage % :"))

# using nested if else
if percentage >= 0 and percentage <= 100:  # Check if percentage is valid
    if percentage >= 90:
        print("A1 Grade")
    elif percentage >= 80:
        print("A Grade")
    elif percentage >= 70:
        print("B Grade")
    elif percentage >= 60:
        print("C Grade")
    elif percentage >= 50:
        print("D Grade")
    else:
        print("F Grade (FAIL)")
else:
    print(f"{percentage}% is invalid percentage")
```

### 🔵 Program Explanation:

- First, the program **asks the user** to enter their percentage.
- Then it **checks** if the percentage is between **0 and 100**.
- If it is valid, it checks:
  - **90% or more** ➔ A1 Grade
  - **80% to 89%** ➔ A Grade
  - **70% to 79%** ➔ B Grade
  - **60% to 69%** ➔ C Grade
  - **50% to 59%** ➔ D Grade
  - **Below 50%** ➔ F Grade (FAIL)
- If the percentage is not between 0 and 100, it prints an **invalid percentage message**.

---

## 🖥️ Age Checker Program

```python
age = int(input("Enter Your Age :"))

if age >= 0 and age <= 100:
    if age <= 13:
        print("You are a Child.")
    elif age <= 20:
        print("You are a Teenager.")
    elif age <= 60:
        print("You are an Adult.")
    elif age <= 100:
        print("You are a Senior Citizen.")
else:
    print(f"Invalid Age {age} :(")
```

### 🔵 Program Explanation:

- First, the program **asks the user** to enter their age.
- Then it **checks** if the age is between **0 and 100**.
- If it is valid, it checks:
  - **0 to 13 years** ➔ Child
  - **14 to 20 years** ➔ Teenager
  - **21 to 60 years** ➔ Adult
  - **61 to 100 years** ➔ Senior Citizen
- If the age is not between 0 and 100, it shows an **invalid age message**.

---

## 🧠 If-Elif-Else Structure Flow Diagram


```
┌───────────────────────┐
│      Start Program    │
└──────────┬────────────┘
           │
┌──────────▼────────────┐
│   Condition Check     │
│  (if condition)       │
└──────────┬────────────┘
           ├───────────────┐
           │ True          │ False
┌──────────▼────────────┐ ┌──────────▼────────────┐
│  Execute if-block     │ │  Check next condition │
│  (code inside if)     │ │  (elif condition)     │
└───────────────────────┘ └──────────┬────────────┘
                                     ├───────────────┐
                                     │ True          │ False
                             ┌───────▼───────┐ ┌─────▼──────┐
                             │ Execute elif   │ │  Check next│
                             │ (1st elif)     │ │  elif/else │
                             └───────┬───────┘ └─────┬──────┘
                                     │               │
                                     │               │
                             ┌───────▼───────┐ ┌─────▼──────┐
                             │  More elifs?  │ │ Execute    │
                             │  (if any)     │ │ else-block │
                             └───────┬───────┘ └─────┬──────┘
                                     │               │
                                     └──────┬────────┘
                                            │
                                   ┌────────▼────────┐
                                   │   End Program   │
                                   └─────────────────┘
```

### Key Explanation:
1. The program **starts** and evaluates the first `if` condition.
2. If **True** → Executes the `if` block and **skips all `elif/else`**.
3. If **False** → Moves to the next `elif` condition (if any).
4. If **all `if/elif` are False** → Executes the `else` block (if present).
5. The program **ends** after executing any matching block.

---

### Example Flow for `Grading System`:
```
Start
  │
  ▼
Enter Percentage: 85%
  │
  ▼
Check: 85 >= 90? False → Move to elif
  │
  ▼
Check: 85 >= 80? True → Print "A Grade"
  │
  ▼
Skip all remaining elif/else
  │
  ▼
End Program
```

---

## 📢 Key Points for Beginners:

- **`if`** ➔ Runs a block of code if a condition is true.
- **`elif`** ➔ Runs when the first `if` is false but another condition is true.
- **`else`** ➔ Runs when none of the `if` or `elif` conditions are true.
- **Nested if-else** ➔ Means using `if` inside another `if`, useful for checking multiple conditions.

---

## 🚀 How to Run This Program?

1. Install Python on your computer.
2. Copy the code into a file (for example: `app.py`).
3. Open your terminal or Python IDE and run the file:

```bash
python app.py
```

4. Enter your inputs and see the results!

---

## 🎯 Final Tip:

> **The more you practice writing simple programs, the better you will become! Keep practicing, keep learning! 💻✨**



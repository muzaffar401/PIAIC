# 📘 Assignment & Functions Summary

## 📝 Lambda Function Assignments

### ✅ Squaring a Number

This lambda function uses the `math.sqrt()` method to find the square root of a number.

```python
import math
square = lambda a: math.sqrt(a) 
result = int(square(64))
print(result)
```

### ✅ Multiplying Two Numbers

This lambda function multiplies two numbers.

```python
multiply = lambda a, b: a * b
result = multiply(5, 6)
print(result)
```

### ✅ Checking if a Number is Positive

This lambda function checks if a number is positive (zero or greater).

```python
condition = lambda a: a >= 0
input_num = int(input("Enter number: "))
result = condition(input_num)
if result:
    print(f"{input_num} is a positive number")
else:
    print(f"{input_num} is a negative number")
```

---

## 🧮 Basic Calculator

This function performs basic arithmetic operations based on the operator entered by the user.

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator: ")

def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        print("Invalid operator")

calculate(num1, num2, operator)
```

---

## 🍎 Food Calories Counter

This function calculates total calories based on three fruits entered by the user. It uses a dictionary with calorie values.

```python
def calculate_food_caleries():
    data = {
        "apple": 89,
        "banana": 76,
        "grapes": 65,
        "orange": 86,
        "kiwi": 55,
    }

    fruit_1 = input("Enter your first fruit: ").lower()
    fruit_2 = input("Enter your second fruit: ").lower()
    fruit_3 = input("Enter your third fruit: ").lower()

    total = 0

    for food in [fruit_1, fruit_2, fruit_3]:
        print(f"Fruit: {food}")
        if food in data:
            total += data[food]
        else:
            print(f"Sorry, {food} is not in the list of available fruits.")

    print(f"Total calories: {total}")

calculate_food_caleries()
```

---

## 🔁 Python Function Topics

### ✅ Simple Function

A basic function that prints a message.

```python
def function_name():
    print("Hello world")
function_name()
```

### ✅ Function with Return

Returns a value instead of printing it.

```python
def function_name():
    return "hello world"
result = function_name()
print(f"result : {result}")
```

### ✅ Function with Parameters

Accepts arguments directly.

```python
def sum(a, b):
    print(a + b)
sum(5, 6)  # Positional arguments
```

### ✅ Function with Default Parameter

Uses a default value if none is provided for that parameter.

```python
def name(f_name, l_name="ahmed"):
    print(f"{f_name} {l_name}")
name("muzaffar")  # l_name is default
```

### ✅ Function with Keyword Argument

Allows changing the order by naming parameters.

```python
def info(name, age, roll_no):
    print(f"name : {name} age : {age} roll_no : {roll_no}")
info(age=18, name="muzaffar", roll_no=94993)
```

### ✅ Multiple Positional Arguments

Functions that accept unlimited positional arguments using `*args`.

#### Example 1:

```python
def total(*numbers):
    total_number = 0
    for num in numbers:
        total_number += num
    return total_number
print(total(1, 2, 3, 4))
```

#### Example 2:

```python
def names(*name):
    for i in name:
        print(i)
names("muzaffar", "ahmed", "bilal")
```

### ✅ Multiple Keyword Arguments

Functions that accept unlimited keyword arguments using `**kwargs`.

```python
def data(**keywrd):
    for key, value in keywrd.items():
        print(f"{key} : {value}")
data(name="muzaffar", age=21, gender="male")
```

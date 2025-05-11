#Assignment  using lambda function

# Squaring a number
import math
square = lambda a: math.sqrt(a) 
result = int(square(64))
print(result)


# multiplying two numbers 
multiply = lambda a,b: a*b
result = multiply(5,6)
print(result)


# Checking if a number is positive

condition = lambda a: a >= 0
input = int(input("enter number"))
result = condition(input)
if result:
    print(f"{input} is a positive number")
else:
    print(f"{input} is a negative number")

# calculator

num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
operator = input("enter operator")

def calculate(num1,num2,operator):

    if operator == "+":
      return num1 + num2
    elif operator == "-":
      return num1 - num2
    elif operator == "*":
      return num1 * num2
    elif operator == "/":
      return num1 / num2
    else:
      print("invalid operator")


calculate(num1,num2,operator)




def calculate_food_caleries():
    data = {
        "apple": 89,
        "banana": 76,
        "grapes": 65,
        "orange": 86,
        "kiwi": 55,
    }
    
    fruit_1 = input("Enter your first fruit: ").lower()  # Convert to lowercase
    fruit_2 = input("Enter your second fruit: ").lower()  # Convert to lowercase
    fruit_3 = input("Enter your third fruit: ").lower()  # Convert to lowercase

    total = 0

    for food in [fruit_1, fruit_2, fruit_3]:
        print(f"Fruit: {food}")
        if food in data:
            total += data[food]
        else:
            print(f"Sorry, {food} is not in the list of available fruits.")

    print(f"Total calories: {total}")


calculate_food_caleries()


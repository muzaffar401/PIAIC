# Function ek block hota hai code ka jo hum ek naam de kar baar baar chala sakte hain.
# Yani ek dafa likho, aur jitni baar chaho use karo time bachata hai aur code saaf rehta hai.

# Simple function banaya
def hello():
    print("Assalamualaikum, ye mera pehla function hai")

# Function call kiya
hello() # output me ayega Assalamualaikum, ye mera pehla function hai


# Function with parameter (value dena)
def greet(name):
    print("Hello", name, "welcome!")

# Function me naam diya
greet("Muzaffar")  # output Hello Muzaffar Welcom


# Function with 2 parameters
def add(a, b):
    print("Dono numbers ka total hai:", a + b)

add(5, 10)  # Output: 15
add(20, 10)  # Output: 30

# with multiply
def add(a, b):
    print("Dono numbers ko multiply kiya ", a * b)

add(5, 10)  # Output: 50
add(20, 10)  # Output: 20


# Function jo value return karta hai
def square(n):
    return n * n  # return matlab value ko wapas bhejna

result = square(6)
print("square hai:", result)  # Output: 36



# Return ka faida value ko kahin aur use bhi kar sakte ho
def get_name():
    return "Muzaffar"

name = get_name()
print("mera naam hai:", name)


# Function with if condition
def check_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(7))  # output: Odd hai
print(check_even(2)) #output :  even he


# Function with default value
def say_hi(name="Muzaffar"):
    print("Hi", name)
#ye default value print karega qk parameter me dee he
say_hi()           #output : Muzaffar

# ye Ahmed print karega qk hamne isko khud value di he 
say_hi("Ahmed")    # output Ahmed 






#function is a reusable block of code that runs only when you call it 

#simple function
def function_name():
    print("Hello world")
function_name()

#function with return 
def function_name():
    return "hello world"
function_name()
result = function_name()
print(f"result : {result}")

# function with parameter
def sum(a,b):
    print(a + b)
sum(5,6) # positional argument


# function with default parameter
def name(f_name,l_name="ahmed"):
    print(f"{f_name} {l_name}")
name("muzaffar") # l_name is default parameter so output is muzaffar ahmed


# function with keyword argument
def info(name,age,roll_no):
    print(f"name : {name} age : {age} roll_no : {roll_no}")
info(age=18,name="muzaffar",roll_no=94993) # keyword dekar argument aage peeche desakte hen


# multiple positional argument 
# example #1
def total(*numbers):
    total_number = 0
    for num in numbers:
      total_number += num
    return total_number
print(total(1, 2, 3, 4)) #unlimited positional arguments desakte hen

# example #2
def names(*name):
    for i in name:
        print(i)
names("muzaffar","ahmed","bilal") #unlimited positional arguments desakte hen


# multiple keyword argument
def data(**keywrd):
    for key,value in keywrd.items():
        print(f"{key} : {value}")
data(name="muzaffar",age=21,gender="male") # multiple keyword with argument









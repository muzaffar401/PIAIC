# List Methods 

# Index
fruits:list = ["banana", "apple", "orange", "mango"]
print(fruits[2])  # Output: orange

# List methods check karne ke liye
print([list_methods for list_methods in dir(list) if list_methods[:2] != '__'])
# Yeh line list ke sirf woh methods dikhati hai jo __ se start nahi hotay yani sirf normal (public) methods.

# append
# add karega item last me 
fruits:list = ["banana", "apple", "orange", "mango"]
fruits.append("pineapple")
print("append list:", fruits)
# Output: ['banana', 'apple', 'orange', 'mango', 'pineapple']

# clear
# poory list clear kardega
fruits:list = ["banana", "apple", "orange", "mango"]
fruits.clear()
print("clear list:", fruits)
# Output: []

# copy
# copy list bana kar dega orignal list se
fruits:list = ["banana", "apple", "orange", "mango"]
copy_fruits = fruits.copy()
print("copy list:", copy_fruits)
# Output: ['banana', 'apple', 'orange', 'mango']

# count
# list me specific element count karega 
fruits:list = ["banana", "apple", "apple", "mango"]
print("count of apple:", fruits.count("apple"))
# Output: 2

# extend
# do list ko apas me jordega milaa dega
fruits:list = ["banana", "apple"]
more_fruits = ["guava", "melon"]
fruits.extend(more_fruits)
print("extend list:", fruits)
# Output: ['banana', 'apple', 'guava', 'melon']

# index
# specific element ka index batayega
fruits:list = ["banana", "apple", "orange", "mango"]
print("index of mango:", fruits.index("mango"))
# Output: 3

# insert
# element add karega lekin sath index bhi puchega 
fruits:list = ["banana", "apple", "orange", "mango"]
fruits.insert(1, "strawberry")
print("insert list:", fruits)
# Output: ['banana', 'strawberry', 'apple', 'orange', 'mango']

# pop
# last element ko hata dega lekin index bhi  desakte hen 
fruits:list = ["banana", "apple", "orange", "mango"]
fruits.pop()
print("pop list:", fruits)
# Output: ['banana', 'apple', 'orange']

# remove
# specific element ko remove karega
fruits:list = ["banana", "apple", "orange", "mango"]
fruits.remove("orange")
print("remove list:", fruits)
# Output: ['banana', 'apple', 'mango']

# reverse
# list ke elements ko reverse kardega
fruits:list = ["banana", "apple", "orange", "mango"]
fruits.reverse()
print("reverse list:", fruits)
# Output: ['mango', 'orange', 'apple', 'banana']

# sort
# list ke elements ki sorting karega means 
fruits:list = ["banana", "apple", "orange", "mango"]
fruits.sort()
print("sorted list:", fruits)
# Output: ['apple', 'banana', 'mango', 'orange']

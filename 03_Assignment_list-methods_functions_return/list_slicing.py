#simple slice: index 1 se 4 se pehle tak (yaani 1, 2, 3)
#           0          1         2         3        4        5
fruits1 = ["banana", "apple", "orange", "mango", "grapes", "melon"]
print(fruits1[1:4])  # ['apple', 'orange', 'mango']
# Yani index 1 se start karo aur 4 se pehle tak print karo

# slice start me kuch nhi diya to default 0 index se le kar index 3 tak 
#            0          1         2         3        4        5
fruits2 = ["banana", "apple", "orange", "mango", "grapes", "melon"]
print(fruits2[:3])  # ['banana', 'apple', 'orange']

#  slice index 2 se end tak 
# means end me kuch nhi to complete end tak print karke dega

fruits3 = ["banana", "apple", "orange", "mango", "grapes", "melon"]
print(fruits3[2:])  # ['orange', 'mango', 'grapes', 'melon']


# 4. negative index se slice  
# last ke 3 items print karo
fruits4 = ["banana", "apple", "orange", "mango", "grapes", "melon"]
print(fruits4[-3:])  # ['mango', 'grapes', 'melon']
# Yani end se 3 items print karo

# full list slicing copy banane ke liye
# Puri list ko copy kar ke print karo
# matlab start kuch nhi to default 0 index and last tak chalega qk last limit nhi batayi
fruits5 = ["banana", "apple", "orange", "mango", "grapes", "melon"]
print(fruits5[:])  # ['banana', 'apple', 'orange', 'mango', 'grapes', 'melon']


# 6. skip with step  har 2nd item lo
# Yani har doosra item print karo (0, 2, 4)
#            print     skip     print     skip     print 
fruits6 = ["banana", "apple", "orange", "mango", "grapes", "melon"]
print(fruits6[::2])  # ['banana', 'orange', 'grapes']


# Reverse list using slicing
# Yani list ko ulta kar ke print karo
fruits7 = ["banana", "apple", "orange", "mango", "grapes", "melon"]
print(fruits7[::-1])  # ['melon', 'grapes', 'mango', 'orange', 'apple', 'banana']


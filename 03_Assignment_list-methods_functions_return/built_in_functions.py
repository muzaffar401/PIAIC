# built-in functions in python 

# id() function
# Ye function kisi bhi variable ki memory location (address) batata hai.
# Agar naya object banega to memory location change hogi.
# Immutable cheezon jaise string ya number ka same value ho to location same bhi ho sakti hai.
student_name = "muzaffar"
print(id(student_name))

# type() function
# ye function type batata he ke string he integer he ya boolean he etc
student_name = "muzaffar"
print(type(student_name))

# dir() function
# ye function data type ko dekh kar uske jitne methods hen wo show karta he 
print(dir("muzaffar"))

# len() function
# ye function length nikaal kar deta he or ye string me hi chalta he agar int dunga to error ayega
print(len("muzaffar"))

# or len() list me bhi work karta he total items batata he
fruits:list = ["banana", "apple", "orange", "mango"]
print(len(fruits))  # Output: 4


# isdigit() function
# ye function check karta he ke string me sirf digits (0-9) hain ya nahi
# agar haan to True dega warna False
print("12345".isdigit())  # Output: True
print("abc123".isdigit())  # Output: False

# isalpha() function
# ye check karta he ke string me sirf alphabets hain ya nahi (A-Z, a-z)
print("muzaffar".isalpha())  # Output: True
print("muzaffar123".isalpha())  # Output: False

# isalnum() function
# ye check karta he ke string me alphabets ya digits dono ho saktay hain, lekin koi symbol ya space nahi
print("abc123".isalnum())  # Output: True
print("abc 123".isalnum())  # Output: False

# islower() function
# ye check karta he ke string ke sare letters small alphabets me hain ya nahi
print("muzaffar".islower())  # Output: True
print("Muzaffar".islower())  # Output: False

# isupper() function
# ye check karta he ke string ke sare letters capital alphabets me hain ya nahi
print("MUZAFFAR".isupper())  # Output: True
print("Muzaffar".isupper())  # Output: False

# isspace() function
# ye check karta he ke string me sirf space (khaali jaga) hai ya nahi
print("   ".isspace())  # Output: True
print(" muzaffar ".isspace())  # Output: False


# isdecimal() function
# ye sirf decimal digits (0-9) ko hi accept karta he
# ye thoda strict hota he, fractions ya special digits ko false karega
print("123".isdecimal())    # Output: True
print("½".isdecimal())      # Output: False
print("٣".isdecimal())      # Output: True (Arabic digit)

# isnumeric() function
# ye sab number type ko accept karta he — digits, fractions, unicode numbers sab
# sabse flexible function he number check karne ke liye
print("123".isnumeric())    # Output: True
print("½".isnumeric())      # Output: True
print("Ⅷ".isnumeric())      # Output: True (Roman numeral)
print("muzaffar".isnumeric())  # Output: False

# Summary (easy comparison)

# isdigit()     -> Normal digits (0-9) = True, baqi sab = False
# isdecimal()   -> Sirf decimal digits (0-9), aur bhi strict
# isnumeric()   -> Digits + unicode numbers + fractions = True





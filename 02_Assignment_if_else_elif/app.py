# Grading system using if else elif using python 

percentage = int(input("Enter Your Percentage % :"))

# using nested if else  
if percentage >= 0 and percentage <= 100: # yahan dono condition true honi chiye due to and operator
    if percentage >= 90: # 90 se bara or barabar ho to A1 grade
        print("A1 Grade")
    elif percentage >= 80: # 80 se bara or barabar ho to A grade
        print("A Grade")
    elif percentage >= 70: # 70 se bara or barabar ho to B grade
        print("B Grade")
    elif percentage >= 60: # 60 se bara or barabar ho to C grade
        print("C Grade")
    elif percentage >= 50: # 50 se bara or barabar ho to D grade
        print("D Grade")
    else:
        print("F Grade (FAIL)") # 50 se kam ho to Fail hojaye
else:
    print(f"{percentage}% is invalid percentage") # agar percentage 0 se choti or 100 se bary ho to invalid hojaye


# Age checker Program using if else elif

age = int(input("Enter Your Age :"))

if age >= 0 and age <= 100:
    if age <= 13:
        print("you are a child")
    elif age <= 20:
        print("you are a teenager")
    elif age <= 60:
        print("you are an adult")
    elif age <= 100:
        print("you are a senior citizen")
else:
    print(f"Invalid Age {age} :(")
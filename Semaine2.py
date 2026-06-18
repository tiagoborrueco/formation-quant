name = "Tiago"
age = "19"

print(f"My name is {name} and I am {age} years old")
#f-string is a way to format strings in Python. It allows you to embed expressions inside string literals, using curly braces {}. In this case, the variables name and age are being inserted into the string.


# =======================================

age_str = "19"
age_int = 19

print(age_str + age_str) #1919
print(age_int + age_int) #38


# ========================================

if age_int >= 18:
    print("You are an adult")
else:
    print("You are a minor")

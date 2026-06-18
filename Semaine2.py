# ========================================
# =========Variables et f-string==========
# ========================================

name = "Tiago"
age = "19"

print(f"My name is {name} and I am {age} years old")
#f-string is a way to format strings in Python. It allows you to embed expressions inside string literals, using curly braces {}. In this case, the variables name and age are being inserted into the string.


# ========================================
# ===========Int et String================
# ========================================

age_str = "19"
age_int = 19

print(age_str + age_str) #1919
print(age_int + age_int) #38


# ========================================
# ===========Condtions====================
# ========================================
if age_int >= 18:
    print("You are an adult")
else:
    print("You are a minor")


# ========================================
# =============Boucles====================
# ========================================

rendement = [0.2, -0.3, -0.04, 0.1, 0.5, -0.2, 0]

for r in rendement:
    if r < 0:
        print(f"le rendement est négatif: {r}")
    elif r > 0:
        print(f"Le rendement est positif: {r}")
    else:
        print(f"Le rendement est nul: {r}")

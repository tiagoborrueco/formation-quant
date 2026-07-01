def is_armstrong_number(number):
    number2 = str(number)
    amstrong = 0
    for chiffre in number2:
        amstrong = amstrong + int(chiffre)**len(number2)
    return amstrong == number

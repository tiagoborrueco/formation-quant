def line_up(name, number):
    analyse = number + 100
    analyse2 = number + 10
    if analyse2 % 10 == 1 and analyse % 100 != 11:
        particule = "st"
    elif analyse2 % 10 == 2 and analyse % 100 != 12:
        particule = "nd"
    elif analyse2 % 10 == 3 and analyse % 100 != 13:
        particule = "rd"
    else:
        particule = "th"

    phrase = f"{name}, you are the {number}{particule} customer we serve today. Thank you!"


    return phrase

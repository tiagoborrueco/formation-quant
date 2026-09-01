def square_root(number):
    guess = 1
    while guess**2 != number:
        guess = (1/2)*(guess + number/guess)
    return guess

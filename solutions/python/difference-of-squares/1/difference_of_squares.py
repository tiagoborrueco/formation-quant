def square_of_sum(number):
    result = (number*(number +1) / 2)**2
    return result

def sum_of_squares(number):
    n = 0
    u = 0
    while n < number + 1:
        u = u + n**2
        n = n + 1
    return u

def difference_of_squares(number):
    diff = square_of_sum(number) - sum_of_squares(number)
    return diff

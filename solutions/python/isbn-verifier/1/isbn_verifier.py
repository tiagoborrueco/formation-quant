def is_valid(isbn):
    check = 0
    n = 10
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    if 'X' in isbn and not isbn.endswith('X'):
        return False

    for digit in isbn:
        if digit.isdigit():
            check = check + int(digit) * n
        elif digit == 'X':
            check = check + 10
        else:
            return False
        n = n - 1
    return check % 11 == 0











        
    
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factor = [compte for compte in range(1, number) if number % compte == 0]
    if sum(factor) < number:
        return 'deficient'
    if sum(factor) == number:
        return 'perfect'
    return 'abundant'
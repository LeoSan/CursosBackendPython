def sum(a, b):
    """
    >>> sum(5,7)
    12

    >>> sum(4, -4)
    2
    """
    return a + b

def subtract(a, b):
    """
    >>> subtract(5,7)
    12

    >>> subtract(4, -4)
    2
    """
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "NA"
    return a / b
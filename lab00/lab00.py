def twenty_twenty_one():
    """Come up with the most creative expression that evaluates to 2021,
    using only numbers and the +, *, and - operators.

    Expected result:
    >>> twenty_twenty_one()
    2021
    """
    return 2022


def sum(a, b):
    """Compute the sum of a and b.

    Expected result:
    >>> sum(1, 2)
    3
    >>> sum(3, 8)
    11
    """
    return a + b


def square_sum(a, b):
    """Compute the sum of square a and square b.

    Expected result:
    >>> square_sum(3, 4)
    25
    """
    return a*a+b*b
def absolute_value(x):
    if x>0:
        return x
    elif x==0:
        return 0
    else:
        return -x
def fib(n):
    """compute the nth """
    pred, curr = 0, 1
    k=1
    while k<n:
        pred, curr = curr, curr+pred
        k = k + 1
    return curr
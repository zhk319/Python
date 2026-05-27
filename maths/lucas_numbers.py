def lucas_number(index: int) -> int:
    """
    Returns the Lucas number at the given index using an iterative approach.
    The Lucas numbers are an integer sequence where each term is the sum of the
    two preceding terms, starting with 2 and 1.

    Reference: https://en.wikipedia.org/wiki/Lucas_number

    >>> lucas_number(0)
    2
    >>> lucas_number(1)
    1
    >>> lucas_number(5)
    11
    >>> lucas_number(10)
    123
    >>> lucas_number(-3)
    Traceback (most recent call last):
        ...
    ValueError: index must be a non-negative integer.
    """
    if index < 0:
        raise ValueError("index must be a non-negative integer.")

    if index == 0:
        return 2
    if index == 1:
        return 1

    a, b = 2, 1
    for _ in range(2, index + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    

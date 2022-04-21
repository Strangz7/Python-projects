def get_digit(number: int, position: int) -> int:
    """
    Get the digit at a particular position
    >>> get_digit(234, 0)
    4
    >>> get_digit(234, 2)
    2

    """
    return number // (10 ** position) % 10

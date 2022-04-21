def divide(a,b):
    if b == 0:
        raise ValueError("Denominator can not be zero")
    if not isinstance(a, (int, float)) or not isinstance(b,(int, float)):
        raise TypeError("At least you can see that the function is DIVIDE na")
    return int(a) / int(b)
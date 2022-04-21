from collections import Counter


def list_func(lst):
    return Counter(lst)


print((list_func([1, 1, 2, 3, 2, 2, 4, 5, 4, 5, 4, 3, 6, 2, 2])))

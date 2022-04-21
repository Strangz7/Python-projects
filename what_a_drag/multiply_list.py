def list_multiplication(lists):
    index = 1
    for list in lists:
        index *= list
    return index


print(list_multiplication([2,3,4,7]))

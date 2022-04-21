def max_list_num(lists):
    max = lists[0]
    for list in lists:
        if list > max:
            max = list
    return max


# print(max_list_num([2, 7, 4, 5]))
b = 1
for a in [2, 3, 4, 5]:
    b *= a
    print(b)

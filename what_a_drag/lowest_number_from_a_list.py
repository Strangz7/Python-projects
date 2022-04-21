def lowest_list_num(list):
    min = list[0]
    for index in list:
        if index < min:
            min = index
    return min


print(lowest_list_num([2,5,6,9]))
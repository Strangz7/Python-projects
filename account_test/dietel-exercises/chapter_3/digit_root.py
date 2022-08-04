# num = 13579
# sum1 = 0
# lst = []
# total = []
# tty = 0
# lt = 0
#

# for i in num:
#     sum += i
#
# for x in str(sum):
#     lst.append(int(x))
#
# for y in lst:
#     tty += y
#
# for z in str(tty):
#     total.append(int(z))
#
# if len(total) > 1:
#     for i in total:
#         lt += i
# else:
#     print(total)
def numbers_digit(number):
    x = sum([int(a) for a in str(number)])
    # totals = 0
    # for i in x:
    #     totals += i
    if x > 9:
        result = numbers_digit(x)
    else:
        result = x
    return result


print(numbers_digit(12345))



# while len(lst) > 1:

# print(tty)
# print(lst)
# print(lt)# print(total)

# a = int(input())
# b = int(input())
# print(a + b)
# print( a - b)
# print(a * b)

# print(a // b)
# print(a / b)

# len = [1,2,3,4]
# res = len[::-1]
# print(res)
# a = [int(input(f"Enter number {i+1}")) for i in range(4)]
# a = [4,3,2,1]
# b = []
# c = 0
# while c <= len(a) - 1:
#     b.append(a[(len(a) - 1) - c])
#     c += 1
# print(b, end='')
num = [1,3,2,1,8,9]
sum = 0
lst = []
total = 0
for i in num:
    sum += i

for x in str(sum):
    lst.append(int(x))
    # if len(lst) > 0:
    #      for i in lst:
    #         total += i
    # else:
    #     total

print(lst)


while len(lst) >0:
    for i in num:
        sum += i

    for x in str(sum):
        lst.append(int(x))




# print(str(sum))
# for i in lst:
#     print(i)

# my_list = [int(x) for x in str(lst)]
# print(my_list)
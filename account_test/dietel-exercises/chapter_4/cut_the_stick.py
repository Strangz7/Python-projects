# num = [5, 4, 4, 2, 2, 8]
# total = 0
# x = min(num)
# for i in num:
#     i -= x
#     print(i)
import math
# math.pi
num = 3
for i in range(1 , num+2):
    x = math.pi
    # print(f'{x:.{i}f}')

def pi_to_n(n):
    lst = []
    for i in range(2, n+2):
        x = math.pi
        lst.append(print(f'{x:.{i}f}'))
        # print(f'{x:.{i}f}')


pi_to_n(3)


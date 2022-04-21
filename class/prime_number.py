# import math
#
# number = int(input('Enter a number? '))
# square_root = math.sqrt(number)
# ceil = math.ceil(square_root)
#
# catNames = []
# while True:
#     name = input("Enter the name of cat (or enter nothing to stop): ")
#     if name == '':
#         break
#     catNames += [name]
# print('The cat names are: ')
# for name in catNames:
#     print(name)
# numbers = [1,2,3,4]
# for number in numbers:
#     print(number)

# numbers = []
# for i in range(1,10):
#     if i % 2 != 0:
#         numbers.append(i)
# print(numbers)

# lst = []
# for i in range (65,91):
#     lst.append(chr(i))
# print(lst)

# lst = [chr(i) for i in range(65,91)]
# print(lst)

def mult(c, fun):
    return fun(c)


def operate(x, y, mul):
    return mul(x, y)


double = operate(2, 3, lambda x, y: x * y)
# multiply = operate(5, 7, mult)
# print(multiply)
# plus = operate(1, 3, lambda x, y: x + y)
print(double)

lal = mult(4, lambda c: c ** 2)
print(lal)


def add(a, s):
    return a + s


total = add(1, 2)
print(total)


def sub(a, s):
    return a - s


subtract = sub(12, 14)
print(abs(subtract))


def multi(x, y, fun):
    return fun(x, y)


times = multi(2, 3, add)
print(times)

multiplication = multi(2, 3, lambda x, y: x * y)
print(multiplication)


def square(x, fun):
    return fun(x)


root = square(4, lambda x: x ** 2)
print(root)

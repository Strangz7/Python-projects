# DICT COMP
# dict_comp = {k: v for k, v in zip(range(7), range(7))}
# print(dict_comp)

s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}
# s1.add(7)
# print(s1)
# s1 &= s2
# print(s1)
# print(s1.pop())
# print(s1.pop())
# print(s1 | s2)
# print(s1.intersection(s2))
# print(s1 - s2)
# s1 -= s2
# print(s1)
# print(s1 ^ s2)
# s1 ^= s2
# print(s1)
# d = {'name': 'Tolani', 'age': 32}
# print(d.get("named", "Samson"))
# print(d.pop('age'))
# print(d.popitem())
# d.update ({'sex': 'male'})
# print(d)

# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
# print('Thank you!')

# total = 0
# for num in range(101):
#     total = total + num
# print(total)

# for row in range(10):
#     for column in range(10):
#         print('<' if row % 2 == 1 else '>', end='')
#     print()
# for row in range(2):
#     for column in range(7):
#         print('@',end='')
#     print()

# input("WHat is your problem: ")
# i = input("Have you had this problem before(yes\\No): ")
# if i == "yes":
#     print("Well you have it again")
# if i == "no":
#     print("Well you have it now")
# else:
#     print("That's not the question ")

e2 = [x ** 2 for x in range(7, 1, -1)]
print(e2)
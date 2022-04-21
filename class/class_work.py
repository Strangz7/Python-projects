# def fn (a = None):
#     if a is None:
#         a = []
#     a.append("Python")
#     return a
# print(fn())
#
# def add (* numbers):
#     total = 0
#     for num in numbers:
#         total+= num
#     return total
# print(add(1,2,3,4,5))


#
# def rotate(lst, k):
#     k = k % len(lst)
#     return lst[-k: ]+ lst[:-k]
#
#
# print(rotate([1,2,3,4,5], 2))


# n = int(input("Input number: "))
# if n % 2 == 0:
#     print("Not Weird")
# else:
#     print("Weird")

# print(any([True, False, False]))
# names = ["Amaka", "Segun", "comb", "Samson", "foil"]
#
# print(name.istitle() for name in names)
# print(all(name.istitle() for name in names))
#
# peoples = [
#     {"name": "Omosetan Omorele", "age": 30, "year_of_esp": 4, "language": ["Pyhton"]},
#     {"name": "Jon Doe", "age": 25, "year_of_esp": 2, "language": ["JavaScript", "C#"]},
#     {"name": "Amaka Steven", "age": 19, "year_of_esp": 5, "language": ["Python"]},
#     {"name": "Florence Segun", "age": 28, "year_of_esp": 15, "language": ["Python", "Java"]},
#     {"name": "Ernest Adeola", "age": 30, "year_of_esp": 4, "language": ["Kotlin", "Java"]}
# ]
#
# print([people["age"] <= 28 and "Python" in people["language"] for people in peoples])
# print(any([people["age"] <= 28 and "Python" in people["language"] for people in peoples]))
# print([people["name"] for people in peoples if people["age"] <= 28 and "Python" in people["language"]])
#
# # MAP
# lst = list(map(lambda x: x ** 2, range(1, 10)))
# print(lst)
#
# map_object = map(lambda x: x ** 2, range(1, 10))
# lst1 = list(map_object)
# lst2 = list(map_object)
# print("1", lst1)
# print("2", lst2)
#
# maps_object = map(lambda x: x ** 2 if x % 2 == 0 else x, range(1, 10))
# lst1 = list(maps_object)
# lst2 = list(maps_object)
# print("1", lst1)
# print("2", lst2)
#
#
# def isEven(x):
#     return x % 2 == 0
#
#
# filter_obj = filter(isEven, range(1, 10))
# print(filter_obj)
#
# from functools import reduce
# fruits = ["Apple", "Pear", "Pineaple", "Orange", "Watermelon", "Banana", "Ccumber"]
# longest = reduce(lambda x, y: x if len(x) > len(y) else y, fruits)
# print(longest)
#
# from functools import reduce
# fruits = ["Apple", "Pear", "Pineaple", "Orange", "Watermelon", "Banana", "Ccumber"]
# shortest = reduce(lambda x, y: x if len(x) < len(y) else y, fruits)
# print(shortest)
#
# print(max(fruits, key=len))
# print(sorted(fruits, key=len, reverse=False ))
# print(sorted(fruits, key=lambda x: x[-1]))


student_1 = [45, 67, 98]
student_2 = [56, 87, 52]
student_3 = [61, 43, 44]

print(list(zip(student_1, student_2, student_3, strict=True)))
s_scores = [max(subject)]
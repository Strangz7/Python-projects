# from module2 import add
# import module2
# print("Module 1", __name__)
# print(add(5,7))
# import module2 as m2
# from greeter import greet
from module2 import add as a,double as d
hello = greet("Steven")
value = a(2,2)
value1 = d(value)
print(value1)
print(hello)
# number = int(input('Enter a number? '))
#
# num = 1
# while num < number:
#     print(num)
#     num += 1
#     if num % 15 == 0:
#         print("Fizz Buzz")
#     elif num % 5 == 0:
#         print('Buzz')
#     elif num % 3 == 0:
#
#         print('fizz')
#     else:
#         print(num)


# active = True
# num = 20
# while active:
#     guess = int(input("Guess a number from 1-30: "))
#     if guess > num:
#         print("Guess too high")
#     elif guess < num:
#         print("Guess too low")
#     elif guess == num:
#         print("Correct")
#         active = False


# number = int(input("Enter number: "))
# while number != 1:
#     if number % 2 != 0:
#         number = number * 3 + 1
#         print(number)
#     if number % 2 == 0:
#         number = number // 2
#         print(number)


# for num in range(1,5):
#     print(num)

# for i in range(1,11):
#     print('*'*i)
# for i in range(11,0,-1):
#     print('*'*i)

# s = "Spam"
# ss = s[:1] + "l" + s[2:]
# print(ss)

# number = int(input("Input a number: "))
# num = 0
# while num < number:
#     no = num += 1
#     if num < number:
#         no1 = number + num
#     print(no)

# number = int(input("Input a number"))
# # num =0
# for i in list(number):
#     print(i)
#
# while num < number:
#     num += 1
#     # print(num)
# num2 = str(num)[::-1]
# print(num2)
# for i in range (number,num):
#     print(i)


# sum = 0
# for i in range(2, 22, 2):
#     sum += i
#     print(sum)

# for i in range(1, 100):
#     if i > 15:
#         break
#     else:
#         print(i)
# product = 1
# # num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num = int(input("Enter a number: "))
# for i in range(1, num+1):
#     product *= i
# print(product)


# smiley = "\U0001f605"
# for i in range(1, 21, 2):
#     print(f"{smiley * i:>20}")

# for i in(range(5, -1, -1)):
#     print(i)

# num = int(input("Enter a number: "))
# total = 1
# for i in range(num, 0, -1):
#     total *= num
#     num -=1
# print(total)

# num = int(input("Enter a number: "))
# a, b = 0, 1
# while a < num:
#     print(a)
#     a, b = b, a + b

# dialogue = "'Remember, Red, hope is a good thing, " \
#            "maybe the best of things, " \
#            "and no good things, andd no good thing ever dies '"
# for word in dialogue.split():
#     print(word)

# my = "Python Rules"
# print(my.upper().find('O'))

# a = "He had the bat"
# print(a.find('t'))
# print(a.find('t', 8))
# print(a.find('h', a.find('h') + 1 ))

# s = "This is the world of python"
# print(s.replace('o', '00',1))
# print(s)

# num = int(input("Enter a number: "))
# num1 = int(input("Enter a number: "))
# product = num1*num
# if product <= 1000:
#     print(product)
# else:
#     print(num + num1)

# str = input("Write a word: " )
# str1 =len(str)
# for i in range (0, str1-1, 2):
#     print(str[i])
# num = [10, 20, 30, 40, 10]
# num1 = [75, 65, 35, 75, 30]

# lst = ['Segun', 'sege', 'oko', 'mama', 'e']
# lst.append(['kurubente', 'kurubente', 'koga', 'ju'])
# lst.extend(['kurubente', 'kurubente', 'koga', 'ju'])
# print(lst)

# user = input("Write your name: ")
# if len(user) <3:
#     print("Name must be at least 3 characters long")
# elif len(user) > 50:
#     print("Name can be a maximum of 50 characters")
# else:
#     print("Name looks good")
# price = [5, 2, 5, 2, 2]
# for i in price:
#     for j in price:
#         print("*"*j)
#     print()
# numbers = ['1',22,23,14,16,18,]
#
# for i in numbers:
#     print(i)


def cube(x):
    result = x * x * x
    return result


num = cube(2)
print(num)
num1 = cube(3)
print(num1)


def greet(name):
    return f" Hello  {name}"


greeting = greet("steve")
print(greeting)

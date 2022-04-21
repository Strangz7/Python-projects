number = int(input("Enter a number "))
number1 = int(input("Enter a number "))
number2 = int(input("Enter a number "))

maximum = number
minimum = number1

if number1 > maximum:
    maximum = number1

if number2 > maximum:
    maximum = number2


if number < minimum:
    minimum = number

if number2 < minimum:
    minimum = number2


if number1 != maximum or number1 != minimum :
    print(number1)
if number != maximum or number != minimum:
    print(number)

if number2 != maximum or number2 != minimum:
    print(number2)

print(maximum, minimum)
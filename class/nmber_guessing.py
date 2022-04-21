guess = 20


def remainder(x, fun):
    return fun(x)


while True:
    number = int(input("Guess a number(Enter ) to exit): "))
    if number == 0:
        break
    remain = remainder(number, lambda x: abs(number - guess))
    if number > guess:
        print("Number is greater than guess you are " + remain + " close")
    if number < guess:
        print("Number is less than ")

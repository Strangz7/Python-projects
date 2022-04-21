def invest(amount, rate, years):
    # amount = 0
    # rate = 0
    # years = 0
    # i = 1
    value = 0
    for i in range(years):
        i = amount + rate
        value += i
        print(value)


print(invest(100, .05, 4))

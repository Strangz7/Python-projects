list_of_numbers = [i for i in range(30)]
while True:
    try:
        user_number = int(input('Enter number: '))
        if user_number in list_of_numbers:
            print('Number in list of numbers')
            continue
        else:
            print('Number not in list')
    except ValueError:
        print('It must be a number')

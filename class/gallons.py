counter = 0
average_mile_gallon = 0
while True:
    counter += 1
    gallons = float(input("Enter the gallons used(-1 to end): "))
    if gallons != -1:
        miles = float(input("The gallons used for each tankful: "))
        miles_gallon = miles / gallons
        average_mile_gallon += miles_gallon
        print(f"he miles/gallon for this tank was {miles_gallon}")
        continue
    print(average_mile_gallon)
    print(f'The overall average miles/gallon was {average_mile_gallon}')
    break



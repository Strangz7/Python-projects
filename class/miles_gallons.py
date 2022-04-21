miles_gallons = 00
total = 0
counter = 0
average = 0
while True:
    gallons = float(input("Enter the gallons used(-1 to end): "))
    if gallons < 0:
        break
    miles = float(input("Enter the miles driven: "))
    counter = counter + 1
    miles_gallons = miles / gallons
    print(f"The miles per gallon for this thank was: {miles_gallons}")
    total = total + miles_gallons
average = total / counter
print(f"The overall miles per gallon was: {average}")
# print(len(miles_gallons))
# print(total)
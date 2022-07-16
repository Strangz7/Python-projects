number = int(input("Enter a number "))
num = 1
# number +=1
for i in range(1, number +1):
    num *= i

# fac = [num * i for i in range(1, number)]
print(num)
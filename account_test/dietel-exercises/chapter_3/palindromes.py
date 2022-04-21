numbers = input("Enter numbers ")
# num = [numbers]
# str =""
# for number in numbers :
#     str = number + str
# if str == numbers:
#     print(f"{numbers} is a palindrome")
# else:
#     print(f"{numbers}not a palindrome" )

if numbers == numbers[::-1]:
    print(f"{numbers} is a palindrome")
else:
    print(f"{numbers} not a palindrome")

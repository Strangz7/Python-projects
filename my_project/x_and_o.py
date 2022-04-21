first_row = [" ", " ", " "]
second_row = ["   ", " ", " "]
third_row = [" ", " ", " "]
print(first_row, '\n', second_row, '\n', third_row)
# while True:
valid_input = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

while True:
    if "o" == first_row[0] and "o" == first_row[1] and "o" == first_row[2]:
        print("o win")
        break
    elif "o" == first_row[0] and "o" == second_row[1] and "o" == third_row[2]:
        print("o win")
        break
    elif "o" == first_row[1] and "o" == second_row[1] and "o" == third_row[1]:
        print("o win")
        break
    elif "o" == first_row[2] and "o" == second_row[2] and "o" == third_row[2]:
        print("o win")
        break
    elif "o" == second_row[0] and "o" == second_row[1] and "o" == second_row[2]:
        print("o win")
        break
    elif "o" == third_row[0] and "o" == third_row[1] and "o" == third_row[2]:
        print("o win")
        break
    user_input = input("Enter 1 to 9: ")
    if user_input in valid_input:
        if user_input == "1":
            if "x" in first_row[0] or "o" in first_row[0]:
                print("Invalid input")
            else:
                first_row[0] = "x"
                print(first_row, '\n', second_row, '\n', third_row)
        elif user_input == "2":
            if "x" in first_row[1] or "o" in first_row[1]:
                print("Invalid input")
            else:
                first_row[1] = "x"
                print(first_row, '\n', second_row, '\n', third_row)
        elif user_input == "3":
            if "x" in first_row[2] or "o" in first_row[2]:
                print("Invalid input")
            else:
                first_row[2] = "x"
                print(first_row, '\n', second_row, '\n', third_row)
        elif user_input == "4":
            if "x" in second_row[0] or "o" in second_row[0]:
                print("Invalid input")
            else:
                second_row[0] = "x"
                print(first_row, '\n', second_row, '\n', third_row)
        elif user_input == "5":
            if "x" in second_row[1] or "o" in second_row[1]:
                print("Invalid input")
            else:
                second_row[1] = "x"
                print(first_row, '\n', second_row, '\n', third_row)
        elif user_input == "6":
            if "x" in second_row[2] or "o" in second_row[2]:
                print("Invalid input")
            else:
                second_row[2] = "x"
                print(first_row, '\n', second_row, '\n', third_row)
        elif user_input == "7":
            if "x" in third_row[0] or "o" in third_row[0]:
                print("Invalid input")
            else:
                third_row[0] = "x"
                print(first_row, '\n', second_row, '\n', third_row)
        elif user_input == "8":
            if "x" in third_row[1] or "o" in third_row[1]:
                print("Invalid input")
            else:
                third_row[1] = "x"
                print(first_row, '\n', second_row, '\n', third_row)
        elif user_input == "9":
            if "x" in third_row[2] or "o" in third_row[2]:
                print("Invalid input")
            else:
                third_row[2] = "x"
                print(first_row, '\n', second_row, '\n', third_row)
        else:
            print('Invalid input ')
    if "x" == first_row[0] and "x" == first_row[1] and "x" == first_row[2]:
        print("x win")
        break
    elif "x" == first_row[0] and "x" == second_row[1] and "x" == third_row[2]:
        print("x win")
        break
    elif "x" == first_row[1] and "x" == second_row[1] and "x" == third_row[1]:
        print("x win")
        break
    elif "x" == first_row[2] and "x" == second_row[2] and "x" == third_row[2]:
        print("x win")
        break
    elif "x" == second_row[0] and "x" == second_row[1] and "x" == second_row[2]:
        print("x win")
        break
    elif "x" == third_row[0] and "x" == third_row[1] and "x" == third_row[2]:
        print("x win")
        break
    user_input2 = input("enter 1 to 9: ")
    if user_input2 in valid_input:
        if user_input2 == "1":
            if "x" in first_row[0] or "o" in first_row[0]:
                print("Invalid input")
            else:
                first_row[0] = "o"
                print(first_row, '\n', second_row, '\n', third_row)
        if user_input2 == "2":
            if "x" in first_row[1] or "o" in first_row[1]:
                print("Invalid input")
            else:
                first_row[1] = "o"
                print(first_row, '\n', second_row, '\n', third_row)
        if user_input2 == "3":
            if "x" in first_row[2] or "o" in first_row[2]:
                print("Invalid input")
            else:
                first_row[2] = "o"
                print(first_row, '\n', second_row, '\n', third_row)
        if user_input2 == "4":
            if "x" in second_row[0] or "o" in second_row[0]:
                print("Invalid input")
            else:
                second_row[0] = "o"
                print(first_row, '\n', second_row, '\n', third_row)
        elif user_input2 == "5":
            if "x" in second_row[1] or "o" in second_row[1]:
                print("Invalid input")
            else:
                second_row[1] = "o"
                print(first_row, '\n', second_row, '\n', third_row)
        elif user_input2 == "6":
            if "x" in second_row[2] or "o" in second_row[2]:
                print("Invalid input")
            else:
                second_row[2] = "o"
                print(first_row, '\n', second_row, '\n', third_row)
        elif user_input2 == "7":
            if "x" in third_row[0] or "o" in third_row[0]:
                print("Invalid input")
            else:
                third_row[0] = "o"
                print(first_row, '\n', second_row, '\n', third_row)
        elif user_input2 == "8":
            if "x" in third_row[1] or "o" in third_row[1]:
                print("Invalid input")
            else:
                third_row[1] = "o"
                print(first_row, '\n', second_row, '\n', third_row)
        elif user_input2 == "9":
            if "x" in third_row[2] or "o" in third_row[2]:
                print("Invalid input")
            else:
                third_row[2] = "o"
                print(first_row, '\n', second_row, '\n', third_row)
    else:
        print('Invalid input')

first_row = [" < >", "< >", "< >"]
second_row = ["< >", "< >", "< >"]
third_row = ["< >", "< >", "< >"]
print(first_row, "\n", second_row, "\n", third_row)
while True:
    valid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while True:
        if first_row[0] == "o" and first_row[1] == "o" and first_row[2] == "o4":
            print("o win")
        userinput = input("input 1 to 9: ")
        if userinput == "1":
            if "x" in first_row[0] or "o" in first_row[0]:
                print("input somewhere")
            else:
                first_row[0] = "x"
                print(first_row, "\n", second_row, "\n", third_row)
        elif userinput == "2":
            if "x" in first_row[1] or "o" in first_row[1]:
                print("input somewhere")
            else:
                first_row[1] = "x"
                print(first_row, "\n", second_row, "\n", third_row)
        elif userinput == "3":
            if "x" in first_row[2] or "o" in first_row[2]:
                print("input somewhere")
            else:
                first_row[2] = "x"
                print(first_row, "\n", second_row, "\n", third_row)
        elif userinput == "4":
            if "x" in second_row[0] or "o" in second_row[0]:
                print("input somewhere")
            else:
                second_row[0] = "x"
                print(first_row, "\n", second_row, "\n", third_row)
        elif userinput == "5":
            if "x" in second_row[1] or "o" in second_row[1]:
                print("input somewhere")
            else:
                second_row[1] = "x"
                print(first_row, "\n", second_row, "\n", third_row)
        elif userinput == "6":
            if "x" in second_row[2] or "o" in second_row[2]:
                print("input somewhere")
            else:
                second_row[2] = "x"
                print(first_row, "\n", second_row, "\n", third_row)
        elif userinput == "7":
            if "x" in third_row[0] or "o" in third_row[0]:
                print("input somewhere")
            else:
                third_row[0] = "x"
                print(first_row, "\n", second_row, "\n", third_row)
        elif userinput == "8":
            if "x" in third_row[1] or "o" in third_row[1]:
                print("input somewhere")
            else:
                third_row[1] = "x"
                print(first_row, "\n", second_row, "\n", third_row)
        elif userinput == "9":
            if "x" in third_row[2] or "o" in third_row[2]:
                print("input somewhere")
            else:
                third_row[2] = "x"
                print(first_row, "\n", second_row, "\n", third_row)
        if first_row[0] == "x" and first_row[1] == "x" and first_row[2] == "x":
            print("x win")
        elif first_row[0] == "o" and first_row[1] == "o" and first_row[2] == "o4":
            print("o win")
        userinput = input("input 1 to 9: ")
        if userinput == "1":
            if "x" in first_row[0] or "o" in first_row[0]:
                print("input somewhere")
            else:
                first_row[0] = "o"
                print(first_row, "\n", second_row, "\n", third_row)
        elif userinput == "2":
            if "x" in first_row[1] or "o" in first_row[1]:
                print("input somewhere")
            else:
                first_row[1] = "o"
                print(first_row, "\n", second_row, "\n", third_row)
        elif userinput == "3":
            if "x" in first_row[2] or "o" in first_row[2]:
                print("input somewhere")
            else:
                first_row[2] = "o"
                print(first_row, "\n", second_row, "\n", third_row)
        elif userinput == "4":
            if "x" in second_row[0] or "o" in second_row[0]:
                print("input somewhere")
            else:
                second_row[0] = "o"
                print(first_row, "\n", second_row, "\n", third_row)
        elif userinput == "5":
            if "x" in second_row[1] or "o" in second_row[1]:
                print("input somewhere")
            else:
                second_row[1] = "o"
                print(first_row, "\n", second_row, "\n", third_row)
        elif userinput == "6":
            if "x" in second_row[2] or "o" in second_row[2]:
                print("input somewhere")
            else:
                second_row[2] = "o"
                print(first_row, "\n", second_row, "\n", third_row)
        elif userinput == "7":
            if "x" in third_row[0] or "o" in third_row[0]:
                print("input somewhere")
            else:
                third_row[0] = "o"
                print(first_row, "\n", second_row, "\n", third_row)
        elif userinput == "8":
            if "x" in third_row[1] or "o" in third_row[1]:
                print("input somewhere")
            else:
                third_row[1] = "o"
                print(first_row, "\n", second_row, "\n", third_row)
        elif userinput == "9":
            if "x" in third_row[2] or "o" in third_row[2]:
                print("input somewhere")
            else:
                third_row[2] = "o"
                print(first_row, "\n", second_row, "\n", third_row)
    else:
        print("input not valid")

temp_file = open("temp.txt", "w")
print("first line", file=temp_file)
print("second line", file=temp_file)
# print(temp_file.readline())
temp_file.close()

temp_file = open("temp.txt", mode='r')
for line in temp_file.readline():
    for word in line.split(" "):
        print(word)

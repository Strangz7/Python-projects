import random

alphabet = ["a", "s", "d", "f", "g", "h", "j", "k", "l", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "z", "x",
            "c", "v", "b", "n", "m"]
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "*", "(", ")", "<", ">", "?", "/", "+", "_", "-", "|", "~", "^"]

alphabet_len = int(input("Length of alphabets? "))
num_len = int(input("Length of nos?"))
symbols_len = int(input("Length of symbols?"))

# password = []

# for alpha in range(alphabet_len):
#     password.append(random.choice(alphabet))
password = [random.choice(alphabet) for alpha in range(alphabet_len)]
password = [random.choice(num) for number in range(num_len)]
password = [random.choice(symbols) for symbol in range(symbols_len)]
for number in range(num_len):
    password.append(random.choice(num))

for symbol in range(symbols_len):
    password.append(random.choice(symbols))

random.shuffle(password)
for i in password:
    print(i, end=" ")



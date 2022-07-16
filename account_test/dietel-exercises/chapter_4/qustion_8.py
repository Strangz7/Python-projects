import random

base_2 = ''
for i in range(5):
    base_2 += str(random.randint(0, 1))
to_base_10 = int(base_2, base=2)
print(f'{base_2} -> {to_base_10}')
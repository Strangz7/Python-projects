sequence = [0, 1]
no1, no2 = 0, 1
for i in range(1, (50 - 1)):
    sequence.append(sequence[i - 1] + sequence[i])
print(f'Sum of first 50 Fibonacci sequence: {sum(sequence)}')

k = 4
a = [1, 2, 3, 4]
for i in range(k):
    j = a.pop()
    a.insert(0, j)
    print(a)

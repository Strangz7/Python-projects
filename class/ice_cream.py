m = 4
arr = [1, 4, 5, 3, 2]
total = 0
lst = []
for i in arr:
    for j in arr:
        k = i + j
        if k == m:
            lst.append(arr[i] + arr[j])
            print(k)

print(lst)

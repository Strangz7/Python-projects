arr = [1, 3, 5, 7, 9]
i = max(arr)
arr.remove(i)
s = sum(arr)
arr.append(i)
m = min(arr)
arr.remove(m)
a = sum(arr)
print(s, a)

# min = arr[0]
# small = 0
# for i in arr:
#     temp = arr[0]
#     if i > temp:
#         temp = i
#     arr.remove(temp)
#     print(sum(arr))

# for i in arr:
#     if i < min:
#         min = i
# arr.remove(temp)
# print(sum(arr))
# arr.remove(min)
# # print(temp)
# print(sum(arr))

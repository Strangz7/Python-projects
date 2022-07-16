s = "a" "b" "c" "a" "d" "e" "c" "c" "d" "c" "c" "d"
l = []
for i in s:
    i.join(s)
    if l != i:
        l.append(s)
    print(l)


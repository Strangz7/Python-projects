from datetime import datetime
d = datetime.now()
print(d.strftime("%A"))
print(d.strftime("%A %D %B %y"))

s = "Hello"
it = iter(s)
print(next(it))
print(next(it))
print(next(it))

def gen():
    count = 0
    while True:
        yield count
        count += 1


def counter(low, high, step):
    while low <= high:
        yield low
        low += step



print(list(counter(2,6)))
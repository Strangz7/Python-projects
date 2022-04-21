import pathlib


class CustomList(list):
    def __getitem__(self, index):
        if index <= 0:
            raise IndexError('Index out of bounds')

        return super().__getitem__(index - 1)

    def __setitem__(self, key, value):
        if key <= 0:
            raise IndexError("Index out of bounds")
        return super(CustomList, self).__setitem__(key - 1, value)


a = CustomList()
a.append(1)
a.append(2)
a.append(3)
print(a[2])
a[2] = 59
print(a[2])
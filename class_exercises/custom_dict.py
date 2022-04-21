class CustomDict(dict):
    def __setitem__(self, key, value):
        # for k in CustomDict:
        #     if k[key] != key:
        #         return super(CustomDict, self).__setitem__(key, value)
        #     else:
        #         raise KeyError(k, "key already exist")
        if key in self:
            raise KeyError(key, "key already exist")
        return super(CustomDict, self).__setitem__(key, value)

    def __getitem__(self, item):
        return super(CustomDict, self).__getitem__(item)


a = CustomDict()
a["ke"] = "value"
a["ke"] = "vvv"


dict_file = open("dict.txt", "w")
print(a["ke"], file=dict_file)
dict_file.close()

def setter(args):
    pass


class Person:
    count = 0

    def __init__(self, first_name, last_name, year, month, day, count):
        self.first_name = first_name
        self.last_name = last_name
        self._year = year
        self._month = month
        self._day = day
        Person.count += 1

    @setter
    def first_name(self, first_name):
        self.first_name = first_name

    @setter
    def last_name(self, last_name):
        self.last_name = last_name

    @setter
    def year(self, year):
        self._year = year

    @setter
    def month(self, month):
        self._month = month

    @setter
    def day(self, day):
        self._day = day

    @year.deleter
    def year(self):
        print("Deleting year>>>>")
        del self._year

    @month.deleter
    def month(self):
        print("Deleting month>>>")
        del self._month

    @day.deleter
    def day(self):
        print("Deleting day>>>")
        del self._day

    @property
    def first_name(self):
        return self.first_name

    @property
    def last_name(self):
        return self.last_name

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self.day

    @classmethod
    def get_id(cls):
        return cls.count

    @staticmethod
    def get_age(self):
        return 2022 - self._yea

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @last_name.setter
    def last_name(self, value):
        self._last_name = value
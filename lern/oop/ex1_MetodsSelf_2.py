import sys

# программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы

    def insert(self, data):
        for temp in data:
            self.lst_data.insert(len(self.lst_data), dict(zip(self.FIELDS, temp.split())))

    def select(self, a, b):
        return self.lst_data[a:b+1]


db = DataBase()
db.insert(lst_in)
print(db.lst_data)
print(db.select(1, 2))


# d = '1 Сергей 35 120000'
# z = DataBase()
# z.insert(d)
# print(z.lst_data)

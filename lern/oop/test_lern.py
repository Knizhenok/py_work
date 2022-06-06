import sys


# здесь объявляется класс StreamData
class StreamData:

    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        else:
            self.__dict__ = dict(zip(fields, lst_values))
            return self.__dict__


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


class String:
    is_empty = False


s1 = String()
s2 = String()

s2.is_empty = True

print(s2.is_empty)
print(String.is_empty)



sr = StreamReader()
data, result = sr.readlines()

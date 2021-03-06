import sys


class ListObject:
    # const = 0

    def __init__(self, data):
        self.data = data
        self.next_obj = None
        # print(self.data)

    def link(self, val):
        end = ListObject(val)
        print(end.data)
        # self.const += 1
        n = self
        # print(f'n = {n}')

        while n.next_obj:
            n = n.next_obj
            # print(f'n.next {n}')
        n.next_obj = end

        # print(self.const)


if __name__ == '__main__':
    # lst_in = list(map(str.strip, sys.stdin.readlines()))
    lst_in = ['1. Первые шаги в ООП',
              '1.1 Как правильно проходить этот курс',
              '1.2 Концепция ООП простыми словами',
              '1.3 Классы и объекты. Атрибуты классов и объектов',
              '1.4 Методы классов. Параметр self',
              '1.5 Инициализатор init и финализатор del',
              '1.6 Магический метод new. Пример паттерна Singleton',
              '1.7 Методы класса (classmethod) и статические методы (staticmethod)']

    head_obj = ListObject(lst_in[0])
    print(head_obj.data)

    for line in lst_in[1:]:
        head_obj.link(line)

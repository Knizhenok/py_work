<<<<<<< HEAD
import sys


class ListObject:
    # const = 0

    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


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
    obj = head_obj

    for i in range(1, len(lst_in)):
        obj_new = ListObject(lst_in[i])
        obj.link(obj_new)
        obj = obj_new
=======
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def size_node(self):
        count = 0
        while self.next:
            count += count
        return count

    def __str__(self):
        return f'[{self.data}]->{self.next}'


class LinkedList:
    def __init__(self):
        self.head = None

    def size_node(self):
        count = 0
        temp_count = self.head
        while temp_count:
            count += 1
            temp_count = temp_count.next
        return count

    def __str__(self):
        return str(self.head)


if __name__ == '__main__':
    linked_list = LinkedList()
    temp = Node(1)
    linked_list.head = temp

    for i in range(2, 5):
        temp.next = Node(i)
        temp = temp.next

    print(linked_list)
    print(linked_list.size_node())
>>>>>>> 29986ae (lern 15.17)

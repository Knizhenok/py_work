class Point:
    # Описание класса посмотреть можно Point.__doc__
    "Класс для предоставления координат точек на плоскости"
    # атрибуты класса общие для всех объектов класса и объекты только ссылаются на них
    #  меняя
    color = 'red'
    circle = 2


# Point.__dict__ вывести все по классу
# type(object) выведет родительский класс


# варианты добавления и изменения атрибутов класса
Point.type_pt = 'disk'
setattr(Point, 'prop', 1)

#  считать если атрибут не существует и для избежания ошибки кроме
#  надо использовать такой запрос с подменой
getattr(Point, 'a', False)

# удаление атрибута
# del Point.type_pt
# delattr(Point, 'type_pt')

# проверка наличия атрибута в классе
hasattr(Point, 'prop')


if __name__ == '__main__':
    a = Point()
    # print(getattr(a, 'col', False))
    Point.circle += 1
    a.start_pt = (10, 5)
    a.end_pt = (100, 20)
    a.color = 'blue'
    del a.color

    # print(getattr(a, 'start_pt', False))

    if 'color' in a.__dict__.keys():
        print(True)
    else:
        print(False)

    # print(*a.__dict__.keys())



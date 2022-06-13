import random


class Point:
    color = 'red'
    circle = 2

    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


class Line:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp = (a, b)
        self.ep = (c, d)


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if isinstance(self.a, str) or isinstance(self.b, str) \
                or isinstance(self.c, str):
            return 1
        elif self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 1
        elif self.a + self.b <= self.c or \
                self.b + self.c <= self.a or \
                self.a + self.c <= self.a:
            return 2
        else:
            return 3


if __name__ == '__main__':

    pass

    #########################################
    # a, b, c = map(int, input().split())
    # print(a, b, c)
    # tr = TriangleChecker(a, b, c)
    # print(tr.is_triangle())
    #
    # otr = TriangleChecker('1', 2, 3)
    # print(otr.is_triangle())

    ##################################################################################
    # elements = []
    # temp = (Line(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)),
    #         Rect(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)),
    #         Ellipse(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)))
    # for x in range(217):
    #     elements.append(random.choice(temp))
    #
    # for x in elements:
    #     if isinstance(x, Line):
    #         x.__init__()
    #
    # print(len(elements))
    # for x in elements:
    #     print(type(x), x.__dict__)
    ##################################################################################

    ##################################################################################
    # points = []
    # for x in range(1, 2000, 2):
    #     if x == 3:
    #         points.append(Point(x, x, 'yellow'))
    #     else:
    #         points.append(Point(x, x))
    # print(len(points))
    # print(points[2].color)
    ##################################################################################

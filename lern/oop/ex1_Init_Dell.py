class Point:
    color = 'red'
    circle = 2

    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


if __name__ == '__main__':
    points = []

    for x in range(1, 2000, 2):
        if x == 3:
            points.append(Point(x, x, 'yellow'))
        else:
            points.append(Point(x, x))

    print(len(points))

    print(points[2].color)




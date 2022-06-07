class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f'Воспроизведение {self.filename}')


class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        temp_data = [x for x in self.data if self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1]]
        return [print(x, end=' ') for x in temp_data]


if __name__ == '__main__':
    # pt = Point()
    # pt.set_coords(3, 4)
    # print(pt.get_coords())
    # print(pt.__dict__)
    #
    # media1 = MediaPlayer()
    # media2 = MediaPlayer()
    # media1.open("filemedia1")
    # media2.open("filemedia2")
    #
    # media1.play()
    # media2.play()

    graph_1 = Graph()
    graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
    graph_1.draw()
    Graph.draw(graph_1)



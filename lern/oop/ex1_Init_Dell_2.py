class Graph:
    def __init__(self, data, is_show=True):
        self.data = data
        self.is_show = is_show

    def set_data(self, data):
        self.data = data

    # f'Some text {' '.join(str(i) for i in self.data)}'
    def show_table(self):
        if self.is_show:
            a = ' '.join((str(i) for i in self.data))
            return a
        else:
            print("Отображение данных закрыто")

    def show_graph(self):
        if self.is_show:
            print("Графическое отображение данных:", self.show_table())
        else:
            print("Отображение данных закрыто")

    def show_bar(self):
        if self.is_show:
            print("Столбчатая диаграмма:", self.show_table())
            self.show_table()
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show


if __name__ == '__main__':

    data_graph = list(map(int, input().split()))
    gr = Graph(data_graph)
    gr.show_bar()
    gr.set_show(False)
    gr.show_table()
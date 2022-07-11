class Translator:
    dictionary = {}

    def add(self, eng, rus):
        if eng in self.dictionary:
            self.dictionary[eng].link(rus)
        else:
            self.dictionary[eng] = [rus]

    def remove(self, eng):
        del self.dictionary[eng]

    def translate(self, eng):
        # return [print(x, end=' ') for x in self.dictionary[eng]]
        return self.dictionary[eng]


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")


tr.remove('car')

for x in tr.translate('go'):
    print(x, end=' ')



from class3 import Verifications
from tkinter import Tk


class V2(Verifications):
    def __init__(self, login, password, age):
        Verifications.__init__(self, login, password)
        self.age = age
        self.__save()

    def __save(self):
        with open('users') as r:
            for i in r:
                if f'{self.login, self.password}' + '\n' == i:
                    raise ValueError('Такой есть')
        Verifications.save(self)

    def show(self):
        return self.login, self.password

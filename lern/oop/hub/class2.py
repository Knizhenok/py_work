from class3 import Verifications
from tkinter import Tk, Button


class V2(Verifications):
    def __init__(self, login, password, age):
        super().__init__(login, password)
        self.age = age
        self.__save()

    def __save(self):
        with open('users') as r:
            for i in r:
                if f'{self.login, self.password}' + '\n' == i:
                    raise ValueError('Такой есть')
        super().save()

    def show(self):
        return self.login, self.password


class My_app(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.geometry('400x400')
        self.setUI()

    def setUI(self):
        Button(self, text='OK').pack()


x = V2('qewrweqr', 'zsdfgsdfhsdf', 56)

root = My_app()
root.mainloop()

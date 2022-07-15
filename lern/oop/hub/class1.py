class Purse:

    def __init__(self, valuta, name='Unknown'):
        if valuta not in ('USD', 'EUR'):
            raise ValueError('Такой валюты нет!')
        self.__money = 0.00
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, how_many):
        self.__money = self.__money + how_many

    def top_down_balance(self, how_many):
        if self.__money - how_many < 0:
            print('Не достаточно средств')
            raise ValueError('Не достаточно средств')
        self.__money = self.__money - how_many
        return how_many

    def info(self):
        print(self.__money)

    def __del__(self):
        print('Кошелек удален')


x = Purse('USD')
y = Purse('EUR', 'Bill')
y.top_up_balance(15)
y.info()
x.top_up_balance(y.top_down_balance(10))
x.info()
y.info()
del x


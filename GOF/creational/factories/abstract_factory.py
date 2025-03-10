from abc import ABC
from enum import Enum, auto


class Drinks(Enum):
    TEA = auto()
    COFFEE = auto()
    CHOCOLATE = auto()



class Drink(ABC):
    def consume(self):
        pass

class Tea(Drink):
    def consume(self):
        print('drinking Tea')

class Coffee(Drink):
    def consume(self):
        print('drinking Coffee')

#===================================================

class DrinkFactory(ABC):
    def prepare(self):
        pass


class TeaFactory(DrinkFactory):
    def prepare(self):
        print('Prepare Tea........')
        return Tea()

class CoffeeFactory(DrinkFactory):
    def prepare(self):
        print('Prepare Coffee.....')
        return Coffee()

class ChocolateFactory(DrinkFactory):
    def prepare(self):
        print('Prepare Chocolate.....')
        return Coffee()
#================================


class DrinkMachine():

    def __init__(self):
        self.factories=[
            (Drinks.TEA, DrinkFactory()),
            (Drinks.COFFEE, CoffeeFactory()),
            (Drinks.CHOCOLATE, ChocolateFactory),
        ]


    def make_drink(self):
        print("Chose a drink:")
        for f in self.factories:
            print(f[0].name)

        selected = int(input('Select:'))
        factory =  self.factories[selected][1]
        return factory.prepare()




drink_machine = DrinkMachine()
drink = drink_machine.make_drink()
drink.consume()


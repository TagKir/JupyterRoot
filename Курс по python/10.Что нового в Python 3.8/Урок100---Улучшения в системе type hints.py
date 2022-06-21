from typing import Literal, Final


# f = open(r'C:\file.txt', 'v')  # Способа открытия файла v не существует,но клиет ничего не замечает


# def open_file(file, mode: Literal['r', 'w']):
#    pass


# open_file(r'C:\file.txt', 'v')

pi: Final = 3.14  # Мы создали не изменяемую константу
# pi = 1.2


class Dog:

    def __init__(self) -> None:
        self.paws = 4
        self.health = 100
        self.sound = 'woof-woof'

    def bark(self):
        print(self.sound)


class SuperDog(Dog):
    def __init__(self) -> None:
        super().__init__()
        self.health = 200
        self.sound = 'super-woof'


dog = SuperDog()
print(dog.health)
dog.bark()

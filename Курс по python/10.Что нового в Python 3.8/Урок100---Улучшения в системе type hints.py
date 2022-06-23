from typing import Any, Dict, Literal, Final, TypedDict


# f = open(r'C:\file.txt', 'v')  # Способа открытия файла v не существует,но клиет ничего не замечает


# def open_file(file, mode: Literal['r', 'w']):
#    pass


# open_file(r'C:\file.txt', 'v')

pi: Final = 3.14  # Мы создали не изменяемую константу
# pi = 1.2

# @Final - так нельзя
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

person: Dict[str, str] = {'name': 'john', 'last_name': 'conrad', 'sex': 'm'}

# dict_result: Dict[str, Any] = {'word': 'hello', 'count': 5}
# dict_result['comment'] = 123
# print(dict_result['lol'])      ЗДЕСЬ НЕ БЫЛО ОШИБКИ


class WordStat(TypedDict):
    word: str
    count: int


dict_result: WordStat = {'word': 'hello', 'count': 5}
# dict_result: WordStat = {'word': 'hello'}
# print(dict_result['lol'])       А ЗДЕСЬ ТЕПЕРЬ ЕСТЬ

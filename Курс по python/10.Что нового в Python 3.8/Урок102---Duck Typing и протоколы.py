from typing import List, Protocol


class Bird:
    def fly(self):
        print('FLY WITH WINGS')  # капс


class Airplane:
    def fly(self):
        print('fly with fuel')


class Flyable(Protocol):
    def fly(self): ...


def process_flyables(flyables: List[Flyable]):
    for cur_obj in flyables:
        cur_obj.fly()


process_flyables([Bird(), Airplane()])


class Fish():
    def swim(self):
        print('fidh swim in sea')


# process_flyables([Bird(), Airplane(), Fish()])
# До создания протокола - так как python - динамический язык,при вызове будет ошибка,но интерпритатор её не отмечает
# Теперь после создания протокола - теперь мы создали класс Flyable и ошибка отмечается

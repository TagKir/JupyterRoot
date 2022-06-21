# https://habr.com/ru/company/lamoda/blog/432656/


from random import random
from typing import Any, Iterable, Optional, Tuple, Union


class Character:

    def __init__(self, armor: int, power: int):    # armor: int, power: int-Это и есть type hints
        self.armor = armor
        self.power = power
        self.health = 100

    def hit(self, damage: int):
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0


c1 = Character(10, 20)

c1.hit(20)

amount: int
# amount = None

price: Optional[int]
price = 10
price = None
# price = 'abc'

attack: Any = 1
attack = 'hi'
length: Union[int, float]
length = 1
length = 1.2
# length = 'abc'

player: Tuple[str, int] = ('Kramnik', 2750)

changes_in_rating: tuple[int, ...]
changes_in_rating = (1, 2, 3, 4, 5)
# changes_in_rating = (1, 'abc')

chess_players: dict[str, int] = {'Kramnik': 2750}


def random_stream(min_val: int, max_val: int) -> Iterable[int]:
    while True:
        yield random.randint(min_val, max_val)

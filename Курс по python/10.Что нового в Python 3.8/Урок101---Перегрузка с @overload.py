from typing import Literal, Union, overload


def parse_roman(roman):
    romans = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    result = 0
    for i, _ in enumerate(roman):
        if i + 1 < len(roman) and romans[roman[i] < romans[roman[i + 1]]]:
            result -= romans[roman[i]]
        else:
            result += romans[roman[i]]
        return result


def convert_to_roman():
    pass
#                 Здесь должна быть функция,которая из арабских цифр переводит в римские цифры


# @overload
# def add(x: str, y: str, to_arabic: Literal[True]) -> int: ...


# @overload
# def add(x: str, y: str, to_arabic: Literal[False]) -> str: ...


# def add(x: str, y: str, to_arabic: bool) -> Union[str, int]:
#    a: int
#    b: int
#   a = parse_roman(x)
#   b = parse_roman(y)
#    c = a + b

#    return c if to_arabic else convert_to_roman(c)


# result1 = add('I', 'II', False)
# III
# r = result1 / 3          ЭТО ВАЖНО!!

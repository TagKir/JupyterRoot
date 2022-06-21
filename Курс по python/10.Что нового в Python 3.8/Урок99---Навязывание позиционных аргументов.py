# x = float('2.1')
# print(x)

# help(float)


def avg(a, b, c, /):  # Этот / делает аргументы позиционными
    return (a+b+c) / 3


print(avg(1, 2, 3))
# print(avg(a=1, b=2, c=3))


def assert_equal(left, right, /, fail_message=''):
    return (left == right, fail_message)


assert_equal(1, 1)
assert_equal(1, 1, fail_message='left not equal right')

# assert_equal(left=1,right=2)


def copi(*, source, destination, overwrite=False):  # Звезда(" * ") - я НЕ могу дать аргументы без их ссылки (без a=1)
    print(f'copying {source} to {destination} with overwrite-{overwrite}')


copi(source='C:\\tmp\\files.txt', destination='C:\\tmp\\files1_copy.txt', overwrite=True)


# Также я могу
def copy(source, destination, /, *, overwrite=False):
    print(f'copying {source} to {destination} with overwrite-{overwrite}')


copy('C:\\tmp\\files.txt', 'C:\\tmp\\files1_copy.txt', overwrite=True)

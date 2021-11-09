import itertools


def value(x):
    return x > 0


lst = [5, 6, -8, -4, 2]
print(list(itertools.dropwhile(value, lst)))

lst1 = [2, 4, 5, 7, 8]
print(list(itertools.dropwhile(lambda x: x % 2 == 0, lst1)))

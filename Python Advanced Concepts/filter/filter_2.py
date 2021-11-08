values = [1, 2, 3, 4, 5, 6, 10, 11, 14]


def odd_even(num):
    return True if num % 2 == 0 else False


x = filter(odd_even, values)
print(list(x))
print()

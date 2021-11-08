# odd number program
nums = [2, 3, 4, 6, 7, 8, 9]
x = lambda n: n % 2 != 0
answer = filter(x, nums)  # Second value passed should be iterable
print(list(answer))

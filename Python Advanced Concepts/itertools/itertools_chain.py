import itertools

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9]
print(list(itertools.chain(lst1, lst2, lst3)))

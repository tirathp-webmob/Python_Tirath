import itertools
import operator

print(list(itertools.accumulate([1, 2, 3])))
print(list(itertools.accumulate([1, 2, 3, 4], operator.mul)))

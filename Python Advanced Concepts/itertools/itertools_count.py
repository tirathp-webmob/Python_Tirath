# Itertools count
import itertools

for i in itertools.count(10, 5):
    if i > 100:
        break
    else:
        print(i, end=' ')

print()
for j in itertools.count(1,10):
    if j > 100:
        break
    else:
        print(j,end=' ')
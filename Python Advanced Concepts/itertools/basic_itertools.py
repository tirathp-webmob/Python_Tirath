# Itertools cycle
import itertools

temp = 0
for i in itertools.cycle('1234'):
    if temp > 8:
        break
    else:
        print(i, ' ')
        temp += 1
print()
temp1 = 0
for j in itertools.cycle('112'):
    if temp1 > 5:
        break
    else:
        print(j, end=' ')
        temp1 += 1

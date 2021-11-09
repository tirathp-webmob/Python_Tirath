def simpleFunction():
    yield 1
    yield 2

for i in simpleFunction():
    print(i)
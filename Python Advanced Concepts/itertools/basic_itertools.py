import itertools
temp = 0
for i in itertools.cycle('1234'):
    if temp >  7:
        break
    else:
        print(i,' ')
        temp+=1
        


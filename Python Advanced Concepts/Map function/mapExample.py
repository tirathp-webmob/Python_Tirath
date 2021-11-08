# Combination of map and lambda
num1 = [2, 3, 4]
num2 = [5, 6, 7]
x = map(lambda x, y: x + y, num1, num2)
print(list(x))

string_word = ['sat','bat','cat','mat']
ans = list(map(list,string_word))
print(ans)
print()
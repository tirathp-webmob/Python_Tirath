# Try-Except
def zeroDiv(number):
    answer = number/0
    return answer

try:
    c = zeroDiv(2)
    print(c)
except ZeroDivisionError:
    print('Zero Divison Error')

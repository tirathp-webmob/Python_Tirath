# Basic calculator program using lambda function
user_input1 = int(input('Enter first number:- '))
user_input2 = int(input('Enter second number:- '))
amds = int(input('1 : Add ? 2: Division ? 3 : Multiply ? 4 : Subtract'))
add = lambda number1, number2: number1 + number2
subtract = lambda number1, number2: number1 - number2
multiply = lambda number1, number2: number1 * number2
division = lambda number1, number2: number1 / number2

if amds == 1:
    print(add(user_input1, user_input2))

elif amds == 4:
    print(subtract(user_input1, user_input2))

elif amds == 3:
    print(multiply(user_input1, user_input2))

elif amds == 2:
    print(division(user_input1, user_input2))

print()
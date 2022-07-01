import numexpr
from colorama import init
from colorama import Fore, Back, Style
init()


#2 версия калькулятора + colorma + numexpr
print(Fore.GREEN)

expr = input('Введите математическое выражение: ')
result = numexpr.evaluate(expr)

print(Fore.BLACK)
print(Back.CYAN)
print(f'Результат: {result} ')

input()

# 1я версия калькулятора + colorma используется
# print(Fore.GREEN)

# a = float(input('Введите первое число: '))
# b = float(input('Введите второе число: '))

# print(Fore.MAGENTA)

# operation = input('Какое действие произвести? (+, -, *, /) ')
# result = 0

# 2я версия условий в калькуляторе
# if operation == '+':
#     result = a + b
# elif operation == '-':
#     result = a - b
# elif operation == '*':
#     result = a * b
# elif operation == '/':
#     result = a / b
# else:
#     print('Что-то пошло не так...')


# 1я версия условий в калькуляторе
# if operation == '+':
#     print(a + b)
# elif operation == '-':
#     print(a - b)
# elif operation == '*':
#     print(a * b)
# elif operation == '/':
#     print(a / b)


# print(Fore.BLACK)
# print(Back.CYAN)
# print(f'Результат: {result} ')


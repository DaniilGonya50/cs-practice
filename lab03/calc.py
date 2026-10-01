a = float(input('Введите первое число: '))
op = input('Введите операцию: ')
b = float(input('Введите второе число: '))
print('Результат: ', end='')
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b == 0:
        print('На ноль делить нельзя')
    else:
        print(a / b)
else:
    print('Неизвестная операция')

try:
    a, b = map(int, input().split())
    print(a / b)
except ValueError:
    print('Необходимо ввести 2 числа через пробел')
except ZeroDivisionError:
    print('Второе число не может быть равно 0')

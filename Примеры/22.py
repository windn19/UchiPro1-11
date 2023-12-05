try:
    a, b = map(int, input().split())
    result = a / b
except ZeroDivisionError:
    print('Второе число не может быть равно 0')
except ValueError:
    print('Необходимо ввести 2 числа через пробел')
else:
    print(result)
finally:
    print('Конец программы')

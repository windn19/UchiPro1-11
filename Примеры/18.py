try:
    a, b = map(int, input().split())
    print(a / b)
except (ZeroDivisionError, ValueError):
    print('Ошибка при выполнении')

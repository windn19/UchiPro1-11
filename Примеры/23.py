a, b = map(int, input().split())
if b == 0:
    raise ZeroDivisionError
else:
    result = a / b
print(result)
try:
    a, b = map(int, input().split())
    result = a / b
except Exception as e:
    print(e)

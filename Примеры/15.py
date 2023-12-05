lst = input().split()
if len(lst) == 2 and lst[0].isdigit() and lst[1].isdigit():
    a = int(lst[0])
    b = int(lst[1])
    if b != 0:
        print(a / b)
else:
    print('Второе число не может быть равно 0')

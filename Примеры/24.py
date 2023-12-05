class MyError(Exception):
    pass


try:
    raise MyError('Ой, ошибка')
except MyError as e:
    print(e)
    print(e.__class__.__name__)

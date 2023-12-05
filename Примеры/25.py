class MinLengthError(Exception):
    pass


def check_password(password):
    if len(password) < 8:
        raise MinLengthError('Пароль должен быть не менее 8 символов')


password = input()
# try:
check_password(password)
# except MinLengthError as e:
#     print(e)
# else:
#     print('OK')

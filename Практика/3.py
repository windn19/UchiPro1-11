class LengthTelephoneNumberError(Exception):
    pass


class FirstTelephoneNumberCharError(Exception):
    pass


class WrongTelephoneNumberCharError(Exception):
    pass


class TelephoneNumber:
    def __init__(self, number: str):
        if len(number) in (11, 12):
            if number.startswith('+7') or number.startswith('8'):
                if number[1:].isdigit():
                    self.number = number
                else:
                    raise WrongTelephoneNumberCharError
            else:
                raise FirstTelephoneNumberCharError
        else:
            raise LengthTelephoneNumberError


try:
    eval(input())
except Exception as e:
    print(e.__class__.__name__)

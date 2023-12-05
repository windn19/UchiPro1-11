class DefaultList(list):
    def __init__(self, with_exception=True):
        super().__init__()
        self.with_exception = with_exception

    def __getitem__(self, item):
        if self.with_exception:
            return super().__getitem__(item)
        else:
            try:
                return super().__getitem__(item)
            except IndexError:
                return None


# [lst := DefaultList(with_exception=False), lst.append(1), lst.append(2), print(lst[0]), print(lst[1]), print(lst[2])]
# [lst := DefaultList(with_exception=True), lst.append(1), lst.append(2), print(lst[0]), print(lst[1])]
# [lst := DefaultList(), lst.append(1), print(lst[100])]

try:
    eval(input())
except Exception as e:
    print(e.__class__.__name__)

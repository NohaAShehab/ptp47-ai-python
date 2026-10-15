

class Test:
    __slots__ = ['a','b','c']
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

#
# t = Test(1, 2, 3)
# print(Test.__dict__)
# # del t.a


class Info:
    __slots__ = ['name','email','address']


# i = Info()
# print(i)
# print(i.name)


class SalmaComments:
    pass

c = SalmaComments()
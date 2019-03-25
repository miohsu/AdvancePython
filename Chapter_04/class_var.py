class A(object):
    a = 1000

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(1, 2)
b = A(3, 5)
print(A.a, a.a, a.x, a.y)
a.a = 2000
print(A.a, a.a, a.x, a.y)
A.a = 3000
print(A.a, a.a, a.x, a.y)

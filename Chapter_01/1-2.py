"""
    1.
    for i in lst: 这个语句背后其实用的是iter(lst)
    而这个函数的背后则是 lst.__iter__()方法

    通过内置函数（例如 len, iter, str）时不仅会调用特殊方法，通常还提供额外的优化，尤其是对于内置类

    2.
    __add__ 和 __mul__ 函数实现了 + 和 * 操作；
    这两个方法的返回值是新创建的对象，原值不动； 
    中缀运算符的基本原则是不改变操作对象，而是产出一个新值

    3.
    默认情况下自定义的对象总被认为是True，除非该类自定义类 __bool__ 或 __len__ 方法；
    如果不存在 __bool__ 方法，则 bool(lst) 会调用 lst.__len__()，若返回0 则 bool 返回 False

    4.
    增量运算符将中缀运算符变成赋值运算符
"""

from math import hypot


class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector({!r},{!r})'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        # return bool(abs(self))
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    vector = Vector(1, 2)
    print(vector)

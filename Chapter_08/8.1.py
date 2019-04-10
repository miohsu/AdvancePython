"""
    对象引用、可变对象和垃圾回收

    1.
    变量是标注，而不是盒子

    2.
    每个变量都有标识、类型和值。对象一旦创建，它的标识不会改变，可以把对象的标识理解为对象在内存中的地址；
    is 运算符比较两个对象标识，== 运算符比较两个对象的值；
    id() 函数返回对象标识的整数表示

    3.
    元组的不可变性指的是 tuple 数据结构的物理内容(即保存的引用)不可变，与引用的对象无关。

    4.
    深浅复制
    构造方法或[:]做的是浅复制(即复制了最外层容器，副本中的元素是源容器中元素的引用)

    5.
    函数的参数作为引用时
    Python 的参数传递方式是共享传参，函数内部的形参是实参的别名。
    函数可能会修改作为参数传入的可变对象，但是无法修改对象标识。
    不要使用可变类型作为参数的默认值。
"""


class HauntedBus(object):
    """
    wrong!!!!
    """

    def __init__(self, passenger=[]):
        self.passenger = passenger

    def pick(self, name):
        self.passenger.append(name)

    def drop(self, name):
        self.passenger.remove(name)


class TwlightBus(object):
    """
    Right!!!
    """
    def __init__(self, passenger=None):
        if passenger is None:
            self.passenger = []
        else:
            self.passenger = list(passenger)

    def pick(self, name):
        self.passenger.append(name)

    def drop(self, name):
        self.passenger.remove(name)

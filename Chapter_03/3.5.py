"""
    字典的变种
    1.
    collections.OrderedDict
    这个类型在添加键的时候会保持顺序，因此键的迭代次序总是一致的。
    popitem 实现的是一个栈，可以接收一个参数 last=False 变为队列

    2.
    collections.ChainMap
    该类型可以容纳数个不同的映射对象，然后在进行键查找操作时，这些对象会被当作一个整体被逐个查找

    3.
    collections.Counter


    4.
    collections.UserDict
"""

from collections import OrderedDict

init_data = {1: 'a', 2: 'b'}

od = OrderedDict()
od.update(init_data)
od[3] = 'c'
od[4] = 'd'
print(od)
print(od.popitem())
print(od.popitem())

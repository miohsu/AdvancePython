"""
    序列的修改、散列和切片
    鸭子类型：不要检查它是不是鸭子：检查它的叫声像不像鸭子，它的走路姿势像不像鸭子，等等

    1.
    协议 和 鸭子类型
    在面相对象编程中，协议是非正式的接口，只有在文档中定义，代码中不定义。
    例如，Python 的序列协议只需要实现 __len__ 和 __getitem__ 两个方法。任何类实现了这两个方法对可以称之为序列。

    2.
    对序列做散列可以通过 reduce 函数实现
    reduce 函数使用时最好提供三个参数 reduce(function, sequence, initial=None)

    3.
    zip 函数生成一个由元组构成的生成器。使用 zip 函数能轻松的并行迭代两个或更多可迭代对象，它返回的元组可以拆包成变量。
    - zip 函数返回一个生成器，按需生成元组
    - 当一个迭代对象耗尽后，它不会发出警告就停止
    - itertools.zip_longest 函数可以产出到最长的迭代对象耗尽

    4.
    all 函数: 如果所有分量的返回结果都是 True ，那么返回 True
"""

import functools

functools.reduce(lambda a, b: a ^ b, range(6))

n = 0
for i in range(6):
    n ^= i


def __eq__(self, other):
    if len(self) != len(other):
        return False
    for a, b in zip(self, other):
        if a != b:
            return False
    return True


def __eq__(self, other):
    return len(self) == len(other) and all(a == b for a, b in zip(self, other))

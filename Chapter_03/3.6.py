"""
    子类化 UserDict

    1.
    就创造自定义映射类型来说，UserDict比普通的 dict 为父类更加我方便。
    因为 dict 有时在实现某些方法时会走一些捷径，我们不得不在子类中重新这些方法

    2.
    UserDict 并不是 dict 的子类，但是 UserDict 有一个 data 属性，是 dict 的实例，data 属性作为 UserDict实际存储数据的地方
    通过 UserDict 重新实现 3.4 中的 StrKeyDict，这样可以在 __setitem__ 避免不必要的递归，也可以让 __contains__ 里的代码更简洁

    3.
    UserDict 是继承 MutableMapping，所以 StrKeyDict 里剩下的那些映射类型的方法都是从 UserDict、MutableMapping、Mapping 中继承的。
    MutableMapping 提供了几个实用的方法：
    MutableMapping.update: 它不但可以直接调用，而且在 __init__ 中，构造方法可以利用传入的各种参数(其他映射类型、元素是(key, value)对的可迭代对象、键值参数)来建立新值
"""

from collections import UserDict


class StrKeyDict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value

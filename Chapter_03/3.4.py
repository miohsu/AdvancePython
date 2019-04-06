"""
    映射的弹性键查询
    有时候为了方便起见，就算某个键不存在，我们也希望通过这个键值读取值的时候能得到一个默认值。
    - 通过 defaultdict 对象
    - 在 dict 类中实现 __missing__ 方法

    1.
    __missing__ 方法
    该方法只会被 __getitem__ 调用，对 get 方法和 __contains__ 方法不起作用

    2.
    当有非字符串的键被查找时，StrKeyDict0 可以把在查询时把非字符串的键转换成字符串
    在 __contains__ 方法中不能使用 key in dict 否则会出现递归调用，因此需要使用 key in dict.keys()

    3.
    Python3 中 dict.keys() 返回格式为 dict_keys 视图
    Python2 中返回格式为 list
"""

from collections import defaultdict
from collections import abc

d = {1: 1, 2: 2}
d.get(1)
res = d.keys()
pass


class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, k, default=None):
        try:
            return self[k]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

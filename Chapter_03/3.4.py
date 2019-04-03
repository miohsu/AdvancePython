"""
    映射的弹性键查询
    有时候为了方便起见，就算某个键不存在，我们也希望通过这个键值读取值的时候能得到一个默认值。
    - 通过 defaultdict 对象
    - 在 dict 类中实现 __missing__ 方法

    __missing__ 方法
    该方法只会被 __getitem__ 调用，对 get 方法和 __contains__ 方法不起作用
"""

from collections import defaultdict
from collections import abc

d = {1: 1, 2: 2}
d.get(1)

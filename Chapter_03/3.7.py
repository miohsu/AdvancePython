"""
    不可变的映射类型
    1.
    types 模块中引入了一个封装类 MappingProxyType 如果给这个类一个映射，它返回一个只读的映射视图；
    该视图是动态的，如果对源映射进行改动，该视图也会相应改动，反之不行


"""

from types import MappingProxyType

d = {1: 'a', 2: 'b'}
d_proxy = MappingProxyType(d)

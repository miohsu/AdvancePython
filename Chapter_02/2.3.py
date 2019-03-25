"""
    1.
    元组拆包可以应用到任何可迭代对象
    可以使用 * 运算符把一个可迭代对象拆开作为函数的参数
    t = (10, 8)
    divmod(*args)
    *args相当于进行了元组解包

    2.
    进行解包时如果遇到不需要的值时，可以使用占位符 '_'
    可以用 * 来处理剩下的元素，*args获取步确定数量的参数算是一种经典的写法

    3.
    在平行赋值中， * 前缀只能用在一个变量名前，但这个变量可以出现在任意位置

    4.
    collections.namedtuple 可以构建一个带名字的元组和一个有名字的类；
    namedtuple构建的类的实例所消耗的内存跟元组一样
    namedtuple有两个参数，（类名，字段名），字段名可以是可迭代对象，也可以是空格分隔的字符串
    _fields: 类方法
    _make: 类方法
    _asdict: 对象方法

    5.
    元组没有 __reversed__ 方法，但 reversed(tuple_obj) 在没有该方法时依然合法
"""

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 35.933, (35.68, 139, 69))
print(tokyo.name)
print(City._fields)
print(type(tokyo._asdict()))

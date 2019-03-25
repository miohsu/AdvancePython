"""
    1.
    列表推导式、生成器表达式、集合推导式、字典推导式在Python3中拥有自己的局部作用域

    2.
    列表推导式可以计算笛卡尔积，循环嵌套顺序与for从句的先后顺序相同

    3.
    生成器表达式遵循迭代器协议，逐个产出元素，节省内存；
    使用方法将方括号换为圆括号

    4.
    列表推导式 --> 列表
    生成器表达式 --> 迭代器
"""

lst = [1, 2, 3, 4]
new_lst = [i * 4 for i in lst if i > 2]

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
t_shirts = [(color, size) for color in colors
                          for size in sizes]

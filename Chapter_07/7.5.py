"""
    闭包
    只有设计嵌套函数时才有闭包问题
    闭包指延伸了作用域的函数，其中包含函数定义体中引用、但是不在定义体中定义的非全局变量。
    关键是他能访问定义体之外定义的非全局变量.

    1.
    只有嵌套在其他函数中的函数才需要处理不在全局作用域中的外部变量。

    2.
    nonlocal 声明
    对于数字、字符串、元组等不可变类型来说，只能读取，不能更新。如果尝试重新绑定，会隐式创建局部变量，所以需要使用 nonlocal 声明
"""


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager


def make_averager_1():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total/count
    return averager

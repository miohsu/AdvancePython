"""
    匿名函数
    lambda 函数的定义体只能使用纯表达式

    1.
    可调用对象
    除了用户定义的函数，调用运算符(即"()")还可以应用到其他对象上。如果想判断对象能否调用，可以使用内置函数 callable()
    可调用对象总结如下(7种)：
    - 用户定义的函数
    - 内置函数
    - 内置方法
    - 方法
    - 类: 调用类时会运行类的 __new__ 方法创建一个实例，然后运行 __init__ 方法，初始化实例，最后把实例返回给调用方。
    - 类的实例: 如果类定义了 __call__ 方法，那么它的实例可以作为函数调用
    - 生成器函数

    2.
    __call__ 方法
    任何 Python 对象都可以表现的像函数，只需要实现 __call__ 实例方法

    3.
    函数内省
    可以通过 dir(func) 获取 func 函数内的属性

    4.
    运算符特性
    对于增量赋值运算符(+= *=)，如果第一个参数是可变的，那么这些运算符函数就会就地修改，否则返回新值
"""
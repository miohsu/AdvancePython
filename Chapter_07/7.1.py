"""
    函数装饰器和闭包
    函数装饰器用于在源码中标记函数，以某种方式增强函数的行为

    1.
    装饰器是可调用对象，其中一个参数是另一个函数(被装饰的函数)。
    装饰器可能会处理被装饰的函数，然后把它返回，或者将其替换为另一个函数或可调用对象。

    2.
    装饰器两个特点：
    - 装饰器能把被装饰的函数替换成其他函数
    - 装饰器在模块加载时立即执行

    3.
    标准库中的装饰器 functools.lru_cache
    他把耗时的运算结果缓存起来 lru --> least recently used
    lru_cache 使用字典存储结果，而且键根据调用时传入的定位参数和关键字参数创建，所以被lru_cache 装饰的函数的所有参数必须是可散列的

    4.
    叠放装饰器
    @d1
    @d2
    def f():
        pass
    相当于 f = d1(d2(f))

    5.
    参数化装饰器
    @register()
    def func():
        pass
     -->
     func = register()(func)
"""

from functools import lru_cache


def deco(func):
    def inner(*args, **kwargs):
        print('inner')
        return func(*args, **kwargs)

    return inner


@lru_cache()
@deco
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_advance(n):
    a, b = 0, 1
    for i in range(n):
        yield b
        a, b = b, a + b


def register(active=True):
    def decorate(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
    return decorate


if __name__ == '__main__':
    gen = fibonacci_advance(10)
    print(list(gen))

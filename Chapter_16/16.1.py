"""
    协程
    协程与生成器类似，都是定义体中包含 yield 关键字的函数。在协程中，yield 通常出现在表达式的右边，可以产出值也可以不产出值。
    如果 yield 后面没有表达式则返回 None。
    协程可以从调用方接收数据，不过调用方把数据提供给协程使用的是 .send() 方法。

    1.
    yield 是一种流程控制工具，使用它可以实现协作式多任务: 协程可以把控制器让步给中心调度程序，从而激活其他协程。

    2.
    仅当协程处于暂停状态时才能调用 .send 方法，如果协程还没激活，则必须使用 next() 激活协程，或者调用 .send(None)。
    预激协程: 让协程向前执行到第一个 yield 表达式，准备号作为活动协程使用。
"""
from functools import wraps


def coroutine(func):
    """ 预激 func """

    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


if __name__ == '__main__':
    data = [10, 20, 30, 40.1]
    ave = averager()
    # next(ave)
    for i in data:
        print(ave.send(i))
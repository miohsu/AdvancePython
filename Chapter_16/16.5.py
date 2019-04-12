"""
    终止协程和异常处理

    Python2.5 之后，客户端可以在生成器对象上调用两个方法，显式地把异常发送给协程
    - throw
    - close

    generator.throw()
        致使生成器在暂停的 yield 表达式处抛出指定的异常。如果生成器处理了该异常，则生成器继续执行，产出的值可以通过调用 generator.throw 方法得到返回值。
        如果没有处理则向上冒泡。

    generator.close()
        致使生成器在暂停的 yield 表达式处抛出 GeneratorExit 异常。如果生成器没有处理这个异常，或者抛出 StopIteration 异常，调用方不会报错。
        如果收到 GeneratorExit 异常，则不能产生值，否则会报 RuntimeError 异常。

    1.
    yield from


"""

from collections import namedtuple

Result = namedtuple('Result', 'count average')


def coroutine(func):
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


@coroutine
def grouper(results, key):
    while True:
        results[key] = yield from averager()


def start(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        for value in values:
            group.send(value)
        group.send(None)
    print(results)


if __name__ == '__main__':
    data = {
        'girls;kg': [40.9, 38.5, 44.3, 45.2, 41.7, 38.0],
        'girls;m': [1.6, 1.51, 1.4, 1.3, 1.29],
        'boys;kg': [39.0, 40.2, 56.7],
    }
    start(data)

"""
    实验 Executor.map 方法

    1.
    executor.map 返回一个生成器

    2.
    executor.map 返回结果的顺序与调用开始的顺序一致。如果第一个调用生成结果的用时10秒，而其他的调用用时1秒，则阻塞10秒，获取返回 map 函数的第一个调用返回结果。

    3.
    通常的方式可能是，不管提交顺序，只要有结果就读取：因此需要使用 executor.submit 和 futures.as_completed 方法
"""

from time import sleep, strftime
from concurrent import futures


def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t' * n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t' * n, n))
    return n * 10


def main():
    display('Script starting...')
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(5))
    display('results:', results)
    display('Waiting for individual results:')
    for i, result in enumerate(results):
        display('result {}:{}'.format(i, result))


if __name__ == '__main__':
    main()

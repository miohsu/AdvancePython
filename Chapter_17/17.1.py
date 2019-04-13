"""
    使用 future 处理并发 -- Python3.2 引入的 concurrent.futures 模块

    在 IO密集型应用中不管是线程还是协程效率都比较高。

    1.
    concurrent.futures 模块主要特色是 ThreadPoolExecutor 和 ProcessPoolExecutor 类，这两个类实现的接口能分别在不同的线程或进程中执行可执行对象。
    两个类内部维护了一个工作线程池或进程池，以及要执行的任务队列。

    2.
    从 Python3.4 起标准库中有两个名为 Future 的类：
    - concurrent.futures.Future
    - asyncio.Future
    这两个类作用相同：两个 Future 类的实例都可以表示可能已经完成或尚未完成的延迟计算。

    3.
    future 的方法：
    - done: 返回一个布尔值，该方法不会阻塞
    - result: 在 future 运行结束后调用的话可以返回可调用对象的结果
    - add_down_callback: 接受一个可调用对象作为参数，future 运行结束后执行。

    4.
    as_completed 函数
    接受一个 future 列表，返回一个迭代器，在运行 future 后产出 future
"""

import os, time, sys, requests

from concurrent import futures

POP20_CC = 'CN IN US ID BR PK NG BD'.split()

BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = 'downloads/'

MAX_WORKERS = 20


def save_flags(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


# 顺序执行
# def download_many(cc_list):
#     for cc in cc_list:
#         image = get_flag(cc)
#         show(cc)
#         save_flags(image, cc.lower() + '.gif')
#
#     return len(cc_list)


# 多线程执行
def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flags(image, '{}.git'.format(cc.lower()))
    return cc


# def download_many(cc_list):
#     workers = min(MAX_WORKERS, len(cc_list))
#     with futures.ThreadPoolExecutor(workers) as executor:
#         res = executor.map(download_one, sorted(cc_list))
#     return len(cc_list)


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        to_do = []
        for cc in cc_list:
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc,future))
        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            results.append(res)
            msg = '{} result: {!r}'
            print(msg.format(future, res))
    return len(results)




def main(download_many):
    begin_time = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - begin_time
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(download_many)

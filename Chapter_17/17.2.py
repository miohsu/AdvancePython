"""
    阻塞型 IO 和 GIL
    CPython 解释器不是线程安全的，因此有全局解释器锁，一次只允许一个线程执行Python字节码。因此一个Python进程通常不能同时使用多个cpu核心
    在标准库中所有执行的阻塞型IO操作的函数，在等待操作系统返回结果时都会释放GIL。
    一个Python线程等待IO时，阻塞型IO会释放GIL，在运行另一个在线程。

    1.
    使用concurrent.futures.ProcessPoolExecutor 启动多进程;
    ProcessPoolExecutor 与 ThreadPoolExecutor 的区别在于：
        ThreadPoolExecutor 的 __init__ 函数中 max_workers 参数必选
        ProcessPoolExecutor 的 __init__ 函数中 max_workers 参数可选，默认值为 os.cpu_count() 函数返回的 CPU 的数量

    ProcessPoolExecutor 的价值体现在 CPU 密集型的作业上
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


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flags(image, '{}.git'.format(cc.lower()))
    return cc


def download_many(cc_list):
    with futures.ProcessPoolExecutor() as executor:
        to_do = []
        for cc in cc_list:
            future = executor.submit(download_one, cc)
            to_do.append(future)

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            results.append(res)
    return len(results)

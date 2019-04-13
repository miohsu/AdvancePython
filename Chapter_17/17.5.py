"""
    使用 futures.as_completed

    executor.submit 方法排定一个可调用对象的执行时间，然后返回一个 Future 实例。第一个参数是可调用的对象，其余参数是传给可调用对象的参数

    futures.as_completed 接收一个序列作为参数，返回一个迭代器，在future 运行结束后产出 future

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
    with futures.ThreadPoolExecutor(MAX_WORKERS) as executor:
        to_do = []
        for cc in cc_list:
            future = executor.submit(download_one, cc)
            to_do.append(future)

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            results.append(res)
    return len(results)

"""
    列表不是首选时
    1.
    先进先出用 deque
    contain 操作多用 set
    只包含数字的列表 array: array(typecode [, initializer])

    2.
    array 数组 Python3.4 后不再支持 sort() 就地排序，只能用 sorted

    3.
    deque 可用 append 和 pop 方法，他是基于线程安全的
"""

from collections import deque
import array
import random

dq = deque(maxlen=10)


def array_test():
    floats = array.array('d', (random.random() for i in range(10)))
    print(floats)


if __name__ == '__main__':
    # array_test()
    for i in range(20):
        dq.append(i)
    print(dq)

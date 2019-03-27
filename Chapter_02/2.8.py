"""
    bisect 模块管理已排序的序列
    1.
    bisect 模块中包含两个函数 bisect 和 insort
    两个函数都使用二分查找算法在有序序列中查找或插入元素

    2.
    bisect(lst, value) 返回value应该在的位置 index，可以通过 lst.insert(index, value) 插入
    insort 可以完成同样的事, insort = insort_right: Insert item x in list a
"""

import bisect


def bisect_test():
    lst = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
    needles = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

    # for i in needles:
    #     print(bisect.bisect(lst, i))

    for i in needles:
        bisect.insort(lst, i)

    print(lst)


def grade(score, breakpoints=[60, 70, 80, 90], grades='EDCBA'):
    index = bisect.bisect(breakpoints, score)
    return grades[index]


if __name__ == '__main__':
    result = [grade(s) for s in [33, 90, 77, 70, 89, 90, 100]]
    print(result)

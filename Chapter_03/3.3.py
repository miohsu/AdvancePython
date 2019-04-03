"""
    字典的一些方法：
    d.items() d.keys() d.values() d.clear() d.copy()
    d.pop(k, [default]): 返回 k 所对应的值，并移除这个键值对，如果没有该键则返回 None 或 default
    d.popitem(): 随机返回一个键值对，并移除之
        注意：在 OrderedDict 中，该方法会移除最先进入的元素（先进先出）；它可以接收参数 last
    d.fromkeys(it, [initial]): 将迭代器 it 里的元素设置为映射里的键，如果有 initial 参数，则设置为对应值，默认为 None
    d.get(k, [default])
    d.__missing__(k): 当 __getitem__ 找不到对应键时，调用该方法
    d.setdefault(k, [default]): 如果键 k 存在，则返回对应值，否则设定该键值对
    d.update(m, [**kwargs]): m 可以是映射或者键值对迭代器，用来更新 d 中的条目
"""


def args_test(*args, **kwargs):
    print(args, kwargs)
    values = kwargs.values()
    pass


args_test(1, 2, 3, a=1, b=2)

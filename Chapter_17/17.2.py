"""
    阻塞型 IO 和 GIL
    CPython 解释器不是线程安全的，因此有全局解释器锁，一次只允许一个线程执行Python字节码。因此一个Python进程通常不能同时使用多个cpu核心
    在标准库中所有执行的阻塞型IO操作的函数，在等待操作系统返回结果时都会释放GIL。
    一个Python线程等待IO时，阻塞型IO会释放GIL，在运行另一个在线程。

    1.
    使用concurrent.futures.ProcessPoolExecutor 启动多进程
"""
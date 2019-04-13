"""

"""

import threading


class MyThread(threading.Thread):

    def __init__(self, thread_name):
        super().__init__()
        self.thread_name = thread_name

    def run(self):
        currentThreadName = threading.currentThread()
        print('running...{}'.format(currentThreadName))


if __name__ == '__main__':
    mt = MyThread('mio')
    # mt.start()
    mt.run()
    # mt.join()

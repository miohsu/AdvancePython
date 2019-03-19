import threading, time


def say_hello(name):
    print("hello, {name}".format(name=name))
    time.sleep(2)
    print("bye, hello {name}".format(name=name))


def say_hi(name):
    print("hi, {name}".format(name=name))
    time.sleep(3)
    print("bye, hi {name}".format(name=name))


class SayHello(threading.Thread):
    def __init__(self, myname):
        super().__init__()
        self.myname = myname

    def run(self):
        print("hello, {name}".format(name=self.myname))
        time.sleep(2)
        print("bye, hello {name}".format(name=self.myname))


class SayHi(threading.Thread):
    def __init__(self, myname):
        super().__init__()
        self.myname = myname

    def run(self):
        print("hi, {name}".format(name=self.myname))
        time.sleep(3)
        print("bye, hi {name}".format(name=self.myname))


if __name__ == '__main__':
    # thread_1 = threading.Thread(target=say_hello, args=('mio',))
    # thread_2 = threading.Thread(target=say_hi, args=('los',))
    thread_1 = SayHello('miohsu')
    thread_2 = SayHi('los')

    # thread_1.setDaemon(True)
    # thread_2.setDaemon(True)

    start_time = time.time()
    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()
    end_time = time.time()

    print("Spend time: {time}".format(time=end_time - start_time))

from queue import Queue


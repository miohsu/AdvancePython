class Foo(object):
    def instance_method(self):
        print('instance method {}'.format(self.__class__))

    @staticmethod
    def static_method():
        print('static method')

    @classmethod
    def class_method(cls):
        print('class method {}'.format(cls.__name__))


# foo = Foo()
# foo.instance_method()
# Foo.class_method()
# Foo.static_method()


class Father(object):
    X = 1
    Y = 14

    @staticmethod
    def averag(*args):
        return sum(args) / len(args)

    @staticmethod
    def static_method():
        print('Father static method')
        return Father.averag(Father.X, Father.Y)

    @classmethod
    def class_method(cls):
        print('Father class method')
        return cls.averag(cls.X, cls.Y)


class Son(Father):
    X = 3
    Y = 5

    @staticmethod
    def averag(*args):
        print('Son averag method')
        return sum(args) / 3


son = Son()

print(son.averag(1, 5))
print(son.static_method())
print(son.class_method())

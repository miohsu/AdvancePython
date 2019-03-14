class A(object):
    pass


class B(object):
    pass


class C(A):
    pass


class D(B):
    pass


class E(C, D):
    pass


print(E.__mro__)

class Company(object):
    def __init__(self, employeeList):
        self.employee = employeeList

    def __len__(self):
        return len(self.employee)


com = Company(['mio', 'los'])


# print(hasattr(com,'__len__'))


class A(object):
    pass


class B(object):
    pass


from collections.abc import Sized

print(isinstance(com, Sized))

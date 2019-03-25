class Cat(object):
    def say(self):
        print('cat')


class Dog(object):
    def say(self):
        print('dog')


class Duck(object):
    def say(self):
        print('duck')


animals = [Cat, Dog, Duck]

for animal in animals:
    animal().say()

print('=' * 20)


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(['mio', 'los'])
for index in range(len(company)):
    print(company[index])

print('=' * 20)

# 自省是通过一定机制，查询到对象的内部结构
print(company.__dict__)
print(dir(company))

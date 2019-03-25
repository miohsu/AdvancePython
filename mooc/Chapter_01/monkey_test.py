class Student(object):
    def say(self):
        print('student class inner')


stu = Student()


def say_hello():
    print('student class outer')


stu.say = say_hello

stu.say()


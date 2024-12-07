# @Time    : 2024/12/5 20:48
# @Author  : dhixuan
# @File    : python_course_24.py
# @Software: PyCharm

# 方法重写
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.__age = age # 私有方法 子类虽然继承 但一般无法直接访问

    def say_hello(self):
        print("Hello, %s!" % self.name)


class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)  # 作为子类必须显示调用父类属性
        self.score = score

    def say_hello(self): # 重写say_hello
        print("Hello, my name is %s!" % self.name)


print(Student.mro())
stu = Student("Tim", 23, 97)
stu.say_hello()
print(stu._Person__age)


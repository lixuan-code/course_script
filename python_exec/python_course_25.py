# @Time    : 2024/12/5 21:17
# @Author  : dhixuan
# @File    : python_course_25.py
# @Software: PyCharm

# 多态
class Animal(object):

    def shout(self):
        print("Animal can shout!")

class Dog(Animal):
    def shout(self):
        print("Dog can shout!")

class Cat(Animal):
    def shout(self):
        print("Cat can shout!")

class Mouse(Animal):
    def shout(self):
        print("Mouse can shout!")


def animal_shout(cla):
    if isinstance(cla, Animal):
        cla.shout()

animal_shout(Dog())
animal_shout(Cat())
animal_shout(Mouse())

print(Animal.__subclasses__())


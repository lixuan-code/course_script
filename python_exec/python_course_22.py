# @Time    : 2024/12/3 23:31
# @Author  : dhixuan
# @File    : python_course_22.py
# @Software: PyCharm

class Employee:
    __company_name = 'Company'

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __work(self):
        print("%s is working" % self.name)
        print(f"{self.name}'s age is {self.__age}")
        print(f"{self.name}'s company's name is {Employee.__company_name}")


ee = Employee('Tom', 18)
print(ee._Employee__age)
ee._Employee__work()

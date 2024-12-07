# @Time    : 2024/12/3 23:49
# @Author  : dhixuan
# @File    : python_course_23.py
# @Software: PyCharm

class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_salary(self):
        print("get_salary")
        return self.__salary

    def set_salary(self, salary):
        print("set_salary")
        if 1000 < salary < 20000:
            self.__salary = salary
        else:
            print("salary error")

    @property # same as get_salary
    def salary(self):
        print("Same as get_salary")
        return self.__salary

    @salary.setter # same as set_salary
    def salary(self, salary):
        print("Same as set_salary")
        if 1000 < salary < 20000:
            self.__salary = salary
        else:
            print("salary error")

emp = Employee("zhangsan", 20000)
print(emp.get_salary())
emp.set_salary(100)
print(emp.salary)

print('*' * 20)
emp.salary = 15000
print(emp.get_salary())
print(emp.salary)

# @Time    : 2024/12/3 23:00
# @Author  : dhixuan
# @File    : python_course_20.py
# @Software: PyCharm

class Person:

    def __del__(self):
        print("del class Object:", self)

p1 = Person()
print("p1 is:",p1)
p2 = Person()
print("p2 is:",p2)

del p2

print("all script was ran!")


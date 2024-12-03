# @Time    : 2024/11/29 23:03
# @Author  : dhixuan
# @File    : python_course_18.py
# @Software: PyCharm

class GoodStudent:

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def say_score(self):
        print("{}'s score is {}".format(self.name, self.score))

stu1 = GoodStudent("Tom",18, 87)
stu1.say_score()

stu1.salary = 100
print(stu1.salary)

stu2 = GoodStudent("Jerry",32, 97)
GoodStudent.say_score(stu2)
print(dir(stu2))
print(stu2.__dict__)
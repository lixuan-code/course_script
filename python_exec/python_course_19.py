# @Time    : 2024/12/3 22:29
# @Author  : dhixuan
# @File    : python_course_19.py
# @Software: PyCharm

class GoodStudent:
    country = 'China'  # 类属性
    count = 0

    @classmethod
    def print_country(cls):
        print("my country is:", cls.country)

    @staticmethod
    def add(a,b):
        print(f"{a} + {b} = {a + b}")
        return a+b

    def __init__(self, name, age, score):  # 实例属性
        self.name = name
        self.age = age
        self.score = score
        GoodStudent.count += 1

    def say_score(self):  # 实例方法
        print("my country is:", GoodStudent.country)
        print("{}'s score is {}".format(self.name, self.score))

# 调用类方法
GoodStudent.print_country()

# 调用静态方法
gs_add = GoodStudent.add(1,5)
print(gs_add)

# 创建对象实例 调用实例方法
s1 = GoodStudent('Tom', 12, 70)
s1.say_score()

# 创建对象实例 并 print 类属性
s2 = GoodStudent('Jerry', 18, 75)
print(s2.count)

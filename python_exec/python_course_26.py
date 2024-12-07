# @Time    : 2024/12/5 21:48
# @Author  : dhixuan
# @File    : python_course_26.py
# @Software: PyCharm

# 组合
class MobilePhone:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen

class CPU:
    def calculate(self):
        print("CPU can calculate!")

class Screen:
    def show(self):
        print("Screen can show photos!")

mp = MobilePhone(CPU(), Screen())
mp.cpu.calculate()
mp.screen.show()
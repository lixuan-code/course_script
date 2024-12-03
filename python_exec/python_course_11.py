# @Time    : 2024/11/22 20:13
# @Author  : dhixuan
# @File    : python_course_11.py
# @Software: PyCharm

import math
import time

def test_global():
    start: float = time.time()
    for i in range(10000000):
        math.sqrt(i)
    end: float = time.time()
    print("all cost time in global", end - start)

def test_local():
    math_sqrt = math.sqrt
    start: float = time.time()
    for i in range(10000000):
        math_sqrt(i)
    end: float = time.time()
    print("all cost time in local", end - start)

test_global()
test_local()
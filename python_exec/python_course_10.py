# @Time    : 2024/11/22 19:42
# @Author  : dhixuan
# @File    : python_course_10.py
# @Software: PyCharm
from typing import Union


def print_max(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    if a > b:
        print(a, 'is max')
        return a
    else:
        print(b, 'is max')
        return b


print_max(30, 5)
print_max(10, 20)

# function also is object.
c = print_max
m: int = c(12, 4)
print(m * 2)

print(id(print_max))
print(id(c))

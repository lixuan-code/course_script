# @Time    : 2024/11/20 23:30
# @Author  : dhixuan
# @File    : python_course_06.py
# @Software: PyCharm

import time

start_time = time.time()
s = ''
for i in range(10000000):
    s += 'sxt'
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
lst = []
for i in range(10000000):
    lst.append('sxt')
s = ''.join(lst)
end_time = time.time()
print(end_time - start_time)

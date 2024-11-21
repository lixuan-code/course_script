# @Time    : 2024/11/21 18:51
# @Author  : dhixuan
# @File    : python_course_07.py
# @Software: PyCharm

lst = [
    ['Tom',19,30000,'USA'],
    ['Jerry',20,10000,'UK'],
    ['LiMing',18,20000,'China']
]

for m in range(3):
    for n in range(4):
        print(lst[m][n],end='\t')
    print()
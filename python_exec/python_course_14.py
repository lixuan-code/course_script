# @Time    : 2024/11/22 20:55
# @Author  : dhixuan
# @File    : python_course_14.py
# @Software: PyCharm

tup = (5,6,[7,8])

def test(n):
    print("n",id(n))
    n[2][0] = 200
    print("n",id(n))

print(tup)
print("tup",id(tup))

test(tup)

print(tup)
print("tup",id(tup))
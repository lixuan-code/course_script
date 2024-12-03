# @Time    : 2024/11/22 20:26
# @Author  : dhixuan
# @File    : python_course_12.py
# @Software: PyCharm

lst: list[int] = [10,20]

print(lst)
print("lst",id(lst))

def test(m):
    print("m",id(m))
    m.append(300)

test(lst)
print(lst)

print("*"*20)

num: int = 100

def test2(n:int) -> None:
    print("n",id(n))
    n = n + 200
    print("n",id(n))

print(num)
print("num",id(num))

test2(num)

print("num",id(num))
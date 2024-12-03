# @Time    : 2024/11/22 21:35
# @Author  : dhixuan
# @File    : python_course_15.py
# @Software: PyCharm

def test(n: int) -> None:
    print('test',n)
    if n==0:
        print("over")
    else:
        test(n-1)
    print('test---',n)


test(4)


def factorial(n: int) -> int:
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(1))
print(factorial(5))

def fibonacci(n: int) -> int:
    if n==0:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(5))
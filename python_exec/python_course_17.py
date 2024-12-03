# @Time    : 2024/11/22 22:25
# @Author  : dhixuan
# @File    : python_course_17.py
# @Software: PyCharm

globe: str = 'global'

def outer():
    global globe # define global variable, if not define, return Error when you running.
    print(globe)
    globe = 'change_global'


    non_local = 'nonlocal'
    def inner():
        nonlocal non_local # define nonlocal variable, if not define, return Error when you running.
        print(non_local)
        non_local = 'change_nonlocal'

    inner()
    print(non_local)

outer()
print(globe)
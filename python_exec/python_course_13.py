# @Time    : 2024/11/22 20:41
# @Author  : dhixuan
# @File    : python_course_13.py
# @Software: PyCharm


import  copy

def test_copy():
    lsta = [10,20,[5,6]]
    lstb = copy.copy(lsta)

    print(lsta)
    print(lstb)
    print("test copy...............")
    lstb.append(40)
    lstb[2].append(7)

    print(lsta)
    print(lstb)


def test_deepcopy():
    lsta = [10, 20, [5, 6]]
    lstb = copy.deepcopy(lsta)

    print(lsta)
    print(lstb)
    print("test deepcopy...............")
    lstb.append(40)
    lstb[2].append(7)

    print(lsta)
    print(lstb)

test_copy()
print(".........................")
test_deepcopy()
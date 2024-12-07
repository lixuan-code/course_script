# @Time    : 2024/12/3 23:12
# @Author  : dhixuan
# @File    : python_course_21.py
# @Software: PyCharm

class AccountSalary:

    def __call__(self, salary):
        print("Account Salary.")

        yearSalary = salary * 12
        monthSalary = salary
        daySalary = salary // 22.5
        hourSalary = daySalary // 8

        return dict(yearSalary=yearSalary, monthSalary=monthSalary, daySalary=daySalary, hourSalary=hourSalary)


acs = AccountSalary()
print(acs(4500))

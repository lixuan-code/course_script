# @Time    : 2024/11/7 21:40
# @Author  : dhixuan
# @File    : python_course_03.py
# @Software: PyCharm

print("I am %d years old." % 10)
print("%s is %d years old." % ('Tom', 10))

name = "Tom"
age = 12
print("%s is %d years old." % (name, age))

print("{0} is {1:.2f} years old.".format('Tom', age))

info = {"name": "Joe", "age": 18}
print("{name} is {age:.2f} years old.".format(**info))

pi = 3.1415926535897932384262
print("Pi is {:.2e}".format(pi))

print(f"{'abc':_^21}")

teacher = "Mr. Joe"
day = 3
message = (
    f"Dear {teacher},\n"
    f"I need to apply for {day} days.\n"
    f"{'Your respectfully,':>30}\n"
    f"{'Dhixuan':>30}"
)
print(message)

print("Hello","World", sep=',',end='!')
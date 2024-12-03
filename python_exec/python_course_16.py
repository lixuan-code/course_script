# @Time    : 2024/11/22 22:12
# @Author  : dhixuan
# @File    : python_course_16.py
# @Software: PyCharm

def print_name(name: str, family_name: str, is_chinese: bool) -> None:
    def inner_print(first_name,last_name):
        print(first_name,last_name)
    if is_chinese:
        inner_print(family_name,name)
    else:
        inner_print(name,family_name)

print_name('Joe', 'Beddington',False)
print_name('小红', '王',True)
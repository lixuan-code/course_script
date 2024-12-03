# @Time    : 2024/11/21 22:18
# @Author  : dhixuan
# @File    : python_course_08.py
# @Software: PyCharm

from typing import Dict, List, Union

dict_1: Dict[str, Union[str, int]] = {'name': 'Tom', 'age': 18, 'salary': 20000}
dict_2: Dict[str, Union[str, int]] = {'name': 'Lucy', 'age': 22, 'salary': 10000}
dict_3: Dict[str, Union[str, int]] = {'name': 'Jerry', 'age': 23, 'salary': 30000}

table: List[Dict] = [dict_1, dict_2, dict_3]

# get Tom's salary
print(table[0].get('salary'))

# get all people salary
for item in table:
    print(item.get('salary'))

# print all values
for item in table:
    print(item.get('name'), item.get('age'), item.get('salary'))

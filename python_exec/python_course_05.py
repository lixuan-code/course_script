# @Time    : 2024/11/20 20:23
# @Author  : dhixuan
# @File    : python_course_05.py
# @Software: PyCharm

import random

random.seed(12)
num = random.randint(1, 100)
count = 1

while count <= 5:

    guess = int(input('guess: '))

    if guess == num:
        print("恭喜中奖")
        break
    elif guess > num:
        print("大了")
    else:
        print("小了")
    count += 1
print("game over")
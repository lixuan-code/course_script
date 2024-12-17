# @Time    : 2024/12/14 23:46
# @Author  : dhixuan
# @File    : mypy01.py
# @Software: PyCharm

from tkinter import *
from tkinter import messagebox

root = Tk()

root.title('My first GUI')
root.geometry('500x309+600+250')

btn01 = Button(root)
btn01['text'] = 'Click Me'
btn01.pack()


def say_hello(event):
    messagebox.showinfo('message', 'Hello World')


btn01.bind('<Button-1>', say_hello)

root.mainloop()

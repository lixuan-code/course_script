# @Time    : 2024/12/15 00:15
# @Author  : dhixuan
# @File    : mygui01.py
# @Software: PyCharm

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.creat_widget()

    def creat_widget(self):
        self.btn01 = Button(self, text='Click me', command=self.say_hello)
        self.btn01.pack()

        self.btn_quit = Button(self, text='Quit', command=self.destroy)
        self.btn_quit.pack()

    def say_hello(event):
        messagebox.showinfo('message', 'Hello World')


if __name__ == '__main__':
    root = Tk()
    root.title('My first GUI')
    root.geometry('500x309+600+250')

    app = Application(master=root)

    app.mainloop()

import tkinter
from time import sleep


def say_hello():
    sleep(0.25)
    print('Hello')


def say_hi():
    sleep(0.01)
    print('Hi')


def say_ho():
    sleep(0.1)
    print('Ho')


def main():
    root = tkinter.Tk()
    tkinter.Button(root, text='Say Hello', command=say_hello).pack()
    tkinter.Button(root, text='Say Hi', command=say_hi).pack()
    tkinter.Button(root, text='Say Ho', command=say_ho).pack()

    root.after(1000, say_hello)
    root.mainloop()


if __name__ == "__main__":
    main()

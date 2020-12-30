from tkinter import *
import random

root = Tk()
root.geometry('600x400')
root.title('Dice Simulator')
label = Label(root, text='', font=('arial', 100))
l2 = Label(root, text='Choose Which Option You need: ', font=('calibri', 15))
l2.pack()


def select_b1():
    root1 = Toplevel(root)
    root1.title('Single Dice Simulation')

    def rolls():
        num = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
        label.config(text=f'{random.choice(num)}')
        label.pack()

    roll = Button(root1, text='Roll It Out', command=rolls)
    roll.pack()
    root1.mainloop()


def select_b2():
    root2 = Toplevel(root)
    root2.geometry('30x20')
    root2.title('Double Dice Simulation')

    def rolls():
        num = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
        label.config(text=f'{random.choice(num)} {random.choice(num)}')
        label.pack()

    roll = Button(root2, text='Roll It Out', command=rolls)
    roll.pack()
    root2.mainloop()


b1 = Button(root, text='Single Dice Simulation', font=('arial', 12), command=select_b1)
b1.pack(pady=20)
b2 = Button(root, text='Double Dice Simulation', font=('arial', 12), command=select_b2)
b2.pack(pady=20)

root.mainloop()

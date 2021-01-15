from tkinter import *

root = Tk()
textin = StringVar()
root.geometry('605x435')
root.resizable(False, False)
dark_grey = '#141414'
med_grey = '#212121'
cus_red = '#c41212'
screen = Entry(root, textvariable=textin, font=('Helvetica', 32), width=25, background=dark_grey, fg='white',
               justify=CENTER)
screen.grid(row=0, column=0, columnspan=7)
root.config(bg=dark_grey)
root.title('Calculator')
operator = ""


def clickbut(number):
    global operator
    operator = operator + str(number)
    textin.set(operator)


def equlbut():
    global operator
    add = str(eval(operator))
    textin.set(add)
    operator = ''


def equlbut():
    global operator
    sub = str(eval(operator))
    textin.set(sub)
    operator = ''


def equlbut():
    global operator
    mul = str(eval(operator))
    textin.set(mul)
    operator = ''


def equlbut():
    global operator
    div = str(eval(operator))
    textin.set(div)
    operator = ''


def button_clear():
    screen.delete(0, END)


# buttons
b1 = Button(root, text='9', font=('Helvetica', 25), padx=35, pady=15, bg=dark_grey, fg="white", relief='flat',
            command=lambda: clickbut(9))
b1.grid(row=1, column=0, sticky=W)
b2 = Button(root, text='8', font=('Helvetica', 25), padx=32, pady=15, bg=dark_grey, fg="white", relief='flat',
            command=lambda: clickbut(8))
b2.grid(row=1, column=1, sticky=E)
b3 = Button(root, text='7', font=('Helvetica', 25), padx=32, pady=15, bg=dark_grey, fg="white", relief='flat',
            command=lambda: clickbut(7))
b3.grid(row=1, column=2, sticky=E)
b4 = Button(root, font=('Helvetica', 25), text='+', padx=32, pady=15, bg=med_grey, fg="white", relief='flat',
            command=lambda: clickbut("+"))
b4.grid(row=1, column=4, sticky=E)
ac = Button(root, text='AC', font=('Helvetica', 25), padx=43, pady=62, bg=med_grey, fg='white', relief='flat',
            command=button_clear)
ac.grid(row=1, column=5, sticky=E, rowspan=2)
# -----------------------------------------------------------------------
b5 = Button(root, text='6', font=('Helvetica', 25), padx=35, pady=15, bg=dark_grey, fg="white", relief='flat',
            command=lambda: clickbut(6))
b5.grid(row=2, column=0, sticky=W)
b6 = Button(root, text='5', font=('Helvetica', 25), padx=32, pady=15, bg=dark_grey, fg="white", relief='flat',
            command=lambda: clickbut(5))
b6.grid(row=2, column=1, sticky=E)
b7 = Button(root, text='4', font=('Helvetica', 25), padx=32, pady=15, bg=dark_grey, fg="white", relief='flat',
            command=lambda: clickbut(4))
b7.grid(row=2, column=2, sticky=W)
b8 = Button(root, text='-', font=('Helvetica', 25), padx=36, pady=15, bg=med_grey, fg="white", relief='flat',
            command=lambda: clickbut("-"))
b8.grid(row=2, column=4, sticky=E)
# -----------------------------------------------------------------------
b9 = Button(root, text='3', font=('Helvetica', 25), padx=35, pady=15, bg=dark_grey, fg="white", relief='flat',
            command=lambda: clickbut(3))
b9.grid(row=3, column=0, sticky=W)
b10 = Button(root, text='2', font=('Helvetica', 25), padx=32, pady=15, bg=dark_grey, fg="white", relief='flat',
             command=lambda: clickbut(2))
b10.grid(row=3, column=1, sticky=E)
b11 = Button(root, text='1', font=('Helvetica', 25), padx=32, pady=15, bg=dark_grey, fg="white", relief='flat',
             command=lambda: clickbut(1))
b11.grid(row=3, column=2, sticky=E)
b12 = Button(root, text='*', font=('Helvetica', 25), padx=35, pady=15, bg=med_grey, fg="white", relief='flat',
             command=lambda: clickbut("*"))
b12.grid(row=3, column=4, sticky=E)
eq = Button(root, text='=', font=('Helvetica', 25), padx=56, pady=62, bg=cus_red, fg='white', relief='flat',
            command=equlbut)
eq.grid(row=3, column=5, sticky=E, rowspan=2)
# --------------------------------------------------------------------------
b13 = Button(root, text='0', font=('Helvetica', 25), padx=90, pady=15, bg=dark_grey, fg="white", relief='flat',
             command=lambda: clickbut(0))
b13.grid(row=4, column=0, sticky=W, columnspan=2)
b14 = Button(root, text='.', font=('Helvetica', 25), padx=37, pady=15, bg=dark_grey, fg="white", relief='flat')
b14.grid(row=4, column=2, sticky=E, columnspan=2)
b15 = Button(root, text='/', font=('Helvetica', 25), padx=37, pady=15, bg=med_grey, fg="white", relief='flat',
             command=lambda: clickbut("/"))
b15.grid(row=4, column=4, sticky=E)
root.mainloop()

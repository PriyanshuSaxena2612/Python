from PyDictionary import PyDictionary
from tkinter import *
from tkinter import ttk
import textwrap as tw

root = Tk()
style = ttk.Style()
root.resizable(False, False)
var = StringVar()
val = StringVar()
root.geometry('500x400')
root.config(bg='#2D2A32')
root.title('Dictionary')
l = Label(root, text='Enter the word you want to search', font=('arial', 15, 'bold'), fg='#DDD92A', bg='#2D2A32')
l.pack(pady=10)
e = Entry(root, font=('arial', 20, 'bold'), justify='center', textvariable=val)
e.pack(pady=20)
options = ['Meaning', 'Synonym', 'Antonym']


def b1():
    root1 = Toplevel(root)
    if var.get() == 'Meaning':
        Label(root1, text=tw.fill(str(PyDictionary.meaning(val.get())), width=80)).pack()
    elif var.get() == 'Synonym':
        Label(root1, text=tw.fill(str(PyDictionary.synonym(val.get())), width=80)).pack()
    else:
        Label(root1, text=tw.fill(str(PyDictionary.antonym(val.get())), width=80)).pack()
    root1.mainloop()


# Label(root, text=tw.fill(str(PyDictionary.antonym(val.get())), width=80)).pack()

box = ttk.Combobox(root, values=options, state='readonly', textvariable=var)
box.pack()
b = Button(root, text='Enter', command=b1)
b.pack(pady=20)
box.current(0)
root.mainloop()

#Author: Priyanshu Saxena
#Project Assigned On: 01-Sept-2020
#Project Completed On: 22-Sept-2020


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
import time
import mysql.connector
from forex_python.converter import CurrencyRates
import matplotlib.pyplot as plt
root = Tk()
root.geometry('622x300')
c = CurrencyRates()


def closeWindow():
    result = messagebox.askokcancel('Quit', 'Do you want to close this Window?')
    if result:
        quit()


root.protocol("WM_DELETE_WINDOW", closeWindow)
root.resizable(False, False)
root.title('Select Country')
root.iconbitmap('world.ico')


# ---------------------------Time---------------------------------------------------
def clock():
    hour = time.strftime('%H')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    t_time.config(text=hour + ':' + minute + ':' + second)
    t_time.after(1000, clock)


# ---------------------------For Showing DBMS---------------------------------------
def cun():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='2612', database='currency')
    mycursor = mydb.cursor()
    mycursor.execute('select * from currenc')
    result = mycursor.fetchall()
    for i in result:
        print(i)


# --------------------------Frame & Scrollbar--------------------------------------
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
my_scroll = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scroll.pack(side=RIGHT, fill=Y)
my_canvas.config(yscrollcommand=my_scroll.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))
second_frame = Frame(my_canvas, bg='#b5ffe1')
my_canvas.create_window((0, 0), window=second_frame, anchor='nw')


# -------------------------Commands for buttons--------------------------------------
def b1():
    root1 = Toplevel(root)
    root1.title('Conversion from INR')
    root1.iconbitmap('India_flag.ico')
    c = CurrencyRates()
    root1.resizable(False, False)
    frame = Frame(root1)
    frame.pack()
    options = ['USD', 'RON', 'JPY', 'GBP', 'EUR', 'CAD', 'CZK', 'MXN', 'NOK', 'BGN', 'ILS', 'DKK', 'HUF']
    var = StringVar()
    val = DoubleVar()
    e = Entry(frame, textvariable=val, relief='sunken', bd=8, font=('arial', 20, 'bold'), justify='center')
    e.grid(row=0, column=0)
    lbl = Label(frame, text='Enter the value in ₹', relief='raised', width=20, font=('arial', 20, 'bold'), border=5)
    lbl.grid(row=0, column=1)
    box = ttk.Combobox(frame, values=options, textvariable=var, state='readonly', width=20, font=('arial', 21, 'bold'))
    box.grid(row=1, column=1)

    def convert():
        if var.get() == 'USD':
            e.insert(0, '%.3f' % c.convert('INR', 'USD', float(e.get())))
        elif var.get() == 'RON':
            e.insert(0, '%.3f' % c.convert('INR', 'RON', float(e.get())))
        elif var.get() == 'JPY':
            e.insert(0, '%.3f' % c.convert('INR', 'JPY', float(e.get())))
        elif var.get() == 'GBP':
            e.insert(0, '%.3f' % c.convert('INR', 'GBP', float(e.get())))
        elif var.get() == 'EUR':
            e.insert(0, '%.3f' % c.convert('INR', 'EUR', float(e.get())))
        elif var.get() == 'CAD':
            e.insert(0, '%.3f' % c.convert('INR', 'CAD', float(e.get())))
        elif var.get() == 'CZK':
            e.insert(0, '%.3f' % c.convert('INR', 'CZK', float(e.get())))
        elif var.get() == 'MXN':
            e.insert(0, '%.3f' % c.convert('INR', 'MXN', float(e.get())))
        elif var.get() == 'NOK':
            e.insert(0, '%.3f' % c.convert('INR', 'NOK', float(e.get())))
        elif var.get() == 'BGN':
            e.insert(0, '%.3f' % c.convert('INR', 'BGN', float(e.get())))
        elif var.get() == 'ILS':
            e.insert(0, '%.3f' % c.convert('INR', 'ILS', float(e.get())))
        elif var.get() == 'DKK':
            e.insert(0, '%.3f' % c.convert('INR', 'DKK', float(e.get())))
        elif var.get() == 'HUF':
            e.insert(0, '%.3f' % c.convert('INR', 'HUF', float(e.get())))

    b = Button(frame, text='Convert', command=convert, font=('arial', 20, 'bold'), width=18, bd=3)
    b.grid(row=1, column=0, sticky=W)
    right = Label(frame, text='©PSP', relief='sunken', width=50)
    right.grid(row=2, column=0, sticky=EW, columnspan=2)
    # root1.protocol("WM_DELETE_WINDOW", closeWindow)
    root1.mainloop()


def b2():
    root2 = Toplevel(root)
    root2.title('Conversion from USD')
    root2.iconbitmap('dollar.ico')
    c = CurrencyRates()
    root2.resizable(False, False)
    frame = Frame(root2)
    frame.pack()
    options = ['INR', 'RON', 'JPY', 'GBP', 'EUR', 'CAD', 'CZK', 'MXN', 'NOK', 'BGN', 'ILS', 'DKK', 'HUF']
    var = StringVar()
    val = DoubleVar()
    e = Entry(frame, textvariable=val, relief='sunken', bd=8, font=('arial', 20, 'bold'), justify='center')
    e.grid(row=0, column=0)
    lbl = Label(frame, text='Enter the value in $', relief='raised', width=20, font=('arial', 20, 'bold'), border=5)
    lbl.grid(row=0, column=1)
    box = ttk.Combobox(frame, values=options, textvariable=var, state='readonly', width=20, font=('arial', 21, 'bold'))
    box.grid(row=1, column=1)

    def convert():
        if var.get() == 'INR':
            e.insert(0, '%.3f' % c.convert('USD', 'INR', float(e.get())))
        elif var.get() == 'RON':
            e.insert(0, '%.3f' % c.convert('USD', 'RON', float(e.get())))
        elif var.get() == 'JPY':
            e.insert(0, '%.3f' % c.convert('USD', 'JPY', float(e.get())))
        elif var.get() == 'GBP':
            e.insert(0, '%.3f' % c.convert('USD', 'GBP', float(e.get())))
        elif var.get() == 'EUR':
            e.insert(0, '%.3f' % c.convert('USD', 'EUR', float(e.get())))
        elif var.get() == 'CAD':
            e.insert(0, '%.3f' % c.convert('USD', 'CAD', float(e.get())))
        elif var.get() == 'CZK':
            e.insert(0, '%.3f' % c.convert('USD', 'CZK', float(e.get())))
        elif var.get() == 'MXN':
            e.insert(0, '%.3f' % c.convert('USD', 'MXN', float(e.get())))
        elif var.get() == 'NOK':
            e.insert(0, '%.3f' % c.convert('USD', 'NOK', float(e.get())))
        elif var.get() == 'BGN':
            e.insert(0, '%.3f' % c.convert('USD', 'BGN', float(e.get())))
        elif var.get() == 'ILS':
            e.insert(0, '%.3f' % c.convert('USD', 'ILS', float(e.get())))
        elif var.get() == 'DKK':
            e.insert(0, '%.3f' % c.convert('USD', 'DKK', float(e.get())))
        elif var.get() == 'HUF':
            e.insert(0, '%.3f' % c.convert('USD', 'HUF', float(e.get())))

    b = Button(frame, text='Convert', command=convert, font=('arial', 20, 'bold'), width=18, bd=3)
    b.grid(row=1, column=0, sticky=W)
    right = Label(frame, text='©PSP', relief='sunken', width=50)
    right.grid(row=2, column=0, sticky=EW, columnspan=2)
    # root2.protocol("WM_DELETE_WINDOW", closeWindow)
    root2.mainloop()


def b3():
    root3 = Toplevel(root)
    root3.title('Conversion from JPY')
    root3.iconbitmap('Japan_flag.ico')
    c = CurrencyRates()
    root3.resizable(False, False)
    frame = Frame(root3)
    frame.pack()
    options = ['INR', 'RON', 'USD', 'GBP', 'EUR', 'CAD', 'CZK', 'MXN', 'NOK', 'BGN', 'ILS', 'DKK', 'HUF']
    var = StringVar()
    val = DoubleVar()
    e = Entry(frame, textvariable=val, relief='sunken', bd=8, font=('arial', 20, 'bold'), justify='center')
    e.grid(row=0, column=0)
    lbl = Label(frame, text='Enter the value in ¥', relief='raised', width=20, font=('arial', 20, 'bold'), border=5)
    lbl.grid(row=0, column=1)
    box = ttk.Combobox(frame, values=options, textvariable=var, state='readonly', width=20, font=('arial', 21, 'bold'))
    box.grid(row=1, column=1)

    def convert():
        if var.get() == 'INR':
            e.insert(0, '%.3f' % c.convert('JPY', 'INR', float(e.get())))
        elif var.get() == 'RON':
            e.insert(0, '%.3f' % c.convert('JPY', 'RON', float(e.get())))
        elif var.get() == 'USD':
            e.insert(0, '%.3f' % c.convert('JPY', 'USD', float(e.get())))
        elif var.get() == 'GBP':
            e.insert(0, '%.3f' % c.convert('JPY', 'GBP', float(e.get())))
        elif var.get() == 'EUR':
            e.insert(0, '%.3f' % c.convert('JPY', 'EUR', float(e.get())))
        elif var.get() == 'CAD':
            e.insert(0, '%.3f' % c.convert('JPY', 'CAD', float(e.get())))
        elif var.get() == 'CZK':
            e.insert(0, '%.3f' % c.convert('JPY', 'CZK', float(e.get())))
        elif var.get() == 'MXN':
            e.insert(0, '%.3f' % c.convert('JPY', 'MXN', float(e.get())))
        elif var.get() == 'NOK':
            e.insert(0, '%.3f' % c.convert('JPY', 'NOK', float(e.get())))
        elif var.get() == 'BGN':
            e.insert(0, '%.3f' % c.convert('JPY', 'BGN', float(e.get())))
        elif var.get() == 'ILS':
            e.insert(0, '%.3f' % c.convert('JPY', 'ILS', float(e.get())))
        elif var.get() == 'DKK':
            e.insert(0, '%.3f' % c.convert('JPY', 'DKK', float(e.get())))
        elif var.get() == 'HUF':
            e.insert(0, '%.3f' % c.convert('JPY', 'HUF', float(e.get())))

    b = Button(frame, text='Convert', command=convert, font=('arial', 20, 'bold'), width=18, bd=3)
    b.grid(row=1, column=0, sticky=W)
    right = Label(frame, text='©PSP', relief='sunken', width=50)
    right.grid(row=2, column=0, sticky=EW, columnspan=2)
    # root3.protocol("WM_DELETE_WINDOW", closeWindow)
    root3.mainloop()


def b4():
    root4 = Toplevel(root)
    root4.title('Conversion from EUR')
    root4.iconbitmap('France_flag.ico')
    c = CurrencyRates()
    root4.resizable(False, False)
    frame = Frame(root4)
    frame.pack()
    options = ['INR', 'RON', 'USD', 'GBP', 'JPY', 'CAD', 'CZK', 'MXN', 'NOK', 'BGN', 'ILS', 'DKK', 'HUF']
    var = StringVar()
    val = DoubleVar()
    e = Entry(frame, textvariable=val, relief='sunken', bd=8, font=('arial', 20, 'bold'), justify='center')
    e.grid(row=0, column=0)
    lbl = Label(frame, text='Enter the value in €', relief='raised', width=20, font=('arial', 20, 'bold'), border=5)
    lbl.grid(row=0, column=1)
    box = ttk.Combobox(frame, values=options, textvariable=var, state='readonly', width=20, font=('arial', 21, 'bold'))
    box.grid(row=1, column=1)

    def convert():
        if var.get() == 'INR':
            e.insert(0, '%.3f' % c.convert('EUR', 'INR', float(e.get())))
        elif var.get() == 'RON':
            e.insert(0, '%.3f' % c.convert('EUR', 'RON', float(e.get())))
        elif var.get() == 'USD':
            e.insert(0, '%.3f' % c.convert('EUR', 'USD', float(e.get())))
        elif var.get() == 'GBP':
            e.insert(0, '%.3f' % c.convert('EUR', 'GBP', float(e.get())))
        elif var.get() == 'JPY':
            e.insert(0, '%.3f' % c.convert('EUR', 'JPY', float(e.get())))
        elif var.get() == 'CAD':
            e.insert(0, '%.3f' % c.convert('EUR', 'CAD', float(e.get())))
        elif var.get() == 'CZK':
            e.insert(0, '%.3f' % c.convert('EUR', 'CZK', float(e.get())))
        elif var.get() == 'MXN':
            e.insert(0, '%.3f' % c.convert('EUR', 'MXN', float(e.get())))
        elif var.get() == 'NOK':
            e.insert(0, '%.3f' % c.convert('EUR', 'NOK', float(e.get())))
        elif var.get() == 'BGN':
            e.insert(0, '%.3f' % c.convert('EUR', 'BGN', float(e.get())))
        elif var.get() == 'ILS':
            e.insert(0, '%.3f' % c.convert('EUR', 'ILS', float(e.get())))
        elif var.get() == 'DKK':
            e.insert(0, '%.3f' % c.convert('EUR', 'DKK', float(e.get())))
        elif var.get() == 'HUF':
            e.insert(0, '%.3f' % c.convert('EUR', 'HUF', float(e.get())))

    b = Button(frame, text='Convert', command=convert, font=('arial', 20, 'bold'), width=18, bd=3)
    b.grid(row=1, column=0, sticky=W)
    right = Label(frame, text='©PSP', relief='sunken', width=50)
    right.grid(row=2, column=0, sticky=EW, columnspan=2)
    # root4.protocol("WM_DELETE_WINDOW", closeWindow)
    root4.mainloop()


def b5():
    root5 = Toplevel(root)
    root5.title('Conversion from RON')
    root5.iconbitmap('Romania_flag.ico')
    c = CurrencyRates()
    root5.resizable(False, False)
    frame = Frame(root5)
    frame.pack()
    options = ['INR', 'JPY', 'USD', 'GBP', 'EUR', 'CAD', 'CZK', 'MXN', 'NOK', 'BGN', 'ILS', 'DKK', 'HUF']
    var = StringVar()
    val = DoubleVar()
    e = Entry(frame, textvariable=val, relief='sunken', bd=8, font=('arial', 20, 'bold'), justify='center')
    e.grid(row=0, column=0)
    lbl = Label(frame, text='Enter the value in lei', relief='raised', width=20, font=('arial', 20, 'bold'), border=5)
    lbl.grid(row=0, column=1)
    box = ttk.Combobox(frame, values=options, textvariable=var, state='readonly', width=20, font=('arial', 21, 'bold'))
    box.grid(row=1, column=1)

    def convert():
        if var.get() == 'INR':
            e.insert(0, '%.3f' % c.convert('RON', 'INR', float(e.get())))
        elif var.get() == 'USD':
            e.insert(0, '%.3f' % c.convert('RON', 'USD', float(e.get())))
        elif var.get() == 'JPY':
            e.insert(0, '%.3f' % c.convert('RON', 'JPY', float(e.get())))
        elif var.get() == 'GBP':
            e.insert(0, '%.3f' % c.convert('RON', 'GBP', float(e.get())))
        elif var.get() == 'EUR':
            e.insert(0, '%.3f' % c.convert('RON', 'EUR', float(e.get())))
        elif var.get() == 'CAD':
            e.insert(0, '%.3f' % c.convert('RON', 'CAD', float(e.get())))
        elif var.get() == 'CZK':
            e.insert(0, '%.3f' % c.convert('RON', 'CZK', float(e.get())))
        elif var.get() == 'MXN':
            e.insert(0, '%.3f' % c.convert('RON', 'MXN', float(e.get())))
        elif var.get() == 'NOK':
            e.insert(0, '%.3f' % c.convert('RON', 'NOK', float(e.get())))
        elif var.get() == 'BGN':
            e.insert(0, '%.3f' % c.convert('RON', 'BGN', float(e.get())))
        elif var.get() == 'ILS':
            e.insert(0, '%.3f' % c.convert('RON', 'ILS', float(e.get())))
        elif var.get() == 'DKK':
            e.insert(0, '%.3f' % c.convert('RON', 'DKK', float(e.get())))
        elif var.get() == 'HUF':
            e.insert(0, '%.3f' % c.convert('RON', 'HUF', float(e.get())))

    b = Button(frame, text='Convert', command=convert, font=('arial', 20, 'bold'), width=18, bd=3)
    b.grid(row=1, column=0, sticky=W)
    right = Label(frame, text='©PSP', relief='sunken', width=50)
    right.grid(row=2, column=0, sticky=EW, columnspan=2)
    # root5.protocol("WM_DELETE_WINDOW", closeWindow)
    root5.mainloop()


def b6():
    root6 = Toplevel(root)
    root6.title('Conversion from GBP')
    root6.iconbitmap('Scotland.ico')
    c = CurrencyRates()
    root6.resizable(False, False)
    frame = Frame(root6)
    frame.pack()
    options = ['INR', 'JPY', 'USD', 'RON', 'EUR', 'CAD', 'CZK', 'MXN', 'NOK', 'BGN', 'ILS', 'DKK', 'HUF']
    var = StringVar()
    val = DoubleVar()
    e = Entry(frame, textvariable=val, relief='sunken', bd=8, font=('arial', 20, 'bold'), justify='center')
    e.grid(row=0, column=0)
    lbl = Label(frame, text='Enter the value in £', relief='raised', width=20, font=('arial', 20, 'bold'), border=5)
    lbl.grid(row=0, column=1)
    box = ttk.Combobox(frame, values=options, textvariable=var, state='readonly', width=20, font=('arial', 21, 'bold'))
    box.grid(row=1, column=1)

    def convert():
        if var.get() == 'INR':
            e.insert(0, '%.3f' % c.convert('GBP', 'INR', float(e.get())))
        elif var.get() == 'USD':
            e.insert(0, '%.3f' % c.convert('GBP', 'USD', float(e.get())))
        elif var.get() == 'JPY':
            e.insert(0, '%.3f' % c.convert('GBP', 'JPY', float(e.get())))
        elif var.get() == 'GBP':
            e.insert(0, '%.3f' % c.convert('GBP', 'RON', float(e.get())))
        elif var.get() == 'EUR':
            e.insert(0, '%.3f' % c.convert('GBP', 'EUR', float(e.get())))
        elif var.get() == 'CAD':
            e.insert(0, '%.3f' % c.convert('GBP', 'CAD', float(e.get())))
        elif var.get() == 'CZK':
            e.insert(0, '%.3f' % c.convert('GBP', 'CZK', float(e.get())))
        elif var.get() == 'MXN':
            e.insert(0, '%.3f' % c.convert('GBP', 'MXN', float(e.get())))
        elif var.get() == 'NOK':
            e.insert(0, '%.3f' % c.convert('GBP', 'NOK', float(e.get())))
        elif var.get() == 'BGN':
            e.insert(0, '%.3f' % c.convert('GBP', 'BGN', float(e.get())))
        elif var.get() == 'ILS':
            e.insert(0, '%.3f' % c.convert('GBP', 'ILS', float(e.get())))
        elif var.get() == 'DKK':
            e.insert(0, '%.3f' % c.convert('GBP', 'DKK', float(e.get())))
        elif var.get() == 'HUF':
            e.insert(0, '%.3f' % c.convert('GBP', 'HUF', float(e.get())))

    b = Button(frame, text='Convert', command=convert, font=('arial', 20, 'bold'), width=18, bd=3)
    b.grid(row=1, column=0, sticky=W)
    right = Label(frame, text='©PSP', relief='sunken', width=50)
    right.grid(row=2, column=0, sticky=EW, columnspan=2)
    # root6.protocol("WM_DELETE_WINDOW", closeWindow)
    root6.mainloop()


def b7():
    root7 = Toplevel(root)
    root7.title('Conversion from CAD')
    root7.iconbitmap('Canada_flag.ico')
    c = CurrencyRates()
    root7.resizable(False, False)
    frame = Frame(root7)
    frame.pack()
    options = ['INR', 'JPY', 'USD', 'RON', 'EUR', 'GBP', 'CZK', 'MXN', 'NOK', 'BGN', 'ILS', 'DKK', 'HUF']
    var = StringVar()
    val = DoubleVar()
    e = Entry(frame, textvariable=val, relief='sunken', bd=8, font=('arial', 20, 'bold'), justify='center')
    e.grid(row=0, column=0)
    lbl = Label(frame, text='Enter the value in CA$', relief='raised', width=20, font=('arial', 20, 'bold'), border=5)
    lbl.grid(row=0, column=1)
    box = ttk.Combobox(frame, values=options, textvariable=var, state='readonly', width=20, font=('arial', 21, 'bold'))
    box.grid(row=1, column=1)

    def convert():
        if var.get() == 'INR':
            e.insert(0, '%.3f' % c.convert('CAD', 'INR', float(e.get())))
        elif var.get() == 'USD':
            e.insert(0, '%.3f' % c.convert('CAD', 'USD', float(e.get())))
        elif var.get() == 'JPY':
            e.insert(0, '%.3f' % c.convert('CAD', 'JPY', float(e.get())))
        elif var.get() == 'GBP':
            e.insert(0, '%.3f' % c.convert('CAD', 'RON', float(e.get())))
        elif var.get() == 'EUR':
            e.insert(0, '%.3f' % c.convert('CAD', 'EUR', float(e.get())))
        elif var.get() == 'CAD':
            e.insert(0, '%.3f' % c.convert('CAD', 'GBP', float(e.get())))
        elif var.get() == 'CZK':
            e.insert(0, '%.3f' % c.convert('CAD', 'CZK', float(e.get())))
        elif var.get() == 'MXN':
            e.insert(0, '%.3f' % c.convert('CAD', 'MXN', float(e.get())))
        elif var.get() == 'NOK':
            e.insert(0, '%.3f' % c.convert('CAD', 'NOK', float(e.get())))
        elif var.get() == 'BGN':
            e.insert(0, '%.3f' % c.convert('CAD', 'BGN', float(e.get())))
        elif var.get() == 'ILS':
            e.insert(0, '%.3f' % c.convert('CAD', 'ILS', float(e.get())))
        elif var.get() == 'DKK':
            e.insert(0, '%.3f' % c.convert('CAD', 'DKK', float(e.get())))
        elif var.get() == 'HUF':
            e.insert(0, '%.3f' % c.convert('CAD', 'HUF', float(e.get())))

    b = Button(frame, text='Convert', command=convert, font=('arial', 20, 'bold'), width=18, bd=3)
    b.grid(row=1, column=0, sticky=W)
    right = Label(frame, text='©PSP', relief='sunken', width=50)
    right.grid(row=2, column=0, sticky=EW, columnspan=2)
    # root7.protocol("WM_DELETE_WINDOW", closeWindow)
    root7.mainloop()


def b8():
    root8 = Toplevel(root)
    root8.title('Conversion from CZK')
    root8.iconbitmap('Czechia_flag.ico')
    c = CurrencyRates()
    root8.resizable(False, False)
    frame = Frame(root8)
    frame.pack()
    options = ['INR', 'JPY', 'USD', 'RON', 'EUR', 'GBP', 'CAD', 'MXN', 'NOK', 'BGN', 'ILS', 'DKK', 'HUF']
    var = StringVar()
    val = DoubleVar()
    e = Entry(frame, textvariable=val, relief='sunken', bd=8, font=('arial', 20, 'bold'), justify='center')
    e.grid(row=0, column=0)
    lbl = Label(frame, text='Enter the value in Kč', relief='raised', width=20, font=('arial', 20, 'bold'), border=5)
    lbl.grid(row=0, column=1)
    box = ttk.Combobox(frame, values=options, textvariable=var, state='readonly', width=20, font=('arial', 21, 'bold'))
    box.grid(row=1, column=1)

    def convert():
        if var.get() == 'INR':
            e.insert(0, '%.3f' % c.convert('CZK', 'INR', float(e.get())))
        elif var.get() == 'USD':
            e.insert(0, '%.3f' % c.convert('CZK', 'USD', float(e.get())))
        elif var.get() == 'JPY':
            e.insert(0, '%.3f' % c.convert('CZK', 'JPY', float(e.get())))
        elif var.get() == 'RON':
            e.insert(0, '%.3f' % c.convert('CZK', 'RON', float(e.get())))
        elif var.get() == 'EUR':
            e.insert(0, '%.3f' % c.convert('CZK', 'EUR', float(e.get())))
        elif var.get() == 'GBP':
            e.insert(0, '%.3f' % c.convert('CZK', 'GBP', float(e.get())))
        elif var.get() == 'CAD':
            e.insert(0, '%.3f' % c.convert('CZK', 'CAD', float(e.get())))
        elif var.get() == 'MXN':
            e.insert(0, '%.3f' % c.convert('CZK', 'MXN', float(e.get())))
        elif var.get() == 'NOK':
            e.insert(0, '%.3f' % c.convert('CZK', 'NOK', float(e.get())))
        elif var.get() == 'BGN':
            e.insert(0, '%.3f' % c.convert('CZK', 'BGN', float(e.get())))
        elif var.get() == 'ILS':
            e.insert(0, '%.3f' % c.convert('CZK', 'ILS', float(e.get())))
        elif var.get() == 'DKK':
            e.insert(0, '%.3f' % c.convert('CZK', 'DKK', float(e.get())))
        elif var.get() == 'HUF':
            e.insert(0, '%.3f' % c.convert('CZK', 'HUF', float(e.get())))

    b = Button(frame, text='Convert', command=convert, font=('arial', 20, 'bold'), width=18, bd=3)
    b.grid(row=1, column=0, sticky=W)
    right = Label(frame, text='©PSP', relief='sunken', width=50)
    right.grid(row=2, column=0, sticky=EW, columnspan=2)
    # root8.protocol("WM_DELETE_WINDOW", closeWindow)
    root8.mainloop()


def b9():
    root9 = Toplevel(root)
    root9.title('Conversion from MXN')
    root9.iconbitmap('Mexico_flag.ico')
    c = CurrencyRates()
    root9.resizable(False, False)
    frame = Frame(root9)
    frame.pack()
    options = ['INR', 'JPY', 'USD', 'RON', 'EUR', 'GBP', 'CAD', 'CZK', 'NOK', 'BGN', 'ILS', 'DKK', 'HUF']
    var = StringVar()
    val = DoubleVar()
    e = Entry(frame, textvariable=val, relief='sunken', bd=8, font=('arial', 20, 'bold'), justify='center')
    e.grid(row=0, column=0)
    lbl = Label(frame, text='Enter the value in Mex$', relief='raised', width=20, font=('arial', 20, 'bold'), border=5)
    lbl.grid(row=0, column=1)
    box = ttk.Combobox(frame, values=options, textvariable=var, state='readonly', width=20, font=('arial', 21, 'bold'))
    box.grid(row=1, column=1)

    def convert():
        if var.get() == 'INR':
            e.insert(0, '%.3f' % c.convert('MXN', 'INR', float(e.get())))
        elif var.get() == 'USD':
            e.insert(0, '%.3f' % c.convert('MXN', 'USD', float(e.get())))
        elif var.get() == 'JPY':
            e.insert(0, '%.3f' % c.convert('MXN', 'JPY', float(e.get())))
        elif var.get() == 'RON':
            e.insert(0, '%.3f' % c.convert('MXN', 'RON', float(e.get())))
        elif var.get() == 'EUR':
            e.insert(0, '%.3f' % c.convert('MXN', 'EUR', float(e.get())))
        elif var.get() == 'GBP':
            e.insert(0, '%.3f' % c.convert('MXN', 'GBP', float(e.get())))
        elif var.get() == 'CAD':
            e.insert(0, '%.3f' % c.convert('MXN', 'CAD', float(e.get())))
        elif var.get() == 'CZK':
            e.insert(0, '%.3f' % c.convert('MXN', 'CZK', float(e.get())))
        elif var.get() == 'NOK':
            e.insert(0, '%.3f' % c.convert('MXN', 'NOK', float(e.get())))
        elif var.get() == 'BGN':
            e.insert(0, '%.3f' % c.convert('MXN', 'BGN', float(e.get())))
        elif var.get() == 'ILS':
            e.insert(0, '%.3f' % c.convert('MXN', 'ILS', float(e.get())))
        elif var.get() == 'DKK':
            e.insert(0, '%.3f' % c.convert('MXN', 'DKK', float(e.get())))
        elif var.get() == 'HUF':
            e.insert(0, '%.3f' % c.convert('MXN', 'HUF', float(e.get())))

    b = Button(frame, text='Convert', command=convert, font=('arial', 20, 'bold'), width=18, bd=3)
    b.grid(row=1, column=0, sticky=W)
    right = Label(frame, text='©PSP', relief='sunken', width=50)
    right.grid(row=2, column=0, sticky=EW, columnspan=2)
    # root9.protocol("WM_DELETE_WINDOW", closeWindow)
    root9.mainloop()


def b10():
    root10 = Toplevel(root)
    root10.title('Conversion from NOK')
    root10.iconbitmap('Norway_flag.ico')
    c = CurrencyRates()
    root10.resizable(False, False)
    frame = Frame(root10)
    frame.pack()
    options = ['INR', 'JPY', 'USD', 'RON', 'EUR', 'GBP', 'CAD', 'CZK', 'MXN', 'BGN', 'ILS', 'DKK', 'HUF']
    var = StringVar()
    val = DoubleVar()
    e = Entry(frame, textvariable=val, relief='sunken', bd=8, font=('arial', 20, 'bold'), justify='center')
    e.grid(row=0, column=0)
    lbl = Label(frame, text='Enter the value in kr', relief='raised', width=20, font=('arial', 20, 'bold'), border=5)
    lbl.grid(row=0, column=1)
    box = ttk.Combobox(frame, values=options, textvariable=var, state='readonly', width=20, font=('arial', 21, 'bold'))
    box.grid(row=1, column=1)

    def convert():
        if var.get() == 'INR':
            e.insert(0, '%.3f' % c.convert('NOK', 'INR', float(e.get())))
        elif var.get() == 'USD':
            e.insert(0, '%.3f' % c.convert('NOK', 'USD', float(e.get())))
        elif var.get() == 'JPY':
            e.insert(0, '%.3f' % c.convert('NOK', 'JPY', float(e.get())))
        elif var.get() == 'RON':
            e.insert(0, '%.3f' % c.convert('NOK', 'RON', float(e.get())))
        elif var.get() == 'EUR':
            e.insert(0, '%.3f' % c.convert('NOK', 'EUR', float(e.get())))
        elif var.get() == 'GBP':
            e.insert(0, '%.3f' % c.convert('NOK', 'GBP', float(e.get())))
        elif var.get() == 'CAD':
            e.insert(0, '%.3f' % c.convert('NOK', 'CAD', float(e.get())))
        elif var.get() == 'CZK':
            e.insert(0, '%.3f' % c.convert('NOK', 'CZK', float(e.get())))
        elif var.get() == 'MXN':
            e.insert(0, '%.3f' % c.convert('NOK', 'MXN', float(e.get())))
        elif var.get() == 'BGN':
            e.insert(0, '%.3f' % c.convert('NOK', 'BGN', float(e.get())))
        elif var.get() == 'ILS':
            e.insert(0, '%.3f' % c.convert('NOK', 'ILS', float(e.get())))
        elif var.get() == 'DKK':
            e.insert(0, '%.3f' % c.convert('NOK', 'DKK', float(e.get())))
        elif var.get() == 'HUF':
            e.insert(0, '%.3f' % c.convert('NOK', 'HUF', float(e.get())))

    b = Button(frame, text='Convert', command=convert, font=('arial', 20, 'bold'), width=18, bd=3)
    b.grid(row=1, column=0, sticky=W)
    right = Label(frame, text='©PSP', relief='sunken', width=50)
    right.grid(row=2, column=0, sticky=EW, columnspan=2)
    # root10.protocol("WM_DELETE_WINDOW", closeWindow)
    root10.mainloop()


def b11():
    root11 = Toplevel(root)
    root11.title('Conversion from BGN')
    root11.iconbitmap('Bulgaria_flag.ico')
    c = CurrencyRates()
    root11.resizable(False, False)
    frame = Frame(root11)
    frame.pack()
    options = ['INR', 'JPY', 'USD', 'RON', 'EUR', 'GBP', 'CAD', 'CZK', 'MXN', 'NOK', 'ILS', 'DKK', 'HUF']
    var = StringVar()
    val = DoubleVar()
    e = Entry(frame, textvariable=val, relief='sunken', bd=8, font=('arial', 20, 'bold'), justify='center')
    e.grid(row=0, column=0)
    lbl = Label(frame, text='Enter the value in Лв', relief='raised', width=20, font=('arial', 20, 'bold'), border=5)
    lbl.grid(row=0, column=1)
    box = ttk.Combobox(frame, values=options, textvariable=var, state='readonly', width=20, font=('arial', 21, 'bold'))
    box.grid(row=1, column=1)

    def convert():
        if var.get() == 'INR':
            e.insert(0, '%.3f' % c.convert('BGN', 'INR', float(e.get())))
        elif var.get() == 'USD':
            e.insert(0, '%.3f' % c.convert('BGN', 'USD', float(e.get())))
        elif var.get() == 'JPY':
            e.insert(0, '%.3f' % c.convert('BGN', 'JPY', float(e.get())))
        elif var.get() == 'RON':
            e.insert(0, '%.3f' % c.convert('BGN', 'RON', float(e.get())))
        elif var.get() == 'EUR':
            e.insert(0, '%.3f' % c.convert('BGN', 'EUR', float(e.get())))
        elif var.get() == 'GBP':
            e.insert(0, '%.3f' % c.convert('BGN', 'GBP', float(e.get())))
        elif var.get() == 'CAD':
            e.insert(0, '%.3f' % c.convert('BGN', 'CAD', float(e.get())))
        elif var.get() == 'CZK':
            e.insert(0, '%.3f' % c.convert('BGN', 'CZK', float(e.get())))
        elif var.get() == 'MXN':
            e.insert(0, '%.3f' % c.convert('BGN', 'MXN', float(e.get())))
        elif var.get() == 'NOK':
            e.insert(0, '%.3f' % c.convert('BGN', 'NOK', float(e.get())))
        elif var.get() == 'ILS':
            e.insert(0, '%.3f' % c.convert('BGN', 'ILS', float(e.get())))
        elif var.get() == 'DKK':
            e.insert(0, '%.3f' % c.convert('BGN', 'DKK', float(e.get())))
        elif var.get() == 'HUF':
            e.insert(0, '%.3f' % c.convert('BGN', 'HUF', float(e.get())))

    b = Button(frame, text='Convert', command=convert, font=('arial', 20, 'bold'), width=18, bd=3)
    b.grid(row=1, column=0, sticky=W)
    right = Label(frame, text='©PSP', relief='sunken', width=50)
    right.grid(row=2, column=0, sticky=EW, columnspan=2)
    # root11.protocol("WM_DELETE_WINDOW", closeWindow)
    root11.mainloop()


def b12():
    root12 = Toplevel(root)
    root12.title('Conversion from ILS')
    root12.iconbitmap('Israel_flag.ico')
    c = CurrencyRates()
    root12.resizable(False, False)
    frame = Frame(root12)
    frame.pack()
    options = ['INR', 'JPY', 'USD', 'RON', 'EUR', 'GBP', 'CAD', 'CZK', 'MXN', 'NOK', 'ILS', 'DKK', 'HUF']
    var = StringVar()
    val = DoubleVar()
    e = Entry(frame, textvariable=val, relief='sunken', bd=8, font=('arial', 20, 'bold'), justify='center')
    e.grid(row=0, column=0)
    lbl = Label(frame, text='Enter the value in ₪', relief='raised', width=20, font=('arial', 20, 'bold'), border=5)
    lbl.grid(row=0, column=1)
    box = ttk.Combobox(frame, values=options, textvariable=var, state='readonly', width=20, font=('arial', 21, 'bold'))
    box.grid(row=1, column=1)

    def convert():
        if var.get() == 'INR':
            e.insert(0, '%.3f' % c.convert('BGN', 'INR', float(e.get())))
        elif var.get() == 'USD':
            e.insert(0, '%.3f' % c.convert('BGN', 'USD', float(e.get())))
        elif var.get() == 'JPY':
            e.insert(0, '%.3f' % c.convert('BGN', 'JPY', float(e.get())))
        elif var.get() == 'RON':
            e.insert(0, '%.3f' % c.convert('BGN', 'RON', float(e.get())))
        elif var.get() == 'EUR':
            e.insert(0, '%.3f' % c.convert('BGN', 'EUR', float(e.get())))
        elif var.get() == 'GBP':
            e.insert(0, '%.3f' % c.convert('BGN', 'GBP', float(e.get())))
        elif var.get() == 'CAD':
            e.insert(0, '%.3f' % c.convert('BGN', 'CAD', float(e.get())))
        elif var.get() == 'CZK':
            e.insert(0, '%.3f' % c.convert('BGN', 'CZK', float(e.get())))
        elif var.get() == 'MXN':
            e.insert(0, '%.3f' % c.convert('BGN', 'MXN', float(e.get())))
        elif var.get() == 'NOK':
            e.insert(0, '%.3f' % c.convert('BGN', 'NOK', float(e.get())))
        elif var.get() == 'ILS':
            e.insert(0, '%.3f' % c.convert('BGN', 'ILS', float(e.get())))
        elif var.get() == 'DKK':
            e.insert(0, '%.3f' % c.convert('BGN', 'DKK', float(e.get())))
        elif var.get() == 'HUF':
            e.insert(0, '%.3f' % c.convert('BGN', 'HUF', float(e.get())))

    b = Button(frame, text='Convert', command=convert, font=('arial', 20, 'bold'), width=18, bd=3)
    b.grid(row=1, column=0, sticky=W)
    right = Label(frame, text='©PSP', relief='sunken', width=50)
    right.grid(row=2, column=0, sticky=EW, columnspan=2)
    # root12.protocol("WM_DELETE_WINDOW", closeWindow)
    root12.mainloop()


def b13():
    root13 = Toplevel(root)
    root13.title('Conversion from DKK')
    root13.iconbitmap('Denmark_flag.ico')
    c = CurrencyRates()
    root13.resizable(False, False)
    frame = Frame(root13)
    frame.pack()
    options = ['INR', 'JPY', 'USD', 'RON', 'EUR', 'GBP', 'CAD', 'CZK', 'MXN', 'NOK', 'ILS', 'BGN', 'HUF']
    var = StringVar()
    val = DoubleVar()
    e = Entry(frame, textvariable=val, relief='sunken', bd=8, font=('arial', 20, 'bold'), justify='center')
    e.grid(row=0, column=0)
    lbl = Label(frame, text='Enter the value in Kr', relief='raised', width=20, font=('arial', 20, 'bold'), border=5)
    lbl.grid(row=0, column=1)
    box = ttk.Combobox(frame, values=options, textvariable=var, state='readonly', width=20, font=('arial', 21, 'bold'))
    box.grid(row=1, column=1)

    def convert():
        if var.get() == 'INR':
            e.insert(0, '%.3f' % c.convert('DKK', 'INR', float(e.get())))
        elif var.get() == 'USD':
            e.insert(0, '%.3f' % c.convert('DKK', 'USD', float(e.get())))
        elif var.get() == 'JPY':
            e.insert(0, '%.3f' % c.convert('DKK', 'JPY', float(e.get())))
        elif var.get() == 'RON':
            e.insert(0, '%.3f' % c.convert('DKK', 'RON', float(e.get())))
        elif var.get() == 'EUR':
            e.insert(0, '%.3f' % c.convert('DKK', 'EUR', float(e.get())))
        elif var.get() == 'GBP':
            e.insert(0, '%.3f' % c.convert('DKK', 'GBP', float(e.get())))
        elif var.get() == 'CAD':
            e.insert(0, '%.3f' % c.convert('DKK', 'CAD', float(e.get())))
        elif var.get() == 'CZK':
            e.insert(0, '%.3f' % c.convert('DKK', 'CZK', float(e.get())))
        elif var.get() == 'MXN':
            e.insert(0, '%.3f' % c.convert('DKK', 'MXN', float(e.get())))
        elif var.get() == 'NOK':
            e.insert(0, '%.3f' % c.convert('DKK', 'NOK', float(e.get())))
        elif var.get() == 'ILS':
            e.insert(0, '%.3f' % c.convert('DKK', 'ILS', float(e.get())))
        elif var.get() == 'BGN':
            e.insert(0, '%.3f' % c.convert('DKK', 'BGN', float(e.get())))
        elif var.get() == 'HUF':
            e.insert(0, '%.3f' % c.convert('DKK', 'HUF', float(e.get())))

    b = Button(frame, text='Convert', command=convert, font=('arial', 20, 'bold'), width=18, bd=3)
    b.grid(row=1, column=0, sticky=W)
    right = Label(frame, text='©PSP', relief='sunken', width=50)
    right.grid(row=2, column=0, sticky=EW, columnspan=2)
    # root13.protocol("WM_DELETE_WINDOW", closeWindow)
    root13.mainloop()


def b14():
    root14 = Toplevel(root)
    root14.title('Conversion from HUF')
    root14.iconbitmap('Hungary_flag.ico')
    c = CurrencyRates()
    root14.resizable(False, False)
    frame = Frame(root14)
    frame.pack()
    options = ['INR', 'JPY', 'USD', 'RON', 'EUR', 'GBP', 'CAD', 'CZK', 'MXN', 'NOK', 'ILS', 'BGN', 'HUF']
    var = StringVar()
    val = DoubleVar()
    e = Entry(frame, textvariable=val, relief='sunken', bd=8, font=('arial', 20, 'bold'), justify='center')
    e.grid(row=0, column=0)
    lbl = Label(frame, text='Enter the value in Ft', relief='raised', width=20, font=('arial', 20, 'bold'), border=5)
    lbl.grid(row=0, column=1)
    box = ttk.Combobox(frame, values=options, textvariable=var, state='readonly', width=20, font=('arial', 21, 'bold'))
    box.grid(row=1, column=1)

    def convert():
        if var.get() == 'INR':
            e.insert(0, '%.3f' % c.convert('HUF', 'INR', float(e.get())))
        elif var.get() == 'USD':
            e.insert(0, '%.3f' % c.convert('HUF', 'USD', float(e.get())))
        elif var.get() == 'JPY':
            e.insert(0, '%.3f' % c.convert('HUF', 'JPY', float(e.get())))
        elif var.get() == 'RON':
            e.insert(0, '%.3f' % c.convert('HUF', 'RON', float(e.get())))
        elif var.get() == 'EUR':
            e.insert(0, '%.3f' % c.convert('HUF', 'EUR', float(e.get())))
        elif var.get() == 'GBP':
            e.insert(0, '%.3f' % c.convert('HUF', 'GBP', float(e.get())))
        elif var.get() == 'CAD':
            e.insert(0, '%.3f' % c.convert('HUF', 'CAD', float(e.get())))
        elif var.get() == 'CZK':
            e.insert(0, '%.3f' % c.convert('HUF', 'CZK', float(e.get())))
        elif var.get() == 'MXN':
            e.insert(0, '%.3f' % c.convert('HUF', 'MXN', float(e.get())))
        elif var.get() == 'NOK':
            e.insert(0, '%.3f' % c.convert('HUF', 'NOK', float(e.get())))
        elif var.get() == 'ILS':
            e.insert(0, '%.3f' % c.convert('HUF', 'ILS', float(e.get())))
        elif var.get() == 'BGN':
            e.insert(0, '%.3f' % c.convert('HUF', 'BGN', float(e.get())))
        elif var.get() == 'DKK':
            e.insert(0, '%.3f' % c.convert('HUF', 'DKK', float(e.get())))

    b = Button(frame, text='Convert', command=convert, font=('arial', 20, 'bold'), width=18, bd=3)
    b.grid(row=1, column=0, sticky=W)
    right = Label(frame, text='©PSP', relief='sunken', width=50)
    right.grid(row=2, column=0, sticky=EW, columnspan=2)
    # root14.protocol("WM_DELETE_WINDOW", closeWindow)
    root14.mainloop()


tday = datetime.date.today()
# -------------------------------buttons---------------------------------------------
Label(second_frame, text='Please Select A Currency', fg='#fe4a49', font=('calibri', 20, 'bold'), bg='#5b5b5b').pack(
    fill=BOTH)
btn1 = Button(second_frame, text='INR', justify='center', font=('arial', 20, 'bold'), bd=8, relief='raise', command=b1,
              bg='#ffb997')
btn1.pack(fill=BOTH)
btn2 = Button(second_frame, text='USD', justify='center', font=('arial', 20, 'bold'), width=34, bd=8, relief='raise',
              command=b2, bg='#ffd670')
btn2.pack(fill=BOTH)
btn3 = Button(second_frame, text='JPY', justify='center', font=('arial', 20, 'bold'), width=34, bd=8, relief='raise',
              command=b3, bg='#eafdf8')
btn3.pack(fill=BOTH)
btn4 = Button(second_frame, text='EUR', justify='center', font=('arial', 20, 'bold'), width=34, bd=8, relief='raise',
              command=b4, bg='#edbfc6')
btn4.pack(fill=BOTH)
btn5 = Button(second_frame, text='RON', justify='center', font=('arial', 20, 'bold'), width=34, bd=8, relief='raise',
              command=b5, bg='#70d6ff')
btn5.pack(fill=BOTH)
btn6 = Button(second_frame, text='GBP', justify='center', font=('arial', 20, 'bold'), width=34, bd=8, relief='raise',
              command=b6, bg='#dcf763')
btn6.pack()
btn7 = Button(second_frame, text='CAD', justify='center', font=('arial', 20, 'bold'), width=34, bd=8, relief='raise',
              command=b7, bg='#ffb997')
btn7.pack()
btn8 = Button(second_frame, text='CZK', justify='center', font=('arial', 20, 'bold'), width=34, bd=8, relief='raise',
              command=b8, bg='#ffd670')
btn8.pack()
btn9 = Button(second_frame, text='MXN', justify='center', font=('arial', 20, 'bold'), width=34, bd=8, relief='raise',
              command=b9, bg='#eafdf8')
btn9.pack()
btn10 = Button(second_frame, text='NOK', justify='center', font=('arial', 20, 'bold'), width=34, bd=8, relief='raise',
               command=b10, bg='#edbfc6')
btn10.pack()
btn11 = Button(second_frame, text='BGN', justify='center', font=('arial', 20, 'bold'), width=34, bd=8, relief='raise',
               command=b11, bg='#70d6ff')
btn11.pack()
btn12 = Button(second_frame, text='ILS', justify='center', font=('arial', 20, 'bold'), width=34, bd=8, relief='raise',
               command=b12, bg='#dcf763')
btn12.pack()
btn13 = Button(second_frame, text='DKK', justify='center', font=('arial', 20, 'bold'), width=34, bd=8, relief='raise',
               command=b13, bg='#ffb997')
btn13.pack()
btn14 = Button(second_frame, text='HUF', justify='center', font=('arial', 20, 'bold'), width=34, bd=8, relief='raise',
               command=b14, bg='#ffd670')
btn14.pack()
# btn15 = Button(second_frame, text='Show All Full Forms', justify='center', font=('arial', 20, 'bold'), width=34, bd=8,
# relief='raise',
# command=cun, bg='#edbfc6')
# btn15.pack()
my_label = Label(second_frame, text='Date: ' + str(tday), justify='center', relief='sunken', font=('Helvetica', 10))
my_label.pack(fill=BOTH)
t_time = Label(second_frame, relief='sunken', font=('Helvetica', 10))
t_time.pack(fill=BOTH)
clock()

#-----------------------------Graphs---------------------------------------------------
def c1():
    a = ['INR', 'RON', 'JPY', 'GBP', 'EUR', 'CAD', 'CZK', 'MXN', 'NOK', 'BGN', 'ILS', 'DKK', 'HUF']
    y1 = (c.convert('USD', 'INR', 1))
    y2 = (c.convert('USD', 'RON', 1))
    y3 = (c.convert('USD', 'JPY', 1))
    y4 = (c.convert('USD', 'GBP', 1))
    y5 = (c.convert('USD', 'EUR', 1))
    y6 = (c.convert('USD', 'CAD', 1))
    y7 = (c.convert('USD', 'CZK', 1))
    y8 = (c.convert('USD', 'MXN', 1))
    y9 = (c.convert('USD', 'NOK', 1))
    y10 = (c.convert('USD', 'BGN', 1))
    y11 = (c.convert('USD', 'ILS', 1))
    y12 = (c.convert('USD', 'DKK', 1))
    y13 = (c.convert('USD', 'HUF', 1))
    y = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13]
    # print(y)
    plt.xlabel('Countries', fontsize=12)
    plt.ylabel('USD Rates', fontsize = 12)
    plt.title('US Dollar Conversion', color = 'c', fontsize = 18)
    plt.bar(a, y)
    plt.show()
def c2():
    a = ['USD', 'RON', 'JPY', 'GBP', 'EUR', 'CAD', 'CZK', 'MXN', 'NOK', 'BGN', 'ILS', 'DKK', 'HUF']
    y1 = (c.convert('INR', 'USD', 1))
    y2 = (c.convert('INR', 'RON', 1))
    y3 = (c.convert('INR', 'JPY', 1))
    y4 = (c.convert('INR', 'GBP', 1))
    y5 = (c.convert('INR', 'EUR', 1))
    y6 = (c.convert('INR', 'CAD', 1))
    y7 = (c.convert('INR', 'CZK', 1))
    y8 = (c.convert('INR', 'MXN', 1))
    y9 = (c.convert('INR', 'NOK', 1))
    y10 = (c.convert('INR', 'BGN', 1))
    y11 = (c.convert('INR', 'ILS', 1))
    y12 = (c.convert('INR', 'DKK', 1))
    y13 = (c.convert('INR', 'HUF', 1))
    y = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13]
    # print(y)
    plt.bar(a, y, color = 'orange')
    plt.xlabel('Countries', fontsize = 12)
    plt.ylabel('INR Rates', fontsize = 12)
    plt.title('Indian Rupees Conversion', color = 'green', fontsize = 18)
    plt.show()
#-----------------------------Menu----------------------------------------------------
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu, tearoff = False)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='INR Rates', command = c2)
filemenu.add_separator()
filemenu.add_command(label='USD Rates', command = c1)
#filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu, tearoff = False)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Show Full Forms', command=cun)

# ----------------------------end of buttons------------------------------------------
root.mainloop()

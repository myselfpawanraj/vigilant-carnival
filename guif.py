#!/usr/bin/python
import sqlite3
import random
import datetime

connection = sqlite3.connect("BAS.db", 300)

cursor = connection.cursor()

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

import PIL
from PIL import Image
from PIL import ImageTk



from tkcalendar import Calendar, DateEntry

global cart, session_type

'''
    0 - customer
    1 - clerk
    2 - manager
    3 - owner
'''
cart = []


class Table:
     
    def __init__(self, root, lst, w = 16, foreg = 'black', backg = 'white'):
         
        # code for creating table
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                
                self.e = Entry(root, width=w, fg=foreg, bg=backg, 
                               font=('Arial',16))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


def confirm_update_inventory():
    global confirm_update_inventory_window
    confirm_update_inventory_window = Tk()
    confirm_update_inventory_window.geometry('500x150+300+120')
    confirm_update_inventory_window.title('Confirm Book Update')
    isbn = str(ei1.get())
    name = str(ei2.get())
    auth = str(ei3.get())
    price = str(ei4.get())
    cat = str(ei5.get())
    pub = str(ei6.get())
    number_of_copies = str(ei7.get())
    threshold_number_of_books = str(ei8.get())
    average_days_of_procuring = str(ei9.get())

    if (isbn != '' and name != '' and auth != '' and price != '' and cat != ''
            and pub != '' and number_of_copies != '' and threshold_number_of_books != ''
            and average_days_of_procuring != ''):
        l1 = Label(confirm_update_inventory_window,
                   text='Are you sure you want to update this book?',
                   font=(10))
        b1 = Button(confirm_update_inventory_window, text='Yes', width=10, height=3, command=update_book_in_db)
        b2 = Button(confirm_update_inventory_window, text='No', width=10, height=3, command=confbdest)

        l1.place(x=60, y=20)
        b1.place(x=80, y=80)
        b2.place(x=320, y=80)

    else:
        l10 = Label(inv, text='Please enter all details', fg='red', font=(10))
        l10.place(x=150, y=440)
        confirm_update_inventory_window.destroy()
        l10.after(3000, lambda: l10.place_forget())


def confbkadd():
    global confirmb
    confirmb = Tk()
    confirmb.geometry('500x150+300+120')
    confirmb.title('Confirm Book')
    isbn = str(ei1.get())
    name = str(ei2.get())
    auth = str(ei3.get())
    price = str(ei4.get())
    cat = str(ei5.get())
    pub = str(ei6.get())
    number_of_copies = str(ei7.get())
    threshold_number_of_books = str(ei8.get())
    average_days_of_procuring = str(ei9.get())

    if (isbn != '' and name != '' and auth != '' and price != '' and cat != ''
            and pub != '' and number_of_copies != '' and threshold_number_of_books != ''
            and average_days_of_procuring != ''):
        l1 = Label(confirmb,
                   text='Are you sure you want to add this book?',
                   font=(10))
        b1 = Button(confirmb, text='Yes', width=10, height=3, command=bookadd)
        b2 = Button(confirmb, text='No', width=10, height=3, command=confbdest)

        l1.place(x=60, y=20)
        b1.place(x=80, y=80)
        b2.place(x=320, y=80)

    else:
        l10 = Label(inv, text='Please enter all details', fg='red', font=(10))
        l10.place(x=150, y=440)
        confirmb.destroy()
        l10.after(3000, lambda: l10.place_forget())


def confbdest():
    confirmb.destroy()



def update_book_in_db():
    confirm_update_inventory_window.destroy()
    isbn = str(ei1.get())
    name = str(ei2.get())
    auth = str(ei3.get())
    price = float(ei4.get())
    cat = str(ei5.get())
    pub = str(ei6.get())
    number_of_copies = int(ei7.get())
    threshold_number_of_books = int(ei8.get())
    average_days_of_procuring = int(ei9.get())

    vis = Label(update_inventory_window, text='Book updated successfully!', font=(8))
    vis.place(x=150, y=460)
    vis.after(3000, lambda: vis.place_forget())
    cursor.execute('UPDATE Book SET Book_Name=?, Author=?, Price=?, Category=?, Publisher=?, number_of_copies=?, threshold=?, average_number_of_days_to_procure=?, rack_number=? WHERE Book_ISBN=?',
                   (name, auth, price, cat, pub, 
                    number_of_copies, threshold_number_of_books, average_days_of_procuring, 1, isbn))
    connection.commit()
    return


def bookadd():
    confirmb.destroy()
    isbn = str(ei1.get())
    name = str(ei2.get())
    auth = str(ei3.get())
    price = float(ei4.get())
    cat = str(ei5.get())
    pub = str(ei6.get())
    number_of_copies = int(ei7.get())
    threshold_number_of_books = int(ei8.get())
    average_days_of_procuring = int(ei9.get())

    vis = Label(inv, text='Book Added successfully!', font=(8))
    vis.place(x=150, y=460)
    vis.after(3000, lambda: vis.place_forget())
    cursor.execute('INSERT INTO Book VALUES (?,?,?,?,?,?,?,?,?,?)',
                   (isbn, name, auth, price, cat, pub, 
                    number_of_copies, threshold_number_of_books, average_days_of_procuring, 1))
    connection.commit()
    return


def vsrec():

    cursor.execute("SELECT * FROM Sales")
    rows = cursor.fetchall()

    searchres = Tk()
    searchres.geometry('960x640+100+120')
    searchres.title('Sales Records')

    srl = Label(searchres,
                text='Sales Records:',
                font=('Sales Records:', 13),
                bg='Moccasin',
                fg='black')
    srl.place(x=80, y=40)

    l1 = Label(searchres, text='Sales ID', font=('Sales ID', 10))
    l2 = Label(searchres, text='Customer ID', font=('Customer', 10))
    l3 = Label(searchres, text='Invoice No', font=('Invoice No', 10))
    l4 = Label(searchres, text='Sales Date', font=('Sales Date', 10))
    l5 = Label(searchres, text='Bill Amount', font=('Bill Amount', 10))

    l1.place(x=60, y=80)
    l2.place(x=235, y=80)
    l3.place(x=410, y=80)
    l4.place(x=585, y=80)
    l5.place(x=760, y=80)

    col = 100
    for r in rows:
        row = 60
        for x in r:
            templabel = Label(searchres, text=x, font=(str(x), 8))
            templabel.place(x=row, y=col)
            row = row + 175
        col = col + 15

    return


def update_inventory():
    global update_inventory_window
    update_inventory_window = Tk()
    update_inventory_window.geometry('720x600+500+120')
    update_inventory_window.title('Book Inventory')
    wel = Label(update_inventory_window, text='Update Book', fg='black', bg='Moccasin', font=(16))
    global ei1, ei2, ei3, ei4, ei5, ei6, ei7, ei8, ei9
    l1 = Label(update_inventory_window, text='Book ISBN:', font=(10))
    l2 = Label(update_inventory_window, text='Book Name:', font=(10))
    l3 = Label(update_inventory_window, text='Author:', font=(10))
    l4 = Label(update_inventory_window, text='Price:', font=(10))
    l5 = Label(update_inventory_window, text='Category:', font=(10))
    l6 = Label(update_inventory_window, text='Publisher:', font=(10))
    l7 = Label(update_inventory_window, text='Number of copies:', font=(10))
    l8 = Label(update_inventory_window, text='Threshold number of copies:', font=(10))
    l9 = Label(update_inventory_window, text='Average number of days to procure:', font=(10))

    ei1 = Entry(update_inventory_window, font=(10), bd=5)
    ei2 = Entry(update_inventory_window, font=(10), bd=5)
    ei3 = Entry(update_inventory_window, font=(10), bd=5)
    ei4 = Entry(update_inventory_window, font=(10), bd=5)
    ei5 = Entry(update_inventory_window, font=(10), bd=5)
    ei6 = Entry(update_inventory_window, font=(10), bd=5)
    ei7 = Entry(update_inventory_window, font=(10), bd=5)
    ei8 = Entry(update_inventory_window, font=(10), bd=5)
    ei9 = Entry(update_inventory_window, font=(10), bd=5)

    b1 = Button(update_inventory_window, text='Update Book', width=20, height=3, command=confirm_update_inventory)
    wel.place(x=150, y=40)
    l1.place(x=70, y=80)
    ei1.place(x=420, y=80)
    l2.place(x=70, y=120)   
    ei2.place(x=420, y=120)
    l3.place(x=70, y=160)
    ei3.place(x=420, y=160)
    l4.place(x=70, y=200)
    ei4.place(x=420, y=200)
    l5.place(x=70, y=240)
    ei5.place(x=420, y=240)
    l6.place(x=70, y=280)
    ei6.place(x=420, y=280)
    l7.place(x=70, y=320)
    ei7.place(x=420, y=320)
    l8.place(x=70, y=360)
    ei8.place(x=420, y=360)
    l9.place(x=70, y=400)
    ei9.place(x=420, y=400)
    b1.place(x=150, y=500)
    return


def addinv():
    global inv
    inv = Tk()
    inv.geometry('720x600+500+120')
    inv.title('Book Inventory')
    wel = Label(inv, text='Add New Book', fg='black', bg='Moccasin', font=(16))
    global ei1, ei2, ei3, ei4, ei5, ei6, ei7, ei8, ei9
    l1 = Label(inv, text='Book ISBN:', font=(10))
    l2 = Label(inv, text='Book Name:', font=(10))
    l3 = Label(inv, text='Author:', font=(10))
    l4 = Label(inv, text='Price:', font=(10))
    l5 = Label(inv, text='Category:', font=(10))
    l6 = Label(inv, text='Publisher:', font=(10))
    l7 = Label(inv, text='Number of copies:', font=(10))
    l8 = Label(inv, text='Threshold number of copies:', font=(10))
    l9 = Label(inv, text='Average number of days to procure:', font=(10))

    ei1 = Entry(inv, font=(10), bd=5)
    ei2 = Entry(inv, font=(10), bd=5)
    ei3 = Entry(inv, font=(10), bd=5)
    ei4 = Entry(inv, font=(10), bd=5)
    ei5 = Entry(inv, font=(10), bd=5)
    ei6 = Entry(inv, font=(10), bd=5)
    ei7 = Entry(inv, font=(10), bd=5)
    ei8 = Entry(inv, font=(10), bd=5)
    ei9 = Entry(inv, font=(10), bd=5)

    b1 = Button(inv, text='Add Book', width=20, height=3, command=confbkadd)
    wel.place(x=150, y=40)
    l1.place(x=70, y=80)
    ei1.place(x=420, y=80)
    l2.place(x=70, y=120)   
    ei2.place(x=420, y=120)
    l3.place(x=70, y=160)
    ei3.place(x=420, y=160)
    l4.place(x=70, y=200)
    ei4.place(x=420, y=200)
    l5.place(x=70, y=240)
    ei5.place(x=420, y=240)
    l6.place(x=70, y=280)
    ei6.place(x=420, y=280)
    l7.place(x=70, y=320)
    ei7.place(x=420, y=320)
    l8.place(x=70, y=360)
    ei8.place(x=420, y=360)
    l9.place(x=70, y=400)
    ei9.place(x=420, y=400)
    b1.place(x=150, y=500)
    return


def viewpur():
    cursor.execute("SELECT * FROM Purchase")
    rows = cursor.fetchall()

    searchres = Tk()
    searchres.geometry('840x640+100+120')
    searchres.title('Purchase Records')

    srl = Label(searchres,
                text='Purchase Records:',
                font=('Purchase Records:', 13),
                bg='Moccasin',
                fg='black')
    srl.place(x=80, y=40)

    l1 = Label(searchres, text='Purchase ID', font=('Sales ID', 10))
    l2 = Label(searchres, text='Supplier ID', font=('Customer', 10))
    l3 = Label(searchres, text='Purchase Date', font=('Invoice No', 10))
    l4 = Label(searchres, text='Amount Paid', font=('Sales Date', 10))

    l1.place(x=40, y=80)
    l2.place(x=240, y=80)
    l3.place(x=440, y=80)
    l4.place(x=640, y=80)

    col = 100
    for r in rows:
        row = 40
        for x in r:
            templabel = Label(searchres, text=x, font=(str(x), 8))
            templabel.place(x=row, y=col)
            row = row + 200
        col = col + 15

    return


def puradd():
    confirmp.destroy()
    purid = str("pur" + str(random.randint(150, 1000000)))
    supid = str(ep2.get())
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    price = float(ep6.get())

    vis = Label(pur, text='Purchase Added successfully!', font=(8))
    vis.place(x=150, y=460)
    vis.after(3000, lambda: vis.place_forget())
    cursor.execute('INSERT INTO Purchase VALUES (?,?,?,?)',
                   (purid, supid, date, price))
    connection.commit()
    return


def confpur():
    global confirmp
    confirmp = Tk()
    confirmp.geometry('500x150+300+120')
    confirmp.title('Confirm Purchase')
    supid = str(ep2.get())
    price = str(ep6.get())

    if (supid != '' and price != ''):
        l1 = Label(confirmp,
                   text='Are you sure you want to add this purchase?',
                   font=(10))
        b1 = Button(confirmp, text='Yes', width=10, height=3, command=puradd)
        b2 = Button(confirmp, text='No', width=10, height=3, command=confdest)

        l1.place(x=40, y=20)
        b1.place(x=80, y=80)
        b2.place(x=320, y=80)
    else:
        l2 = Label(pur, text='Please enter all details', font=(10), fg='red')
        l2.place(x=200, y=430)
        l2.after(3000, lambda: l2.place_forget())
        confdest()


def confdest():
    confirmp.destroy()


def addpur():
    global pur
    pur = Tk()
    pur.geometry('640x400+500+120')
    pur.title('Book Purchase')
    wel = Label(pur, text='New Book Purchase from Suplier', fg='black', font=(16))
    global ep1, ep2, ep3, ep4, ep5, ep6
    # l1 = Label(pur, text='Purchase ID:', font=(10))
    l2 = Label(pur, text='Supplier ID:', font=(10))
    l7 = Label(pur, text='Price:', font=(10))

    ep2 = Entry(pur, font=(10), bd=5)
    ep6 = Entry(pur, font=(10), bd=5)

    b1 = Button(pur,
                text='Add Purchase Record',
                width=30,
                height=3,
                bg='lightgreen',
                command=confpur)
    b2 = Button(pur,
                text='Find supplier ID',
                width=30,
                height=3,
                bg='lightblue',
                command=search_supplier)

    wel.place(x=150, y=40)
    # l1.place(x=70, y=80)
    # ep1.place(x=230, y=80)
    l2.place(x=70, y=100)
    ep2.place(x=230, y=100)
    l7.place(x=70, y=190)
    ep6.place(x=230, y=190)

    b2.place(x=60, y=250)
    b1.place(x=360, y=250)
    return


def reqadd():
    confirmr.destroy()
    book = str(cb1.get())
    auth = str(ca1.get())

    vis = Label(request, text='Request made successfully!', font=(8))
    vis.place(x=150, y=460)
    vis.after(3000, lambda: vis.place_forget())
    cursor.execute('INSERT INTO Request VALUES (?,?)', (book, auth))
    connection.commit()
    return


def confreqdest():
    confirmr.destroy()


def confreq():
    global confirmr
    confirmr = Tk()
    confirmr.geometry('500x150+300+120')
    confirmr.title('Confirm Request')

    l1 = Label(confirmr,
               text='Are you sure you want to request this book?',
               font=(10))
    b1 = Button(confirmr, text='Yes', width=10, height=3, command=reqadd)
    b2 = Button(confirmr, text='No', width=10, height=3, command=confreqdest)

    l1.place(x=40, y=20)
    b1.place(x=80, y=80)
    b2.place(x=320, y=80)


def cusreq():
    global cb1, ca1
    global request
    request = Tk()
    request.geometry('640x480+700+120')
    request.title('Request Book')
    disp = Label(request,
                 text='Request your book here:',
                 fg='black',
                 bg='Moccasin',
                 font=(12))
    disp.place(x=200, y=70)
    sl1 = Label(request, text='Book Title:', font=('Book Title:', 10))
    cb1 = Entry(request, font=(10), bd=5)

    sl2 = Label(request, text='Author:', font=('Author:', 10))
    ca1 = Entry(request, font=(10), bd=5)

    sl1.place(x=100, y=140)
    cb1.place(x=210, y=140)

    sl2.place(x=100, y=220)
    ca1.place(x=210, y=220)

    sb = Button(request,
                text='Request Book',
                width=20,
                height=2,
                command=confreq)
    sb.place(x=210, y=300)
    return


def logoutadm():
    session_type = 0
    admpg.destroy()
    return


def getbooksunderthreshold():
    threshold = Tk()
    threshold.geometry('1000x600+700+120')
    threshold.title('Book threshold')
    cursor.execute("SELECT Book_ISBN, Book_Name, number_of_copies, Price, Publisher FROM Book b WHERE b.number_of_copies <= b.threshold")
    rows = cursor.fetchall()

    srl = Label(threshold,
                text='Books below or at threshold level',
                font=('Customer Book threshold:', 12),
                bg='Moccasin',
                fg='black')
    srl.place(x=80, y=40)

    l1 = Label(threshold, text='ISBN', font=('Sales ID', 10))
    l2 = Label(threshold, text='Name', font=('Customer', 10))
    l3 = Label(threshold, text='Number of copies', font=('Customer', 10))
    l4 = Label(threshold, text='Price', font=('Customer', 10))
    l5 = Label(threshold, text='Publisher', font=('Customer', 10))

    l1.place(x=60, y=80)
    l2.place(x=210, y=80)
    l3.place(x=430, y=80)
    l4.place(x=580, y=80)
    l5.place(x=730, y=80)

    col = 100
    ix = 0
    for r in rows:
        row = 60
        ix = 0
        for x in r:
            extend = 220
            if not ix or ix == 3 or ix == 2:
                extend = 150
            templabel = Label(threshold, text=x, font=(str(x), 8))
            templabel.place(x=row, y=col)
            row = row + extend
            ix += 1

        col = col + 15

    return


def show_sales_statistics():
    sales_statistics_selection_window = Tk()
    sales_statistics_selection_window.geometry('800x640+500+200')
    sales_statistics_selection_window.title('Sales statistics selection')

    global calfrom, calto
    calfrom = DateEntry(
        sales_statistics_selection_window, selectmode = 'day', 
        year = 2022, month = 4, 
        day = 12)
    calto = DateEntry(
        sales_statistics_selection_window, selectmode = 'day', 
        year = 2022, month = 4, 
        day = 14)

    calfrom.pack(pady = 10)
    calto.pack(pady = 40)

    l1 = Label(sales_statistics_selection_window, text='From date', font=('Times New Roman', 10))
    l2 = Label(sales_statistics_selection_window, text='To date', font=('Times New Roman', 10))

    l1.place(x=80, y = 20)
    l2.place(x=80, y = 80)
    Button(sales_statistics_selection_window, text = "Get statistics for this period",
           command = sales_statistics).pack(pady = 10)

    return


def parse_date(d):
    i = 0
    ch = d[i]
    day = ''
    month = ''
    year = ''

    while ch != '/':
        day += ch
        i += 1
        ch = d[i]

    if len(day) < 2:
        day = '0' + day

    i += 1
    while ch != '/':
        month += ch
        i += 1
        ch = d[i]

    if len(month) < 2:
        month = '0' + month

    i += 1
    while ch != '/':
        year += ch
        i += 1
        ch = d[i]

    return (int(day), int(month), int(year))


def sales_statistics():
    sales_statistics_window = Tk()
    sales_statistics_window.geometry('1280x700+500+200')
    sales_statistics_window.title('Sales statistics')

    lst2 = []
    lst2.append(('ISBN', 'Name', 'Price', 'Publisher', 'Copies sold', 'Total revenue'))
    from_date = calfrom.get_date()
    to_date = calto.get_date()

    print(from_date)
    print(to_date)
    print('SELECT isbn, quantity from book_sales WHERE time_of_sale >= ' 
        + from_date.strftime("%Y-%m-%d") 
        + ' AND time_of_sale <= '
        + to_date.strftime("%Y-%m-%d"))
    cursor.execute(
        'SELECT isbn, quantity from book_sales WHERE time_of_sale >= ? AND time_of_sale <= ?', 
        (from_date.strftime("%Y-%m-%d"), to_date.strftime("%Y-%m-%d")))

    sales_rows = cursor.fetchall()

    print(sales_rows)

    ctr = 1
    stats = {}
    for i in sales_rows:
        cursor.execute("SELECT Book_Name, Price, Publisher FROM Book b WHERE Book_ISBN = ?", (i[0],))
        book_rows = cursor.fetchall()
        print(book_rows)
        if (len(book_rows) > 0):
            if not stats.has_key(i[0]):
                stats[i[0]] = {}
                stats[i[0]]['isbn'] = i[0]
                stats[i[0]]['name'] = book_rows[0][0]
                stats[i[0]]['price'] = book_rows[0][1]
                stats[i[0]]['quantity'] = i[1]
                stats[i[0]]['publisher'] = book_rows[0][2]
            else:
                stats[i[0]]['quantity'] += i[1]

    print(stats)
    for s in stats:
        lst2.append((
            s, 
            stats[s]['name'], 
            str(stats[s]['price']), 
            stats[s]['publisher'], 
            str(stats[s]['quantity']), 
            str(stats[s]['quantity'] * stats[s]['price'])))

    tbl = Table(sales_statistics_window, lst2)
    return


def print_date(d):
    print(d)

def show_not_in_stock_books():
    show_not_in_stock_window = Tk()
    show_not_in_stock_window.geometry('1280x700+500+200')
    show_not_in_stock_window.title('Not in stock books')

    lst2 = []
    lst2.append(('ISBN', 'Name', 'Price', 'Publisher', 'Query count'))

    cursor.execute("SELECT * FROM not_in_stock")
    not_in_stock_rows = cursor.fetchall()

    print(not_in_stock_rows)

    ctr = 1
    for s in not_in_stock_rows:
        cursor.execute("SELECT Book_Name, Price, Publisher FROM Book b WHERE Book_ISBN = ?", (s[0],))
        book_rows = cursor.fetchall()
        print(book_rows)
        if (len(book_rows) > 0):
            lst2.append((s[0], book_rows[0][0], 
                book_rows[0][1], book_rows[0][2], s[1]))

    tbl = Table(show_not_in_stock_window, lst2)
    return


def adminpage():
    global admpg
    user = str(ea1.get())
    pasw = str(ea2.get())

    cursor.execute('SELECT Login_ID,Password,Admin_ID,position FROM Admin')
    rows = cursor.fetchall()
    flag = 0

    for r in rows:
        if (user == r[0] and pasw == r[1]):
            session_type = r[3]
            print(session_type)
            print(r)
            var = Label(adm,
                        text="Login Successful",
                        font=("Login Successful", 18),
                        fg="green")
            var.place(x=150, y=400)
            adm.destroy()
            admpg = Tk()
            admpg.geometry('840x640+500+120')
            admpg.title('Administration Portal')
            var = 'Welcome  ' + r[2] + '!'
            l1 = Label(admpg,
                       text=var,
                       fg='black',
                       bg='Moccasin',
                       font=(var, 16))
            l1.place(x=200, y=50)

            b = Button(admpg,
                       text="Log Out",
                       fg='blue',
                       width=5,
                       height=1,
                       command=logoutadm)
            b.place(x=600, y=50)

            if session_type == 1 or session_type == 2 or session_type == 3:
                b2 = Button(admpg,
                            text="Add to inventory",
                            width=20,
                            height=3,
                            command=addinv)
                b2.place(x=100, y=100)

            if session_type == 2 or session_type == 3 or session_type == 1:
                b7 = Button(admpg,
                            text="Update inventory",
                            width=20,
                            height=3,
                            command=update_inventory)
                b7.place(x=340, y=100)
            
            if session_type == 2 or session_type == 1 or session_type == 3:
                b8 = Button(admpg,
                            text="Create Order",
                            width=20,
                            height=3,
                            command=porder)
                b8.place(x=100, y=250)

            if session_type == 2 or session_type == 3:
                b1 = Button(admpg,
                            text="View Sales Record",
                            width=20,
                            height=3,
                            command=vsrec)
                b1.place(x=340, y=250)
            
            if session_type == 2 or session_type == 3:
                b3 = Button(admpg,
                            text="View Purchase Record",
                            width=25,
                            height=3,
                            command=viewpur)
                b3.place(x=100, y=400)

            if session_type == 2 or session_type == 3:
                b4 = Button(admpg,
                            text="Add Purchase Record",
                            width=25,
                            height=3,
                            command=addpur)
                b4.place(x=340, y=400)

            if session_type == 2 or session_type == 3:
                b5 = Button(admpg,
                            text="Customer Requests",
                            width=20,
                            height=3,
                            command=request)
                b5.place(x=100, y=550)
            
            if session_type == 3:
                b6 = Button(admpg,
                            text="Books under threshold",
                            width=25,
                            height=3,
                            command=getbooksunderthreshold)
                b6.place(x=340, y=550)

            if session_type == 3:
                b9 = Button(admpg,
                            text="Sales Statistics",
                            width=25,
                            height=3,
                            command=show_sales_statistics)
                b9.place(x=580, y=400)

            if session_type == 3:
                b10 = Button(admpg,
                            text="Not in stock books",
                            width=25,
                            height=3,
                            command=show_not_in_stock_books)
                b10.place(x=580, y=250)

            b11 = Button(admpg,
                        text="Search books",
                        width=25,
                        height=3,
                        command=sbook)
            b11.place(x=580, y=100)
            
            flag = 1

    if (flag == 0):
        var = Label(adm,
                    text="Incorrect Username/Password",
                    font=("Incorrect Username/Password", 10),
                    fg="black")
        var.place(x=150, y=420)
    return


def spacesearch(x):
    if (x == 0):
        return 90
    elif x == 1:
        return 276
    elif x == 2:
        return 216
    elif x == 3:
        return 90
    elif x == 4:
        return 168
    elif x == 5:
        return 0


def spacesearch2(x):
    if (x == 0):
        return 110
    elif x == 1:
        return 275
    elif x == 2:
        return 210
    elif x == 3:
        return 300
    elif x == 4:
        return 180


def sbookfun():
    var1 = str(se1.get())
    #sql_command="SELECT * FROM Book WHERE Book_Name LIKE '%?%' "
    bname = '%' + var1 + '%'
    bname = bname.lower()

    var2 = str(se2.get())
    auth = '%' + var2 + '%'
    auth = auth.lower()

    var3 = str(se3.get())
    cat = '%' + var3 + '%'
    cat = cat.lower()

    cursor.execute(
        "SELECT * FROM Book WHERE LOWER(Book_Name) LIKE ? AND LOWER(Author) LIKE ? AND LOWER(Category) LIKE ?",
        (bname, auth, cat))

    rows = cursor.fetchall()

    searchres = Tk()
    searchres.geometry('1280x640+100+120')
    searchres.title('Search Results')

    srl = Label(searchres,
                text='Search Results:',
                font=('Search Results:', 14),
                bg='Moccasin',
                fg='black')
    srl.place(x=80, y=40)

    # l1 = Label(searchres, text='ISBN', font=('ISBN', 12))
    # l2 = Label(searchres, text='Name', font=('Name', 12))
    # l3 = Label(searchres, text='Author', font=('Author', 12))
    # l4 = Label(searchres, text='Price', font=('Price', 12))
    # l5 = Label(searchres, text='Category', font=('Category', 12))
    # l6 = Label(searchres, text='Publisher', font=('Publisher', 12))
    # l1.place(x=65, y=80)
    # l2.place(x=155, y=80)
    # l3.place(x=431, y=80)
    # l4.place(x=647, y=80)
    # l5.place(x=737, y=80)
    # l6.place(x=905, y=80)

    # col = 100
    # for r in rows:
    #     row = 65
    #     for x in range(len(r)):
    #         templabel = Label(searchres, text=r[x], font=(str(r[x]), 10))
    #         templabel.place(x=row, y=col)
    #         row = row + spacesearch(x)
    #     col = col + 20
    global search_results_list, books

    scroll_bar = Scrollbar(searchres)
      
    scroll_bar.pack(side = RIGHT,
                    fill = Y )
       
    search_results_list = Listbox(searchres, 
                     yscrollcommand = scroll_bar.set, 
                     width=60, selectmode=SINGLE,
                     height=5)

    for r in rows:
        search_results_list.insert(END, str(r[1]) + ' by ' + str(r[2]) + ' at INR ' + str(r[3]) + ' ISBN: ' + str(r[0]))

    search_results_list.pack( side = LEFT, fill = BOTH )
      
    scroll_bar.config( command = search_results_list.yview )

    books = []
    books.append(('ISBN', 'Name', 'Author', 'Price', 
        'Category', 'Publisher', 'Number of Copies', 'Rack Number'))
    for r in rows:
        books.append((r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[9] or 1))

    # tbl = Table(searchres, books, w=14)
    if len(rows) > 0:
        sb = Button(searchres,
                    text='View selected book',
                    width=25,
                    height=2,
                    command=view_book_window_fun)
        sb.place(x=800, y=350)

    return


def view_book_window_fun():
    global view_book_window
    view_book_window = Tk()
    view_book_window.geometry('1280x640+500+120')
    view_book_window.title('View Book')

    book = books[search_results_list.curselection()[0] + 1]
    isbn = book[0]

    lst = []
    lst.append(books[0])
    for b in books:
        if b[0] == isbn:
            lst.append(b)
            break

    print(book)

    if book[6] <= 0:
        cursor.execute('SELECT count(*) from `not_in_stock` WHERE ISBN = ?', (isbn,))
        count = cursor.fetchall()

        print(count)
        if count[0][0] > 0:
            cursor.execute('UPDATE `not_in_stock` SET count = ((SELECT count FROM `not_in_stock` WHERE ISBN = ?) + 1) WHERE ISBN = ?',
                   (isbn, isbn))
            connection.commit()
        else:
            cursor.execute('INSERT INTO `not_in_stock` VALUES (?,?)', (isbn, 1))
            connection.commit()

    tbl = Table(view_book_window, lst, w=14)


def sbook():
    global se1, se2, se3
    searchbk = Tk()
    searchbk.geometry('640x480+700+120')
    searchbk.title('Search Book')
    disp = Label(searchbk,
                 text='Enter keywords for search',
                 fg='black',
                 bg='Moccasin',
                 font=(12))
    disp.place(x=200, y=70)
    sl1 = Label(searchbk, text='Book Title:', font=('Book Title:', 10))
    se1 = Entry(searchbk, font=(10), bd=5)

    sl2 = Label(searchbk, text='Author:', font=('Author:', 10))
    se2 = Entry(searchbk, font=(10), bd=5)

    sl3 = Label(searchbk, text='Genre:', font=('Category:', 10))
    se3 = Entry(searchbk, font=(10), bd=5)

    sl1.place(x=100, y=140)
    se1.place(x=210, y=140)

    sl2.place(x=100, y=220)
    se2.place(x=210, y=220)

    sl3.place(x=100, y=300)
    se3.place(x=210, y=300)

    sb = Button(searchbk,
                text='Search Available Books',
                width=25,
                height=2,
                command=sbookfun)
    sb.place(x=210, y=350)

    sl4 = Label(searchbk,
                text="Can't find the book you're looking for?",
                font=("Can't find the book you're looking for?", 10),
                fg='blue')
    sb1 = Button(searchbk,
                 text='Click Here',
                 fg='blue',
                 width=10,
                 height=2,
                 command=cusreq)

    sl4.place(x=100, y=420)
    sb1.place(x=390, y=410)
    return


def add_supplier_to_db():
    confirmsup.destroy()
    isbn = str(supei1.get())
    name = str(supei2.get())
    auth = str(supei3.get())
    price = str(supei4.get())

    vis = Label(add_supplier_window, text='Supplier added successfully!', font=(8))
    vis.place(x=150, y=460)
    vis.after(3000, lambda: vis.place_forget())
    cursor.execute('INSERT INTO Supplier VALUES (?,?,?,?,?)',
                   ("sup" + str(random.randint(300, 10000)), isbn, name, auth, price))
    connection.commit()
    return


def destroy_confirm_add_supplier():
    confirmsup.destroy()


def confirm_add_supplier():
    global confirmsup
    confirmsup = Tk()
    confirmsup.geometry('500x150+300+120')
    confirmsup.title('Confirm Supplier')
    isbn = str(supei1.get())
    name = str(supei2.get())
    auth = str(supei3.get())
    price = str(supei4.get())

    if (isbn != '' and name != '' and auth != '' and price != ''):
        l1 = Label(confirmsup,
                   text='Are you sure you want to add this book?',
                   font=(10))
        b1 = Button(confirmsup, text='Yes', width=10, height=3, command=add_supplier_to_db)
        b2 = Button(confirmsup, text='No', width=10, height=3, command=destroy_confirm_add_supplier)

        l1.place(x=60, y=20)
        b1.place(x=80, y=80)
        b2.place(x=320, y=80)

    else:
        l10 = Label(add_supplier_window, text='Please enter all details', fg='red', font=(10))
        l10.place(x=150, y=440)
        confirmsup.destroy()
        l10.after(3000, lambda: l10.place_forget())


def add_supplier():
    global add_supplier_window
    add_supplier_window = Tk()
    add_supplier_window.geometry('720x600+500+120')
    add_supplier_window.title('Book Inventory')
    wel = Label(add_supplier_window, text='Add New Supplier', fg='black', bg='Moccasin', font=(16))
    global supei1, supei2, supei3, supei4
    supl1 = Label(add_supplier_window, text='Supplier Name:', font=(10))
    supl2 = Label(add_supplier_window, text='Publication:', font=(10))
    supl3 = Label(add_supplier_window, text='Email:', font=(10))
    supl4 = Label(add_supplier_window, text='Phone:', font=(10))

    supei1 = Entry(add_supplier_window, font=(10), bd=5)
    supei2 = Entry(add_supplier_window, font=(10), bd=5)
    supei3 = Entry(add_supplier_window, font=(10), bd=5)
    supei4 = Entry(add_supplier_window, font=(10), bd=5)

    b1 = Button(add_supplier_window, text='Add Supplier', width=20, height=3, command=confirm_add_supplier)
    wel.place(x=150, y=40)
    supl1.place(x=70, y=80)
    supei1.place(x=420, y=80)
    supl2.place(x=70, y=120)   
    supei2.place(x=420, y=120)
    supl3.place(x=70, y=160)
    supei3.place(x=420, y=160)
    supl4.place(x=70, y=200)
    supei4.place(x=420, y=200)
    b1.place(x=150, y=500)
    return


def search_supplier_access():
    var1 = str(sse2.get())
    bname = '%' + var1 + '%'
    bname = bname.lower()

    cursor.execute(
        "SELECT * FROM Supplier WHERE LOWER(Supplier_Name) LIKE ? OR LOWER(Publication) LIKE ? OR LOWER(Email_ID) LIKE ?",
        (bname, bname, bname))
    rows = cursor.fetchall()

    searchres = Tk()
    searchres.geometry('1280x640+100+120')
    searchres.title('Search Results')

    srl = Label(searchres,
                text='Search Results:',
                font=('Search Results:', 13),
                bg='Moccasin',
                fg='black')
    srl.place(x=80, y=40)

    l1 = Label(searchres, text='Supplier_ID', font=('ISBN', 12))
    l2 = Label(searchres, text='Supplier_Name', font=('Name', 12))
    l3 = Label(searchres, text='Publication', font=('Author', 12))
    l4 = Label(searchres, text='Email_ID', font=('Price', 12))
    l5 = Label(searchres, text='Phone_No', font=('Category', 12))
    
    l1.place(x=65, y=80)
    l2.place(x=175, y=80)
    l3.place(x=450, y=80)
    l4.place(x=660, y=80)
    l5.place(x=960, y=80)

    col = 100
    for r in rows:
        row = 65
        for x in range(len(r)):
            templabel = Label(searchres, text=r[x], font=(str(r[x]), 10))
            templabel.place(x=row, y=col)
            row = row + spacesearch2(x)
        col = col + 40

    return


def search_supplier():
    global sse2
    search_supplier_window = Tk()
    search_supplier_window.geometry('640x480+700+120')
    search_supplier_window.title('Search Suppliers')
    disp = Label(search_supplier_window,
                 text='Enter name or address of supplier',
                 fg='black',
                 bg='Moccasin',
                 font=(12))
    disp.place(x=200, y=70)
    sl2 = Label(search_supplier_window, text='Supplier: ', font=('Book Title:', 10))
    sse2 = Entry(search_supplier_window, font=(10), bd=5)

    # sl3 = Label(search_supplier_window, text='Category:', font=('Category:', 10))
    # se3 = Entry(search_supplier_window, font=(10), bd=5)

    # sl1.place(x=100, y=140)
    # se1.place(x=210, y=140)

    sl2.place(x=100, y=220)
    sse2.place(x=210, y=220)

    # sl3.place(x=100, y=300)
    # se3.place(x=210, y=300)

    sb = Button(search_supplier_window,
                text='Search Available Suppliers',
                width=25,
                height=2,
                command=search_supplier_access)
    sb.place(x=210, y=350)

    sl4 = Label(search_supplier_window,
                text="Can't find the supplier you're looking for?",
                font=("Can't find the book you're looking for?", 10),
                fg='blue')
    sb1 = Button(search_supplier_window,
                 text='Add one',
                 fg='blue',
                 width=10,
                 height=2,
                 command=add_supplier)

    sl4.place(x=100, y=420)
    sb1.place(x=390, y=410)
    return


def salord():
    salid = 'sal' + str(random.randint(1, 10000))
    cusid = str(epo2.get())
    invo = random.randint(800, 1000000)
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    isbn = str(epo1.get())

    print(cart_books)
    print((salid, cusid, invo, date, pri))

    cursor.execute('INSERT INTO Sales VALUES(?,?,?,?,?)',
                   (salid, cusid, invo, date, pri))
    connection.commit()

    print("here")
    for book in cart:
        cursor.execute('UPDATE Book SET number_of_copies=((SELECT number_of_copies FROM Book WHERE Book_ISBN=?)-1) WHERE Book_ISBN=?', (book, book))
        connection.commit()

    print("here 2")

    new_cart = {}
    print(cart_books)
    for j in cart_books:
        i = j[0]
        print(j)
        if not new_cart.has_key(i[0]):
            new_cart[i[0]] = {}
            new_cart[i[0]]['isbn'] = i[0]
            new_cart[i[0]]['name'] = i[1]
            new_cart[i[0]]['price'] = i[2]
            new_cart[i[0]]['quantity'] = 1
        else:
            new_cart[i[0]]['quantity'] += 1

    for item in new_cart:
        cursor.execute(
            'INSERT INTO book_sales (customer_id, isbn, sales_id, quantity, time_of_sale) VALUES(?,?,?,?,?)', 
            (cusid, isbn, salid, new_cart[isbn]['quantity'], date))
        connection.commit()

    check.destroy()
    confirmch.destroy()
    show = Label(pord, text='Order placed successfully', font=(8))
    show.place(x=100, y=320)
    show.after(3000, lambda: show.place_forget())

    show_sale_receipt(salid, new_cart)
    #cart=[]
    #pri=0
    return


def show_sale_receipt(sale_id, new_cart):
    sale_receipt_window = Tk()
    sale_receipt_window.geometry('1024x700+500+200')
    sale_receipt_window.title('Receipt')

    lst2 = []
    lst2.append(('Sr No.', 'Book', 'Price', 'Quantity', 'Total Amount'))

    print(new_cart)

    ctr = 1
    for book in new_cart:
        lst2.append((ctr, new_cart[book]['name'], 
            new_cart[book]['price'], 
            str(new_cart[book]['quantity']), 
            str(new_cart[book]['quantity']*new_cart[book]['price'])))
        ctr += 1

    tbl = Table(sale_receipt_window, lst2)
    return


def delbook(pri, book, p):
    #print book
    #print count
    cart.remove(book)
    pri = pri - p
    check.destroy()
    viewcart()
    return


def cartdest():
    check.destroy()
    return


def space(x):
    if x == 0:
        return 100
    elif x == 1:
        return 400
    else:
        return 50


def confchdest():
    confirmch.destroy()
    return


def confcheck():
    global confirmch
    confirmch = Tk()
    confirmch.geometry('500x150+500+120')
    confirmch.title('Confirm Checkout')

    l1 = Label(confirmch, text='Are you sure you want to checkout?', font=(10))
    b1 = Button(confirmch, text='Yes', width=10, height=3, command=salord)
    b2 = Button(confirmch, text='No', width=10, height=3, command=confchdest)

    l1.place(x=60, y=20)
    b1.place(x=80, y=80)
    b2.place(x=320, y=80)


def viewcart():
    global pri
    pri = 0
    global check
    check = Tk()
    check.geometry('840x700+500+200')
    check.title('View Bill')
    disp = Label(check,
                 text='This Bill:',
                 fg='black',
                 bg='Moccasin',
                 font=('Times New Roman', 20))
    disp.place(x=130, y=70)

    backButton = Button(check,
                        text='<-- Back',
                        width=6,
                        height=2,
                        command=cartdest)
    backButton.place(x=20, y=40)

    l1 = Label(check, text='ISBN', font=('ISBN', 15))
    l2 = Label(check, text='Title', font=('Title', 15))
    l3 = Label(check, text='Price', font=('Price', 15))

    l1.place(x=100, y=120)
    l2.place(x=200, y=120)
    l3.place(x=600, y=120)
    col = 170
    global cart_books
    cart_books = []
    for book in cart:
        cursor.execute(
            'SELECT Book_ISBN,Book_Name,Price from Book where Book_ISBN=?',
            (book, ))
        rows = cursor.fetchall()
        for r in rows:
            row = 100
            cart_books.append(rows)
            for x in range(len(r)):
                templabel = Label(check, text=r[x], font=(str(r[x]), 13))
                templabel.place(x=row, y=col)
                row = row + space(x)
            pri = pri + float(r[2])
        col = col + 40

    tempButton = Button(check,
                        text='Remove',
                        width=6,
                        height=1,
                        command=lambda: delbook(pri, book, r[2]))
    tempButton.place(x=row + 40, y=col - 40)

    l4 = Label(check, text='Bill Amount : ', font=('Bill Amount : ', 12))
    l5 = Label(check, text=str(pri), font=(str(pri), 12))
    l4.place(x=450, y=500)
    l5.place(x=600, y=500)
    checkButton = Button(check,
                         text='Checkout',
                         width=6,
                         height=1,
                         command=confcheck)
    checkButton.place(x=400, y=600)
    return


def addtocart():
    global cart
    #cart=[]
    isbn = str(epo1.get())
    username2 = str(epo2.get())
    if isbn == '' or username2 == '':
        l2 = Label(pord, text='Please enter the ISBN', font=(8))
        l2.place(x=100, y=320)
        l2.after(3000, lambda: l2.place_forget())
        return

    cursor.execute('SELECT * FROM Book where Book_ISBN=?', (isbn, ))
    rows = cursor.fetchall()
    if len(rows) == 0 or rows[0][6] <= 0:
        l1 = Label(pord, text='Book not in stock!', font=(8))
        l1.place(x=130, y=320)
        l1.after(3000, lambda: l1.place_forget())
    else:
        cart.append(isbn)
        print(cart)
        l3 = Label(pord, text='Added to Bill!', font=(8))
        l3.place(x=140, y=320)
        l3.after(3000, lambda: l3.place_forget())

    return


def porder():
    global pord
    pord = Tk()
    pord.geometry('640x360+500+200')
    pord.title('Order')
    disp = Label(pord, text='Book Order', fg='black', bg='Moccasin', font=(12))
    disp.place(x=130, y=70)

    l1 = Label(pord, text='ISBN:', font=(10))
    l3 = Label(pord, text='Customer username:', font=(10))
    l2 = Label(pord,
               text='Want to know ISBN of book?',
               font=('Want to know ISBN of Book?', 10))

    global epo1, epo2
    epo1 = Entry(pord, font=(10), bd=5, width=10)
    epo2 = Entry(pord, font=(10), bd=5, width=10)

    b1 = Button(pord,
                text='Click here',
                fg='blue',
                width=6,
                height=1,
                command=sbook)
    b2 = Button(pord,
                text='Add To Bill',
                width=14,
                height=2,
                command=addtocart)
    b3 = Button(pord, text='View Items in Bill', width=14, height=2, command=viewcart)

    l1.place(x=40, y=120)
    epo1.place(x=250, y=120)
    l3.place(x=40, y=180)
    epo2.place(x=250, y=180)
    l2.place(x=40, y=240)
    b1.place(x=230, y=240)
    b2.place(x=40, y=290)
    b3.place(x=250, y=290)
    return


def viewcomporder():

    cursor.execute(
        "SELECT Sales_ID,Invoice_no,S_Date,Bill_Amount FROM Sales WHERE Customer_ID=?",
        (userc, ))
    rows = cursor.fetchall()

    searchres = Tk()
    searchres.geometry('840x640+100+120')
    searchres.title('Completed Orders')

    srl = Label(searchres,
                text='Completed Orders:',
                font=('Completed Orders:', 13),
                bg='Moccasin',
                fg='black')
    srl.place(x=80, y=40)

    l1 = Label(searchres, text='Sales ID', font=('Sales ID', 10))
    l2 = Label(searchres, text='Invoice Number', font=('Invoice Number', 10))
    l3 = Label(searchres, text='Sales Date', font=('Sales Date', 10))
    l4 = Label(searchres, text='Bill Amount', font=('Bill Amount', 10))

    l1.place(x=40, y=80)
    l2.place(x=240, y=80)
    l3.place(x=440, y=80)
    l4.place(x=640, y=80)

    col = 100
    for r in rows:
        row = 40
        for x in r:
            templabel = Label(searchres, text=x, font=(str(x), 8))
            templabel.place(x=row, y=col)
            row = row + 200
        col = col + 15

    return


def request():
    requests = Tk()
    requests.geometry('640x480+700+120')
    requests.title('Book Requests')
    cursor.execute("SELECT * FROM Request")
    rows = cursor.fetchall()

    
    
    srl = Label(requests,
                text='Customer Book Requests:',
                font=('Customer Book Requests:', 13),
                bg='Moccasin',
                fg='black')
    srl.place(x=80, y=40)

    l1 = Label(requests, text='Book Name', font=('Sales ID', 10))
    l2 = Label(requests, text='Author', font=('Customer', 10))

    l1.place(x=60, y=80)
    l2.place(x=235, y=80)

    col = 100
    for r in rows:
        row = 60
        for x in r:
            templabel = Label(requests, text=x, font=(str(x), 8))
            templabel.place(x=row, y=col)
            row = row + 175
        col = col + 15

    return


def logoutcust():
    cuspg.destroy()
    return


def custpage():
    global userc
    global cuspg
    #global stvar
    userc = str(ec1.get())
    paswc = str(ec2.get())

    cursor.execute('SELECT Customer_ID,Password,Customer_Name FROM Customer')
    rows = cursor.fetchall()
    flag = 0
    for r in rows:
        if (userc == r[0] and paswc == r[1]):
            var = Label(cust,
                        text="Login Successful",
                        font=("Login Successful", 18),
                        fg="green")
            var.place(x=150, y=400)
            cust.destroy()
            cuspg = Tk()
            cuspg.geometry('640x480+500+120')
            cuspg.title('CustPage')
            var = 'WELCOME ' + r[2] + '!'

            l1 = Label(cuspg,
                       text=var,
                       fg='black',
                       bg='Moccasin',
                       font=(var, 16))
            l1.place(x=160, y=50)

            b = Button(cuspg,
                       text="Log Out",
                       fg='blue',
                       width=5,
                       height=1,
                       command=logoutcust)
            b.place(x=540, y=50)

            b1 = Button(cuspg,
                        text="Search Books",
                        width=20,
                        height=3,
                        command=sbook)
            b1.place(x=100, y=150)

            # b2 = Button(cuspg,
            #             text="Place Order",
            #             width=20,
            #             height=3,
            #             command=porder)
            # b2.place(x=400, y=150)

            b3 = Button(cuspg,
                        text="View Completed Orders",
                        width=20,
                        height=3,
                        command=viewcomporder)
            b3.place(x=100, y=300)

            b4 = Button(cuspg,
                        text="Request",
                        width=20,
                        height=3,
                        command=cusreq)
            b4.place(x=400, y=150)
            flag = 1
    if (flag == 0):
        var = Label(cust,
                    text="Incorrect Username/Password",
                    font=("Incorrect Username/Password", 10),
                    fg="black")
        var.place(x=150, y=400)


def admin():
    global adm
    adm = Tk()
    adm.geometry('480x480+500+120')
    adm.title('Admin')

    disa1 = Label(adm, text='Admin ID', font=('Admin ID', 10))
    disa2 = Label(adm, text='Password', font=('Password', 10))
    ba1 = Button(adm, text='Login', width=5, height=2, command=adminpage)
    disa3 = Label(adm,
                  text='Welcome Admin',
                  fg='black',
                  bg='Moccasin',
                  font=('Welcome Admin', 16))
    global ea1
    ea1 = Entry(adm, font=(10), bd=5)
    global ea2
    ea2 = Entry(adm, font=(10), bd=5, show='*')
    disa3.place(x=150, y=100)
    disa1.place(x=70, y=230)
    disa2.place(x=70, y=290)
    ba1.place(x=200, y=370)
    ea1.place(x=150, y=230)
    ea2.place(x=150, y=290)
    return


def customer():
    global cust
    cust = Tk()
    cust.geometry('480x480+500+120')
    cust.title('Customer')
    global ec1
    global ec2
    disc1 = Label(cust, text='Customer ID', font=('Customer ID', 10))
    disc2 = Label(cust, text='Password', font=('Password', 10))
    bc1 = Button(cust, text='Login', width=5, height=2, command=custpage)
    disc3 = Label(cust,
                  text='Welcome Customer',
                  fg='black',
                  bg='Moccasin',
                  font=('Welcome Admin', 16))
    ec1 = Entry(cust, font=(10), bd=5)
    ec2 = Entry(cust, font=(10), bd=5, show='*')
    disc3.place(x=150, y=100)
    disc1.place(x=70, y=230)
    disc2.place(x=70, y=290)
    bc1.place(x=200, y=370)
    ec1.place(x=180, y=230)
    ec2.place(x=180, y=290)
    return


def sinpg():
    cusid = str(es1.get())
    pasw1 = str(es2.get())
    pasw2 = str(es21.get())
    cname = str(es3.get())
    city = str(es4.get())
    stre = str(es5.get())
    stat = str(es6.get())
    phno = str(es7.get())

    if (pasw1 != pasw2):
        vis = Label(sig, text='  Passwords  dont  match', font=(8))
        vis.place(x=150, y=460)
        vis.after(3000, lambda: vis.place_forget())
    elif (cusid == '' or pasw1 == '' or pasw2 == '' or cname == ''
          or city == '' or stre == '' or stat == '' or phno == ''):
        l1 = Label(sig, text='Please fill all details', font=(8), fg='red')
        l1.place(x=150, y=460)
        l1.after(3000, lambda: l1.place_forget())
    else:
        vis = Label(sig, text='Account Created successfully', font=(8))
        vis.place(x=150, y=460)
        vis.after(3000, lambda: vis.place_forget())
        cursor.execute('INSERT INTO Customer VALUES (?,?,?,?,?,?,?)',
                       (cusid, pasw1, cname, city, stre, stat, phno))
        connection.commit()
    return


def signup():
    global sig
    sig = Tk()
    sig.geometry('480x480+500+120')
    sig.title('Customer')
    wel = Label(sig,
                text='Customer SignUp',
                fg='black',
                bg='Moccasin',
                font=(16))
    global es1, es2, es21, es3, es4, es5, es6, es7
    l1 = Label(sig, text='Customer ID', font=(10))
    l2 = Label(sig, text='Password', font=(10))
    l21 = Label(sig, text='Re-enter Password', font=(10))
    l3 = Label(sig, text='Name', font=(10))
    l4 = Label(sig, text='City', font=(10))
    l5 = Label(sig, text='Street', font=(10))
    l6 = Label(sig, text='State', font=(10))
    l7 = Label(sig, text='Phone No', font=(10))

    es1 = Entry(sig, font=(10), bd=5)
    es2 = Entry(sig, font=(10), bd=5, show='*')
    es21 = Entry(sig, font=(10), bd=5, show='*')
    es3 = Entry(sig, font=(10), bd=5)
    es4 = Entry(sig, font=(10), bd=5)
    es5 = Entry(sig, font=(10), bd=5)
    es6 = Entry(sig, font=(10), bd=5)
    es7 = Entry(sig, font=(10), bd=5)

    b1 = Button(sig, text='Sign Up', width=20, height=3, command=sinpg)
    wel.place(x=150, y=40)
    l1.place(x=70, y=80)
    es1.place(x=230, y=80)
    l2.place(x=70, y=120)
    es2.place(x=230, y=120)
    l21.place(x=70, y=160)
    es21.place(x=230, y=160)
    l3.place(x=70, y=200)
    es3.place(x=230, y=200)
    l4.place(x=70, y=240)
    es4.place(x=230, y=240)
    l5.place(x=70, y=280)
    es5.place(x=230, y=280)
    l6.place(x=70, y=320)
    es6.place(x=230, y=320)
    l7.place(x=70, y=360)
    es7.place(x=230, y=360)
    b1.place(x=150, y=400)
    return


global gui
gui = Tk()

gui.geometry('1080x700+200+0')
gui.title('BOOKSHOP AUTOMATION SYSTEM')
image = Image.open('academic-complex.jpg')
photo_image = ImageTk.PhotoImage(image)
label = Label(gui, image=photo_image)
label.pack()

deli = 120
svar = StringVar()
labl = Label(gui,
             textvariable=svar,
             height=3,
             width=200,
             bg='Moccasin',
             fg='Black',
             font=('Times New Roman', 15))


'''
def shif():
    shif.msg = shif.msg[1:] + shif.msg[0]
    svar.set(shif.msg)
    gui.after(deli, shif)


shif.msg = '                           BOOKSHOP AUTOMATION SYSTEM                           '
shif()
'''

# labl.place(x=10, y=140)

dis= Label(gui, 
    text='BOOKSHOP AUTOMATION SYSTEM', 
    height=3, 
    width=92,
    bg='Moccasin',
    fg='Black',
    font=('Times New Roman', 18))
disp = Label(gui, text='New User?', bg='Moccasin', font=('Times New Roman', 15))
b1 = Button(gui,
            text='Admin Login',
            width=25,
            height=3,
            command=admin,
            font=('Times New Roman', 18), 
            bg='lightgreen', borderwidth = 0)
b2 = Button(gui,
            text='Customer Login',
            width=25,
            height=3,
            command=customer,
            font=('Times New Roman', 18), 
            bg='lightgreen', borderwidth = 0)
b3 = Button(gui,
            text='Customer Signup',
            width=25,
            height=3,
            command=signup,
            font=('Times New Roman', 18), 
            bg='lightgreen', borderwidth = 0)
dis.place(x=0,y=140)
b1.place(x=100, y=530)
b2.place(x=630, y=530)
b3.place(x=360, y=360)
disp.place(x=483, y=325)

gui.mainloop()

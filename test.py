from dbfread import DBF

# !/usr/bin/env python
# -*- coding: utf8 -*-

import dbf

table = dbf.Table("BNKSEEK.DBF", codepage='cp866')
# table.open('read-only')
table.open()

# print(table.field_names)

lt = []
dt = {}

for i in table:
    dt['real'] = i['real']
    dt['pzn'] = i['pzn']
    dt['uer'] = i['uer']
    dt['rgn'] = i['rgn']
    dt['ind'] = i['ind']
    dt['tnp'] = i['tnp']
    dt['nnp'] = i['nnp']
    dt['adr'] = i['adr']
    dt['rkc'] = i['rkc']
    dt['namep'] = i['namep']
    dt['newnum'] = i['newnum']
    dt['telef'] = i['telef']
    dt['regn'] = i['regn']
    dt['okpo'] = i['okpo']
    dt['dt_izm'] = i['dt_izm']
    dt['ksnp'] = i['ksnp']
    dt['date_in'] = i['date_in']
    dt['date_ch'] = i['date_ch']
    # print(i['vkey'])
    lt.append(dt)

# print(lt)

from tkinter import *
import backend


def get_selected_row(event):
    try:
        index = list1.curselection()[0]
        global selected_tuple
        selected_tuple = list1.get(index)
        # print(selected_tuple)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[0])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[1])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[2])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[3])
        e5.delete(0, END)
        e5.insert(END, selected_tuple[4])
        e6.delete(0, END)
        e6.insert(END, selected_tuple[5])
        e7.delete(0, END)
        e7.insert(END, selected_tuple[6])
        e8.delete(0, END)
        e8.insert(END, selected_tuple[7])
        e9.delete(0, END)
        e9.insert(END, selected_tuple[8])
        e10.delete(0, END)
        e10.insert(END, selected_tuple[9])
        e11.delete(0, END)
        e11.insert(END, selected_tuple[10])
        e12.delete(0, END)
        e12.insert(END, selected_tuple[11])
        e13.delete(0, END)
        e13.insert(END, selected_tuple[12])
        e14.delete(0, END)
        e14.insert(END, selected_tuple[13])
        e15.delete(0, END)
        e15.insert(END, selected_tuple[14])
        e16.delete(0, END)
        e16.insert(END, selected_tuple[15])
        e17.delete(0, END)
        e17.insert(END, selected_tuple[16])
        e18.delete(0, END)
        e18.insert(END, selected_tuple[17])
    except IndexError:
        pass

dt = {}
def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)
    '''e2.delete(0, END)
    for row in backend.view_pzn():
        e2.insert(0, row[0])
        dt['pzn'] = row[1]
        dt['pzn_name'] = row[0]'''


def search_command():
    list1.delete(0, END)
    for row in backend.search(newnum_text.get(), pzn_text.get(), rgn_text.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(real_text.get(), pzn_text.get(), uer_text.get(), rgn_text.get(), ind_text.get(),
                   tnp_text.get(), nnp_text.get(), adr_text.get(), rkc_text.get(), namep_text.get(), newnum_text.get(),
                   telef_text.get(), regn_text.get(), okpo_text.get(), dt_izm_text.get(), ksnp_text.get(),
                   date_in_text.get(), date_ch_text.get())
    list1.delete(0, END)
    list1.insert(END, (real_text.get(), pzn_text.get(), uer_text.get(), rgn_text.get(), ind_text.get(),
                   tnp_text.get(), nnp_text.get(), adr_text.get(), rkc_text.get(), namep_text.get(), newnum_text.get(),
                   telef_text.get(), regn_text.get(), okpo_text.get(), dt_izm_text.get(), ksnp_text.get(),
                   date_in_text.get(), date_ch_text.get()))


def delete_command():
    backend.delete(selected_tuple[10])
    view_command()


def update_command():
    backend.update(real_text.get(), pzn_text.get(), uer_text.get(), rgn_text.get(), ind_text.get(),
                       tnp_text.get(), nnp_text.get(), adr_text.get(), rkc_text.get(), namep_text.get(),
                       telef_text.get(), regn_text.get(), okpo_text.get(), dt_izm_text.get(), ksnp_text.get(),
                       date_in_text.get(), date_ch_text.get(), newnum_text.get())
    view_command()


# GUI
window = Tk()
window.wm_title("Bank Work")
l1 = Label(window, text="REAL")
l1.grid(row=0, column=0, rowspan=1)

l2 = Label(window, text="PZN")
l2.grid(row=0, column=2, rowspan=1)

l3 = Label(window, text="UER")
l3.grid(row=1, column=0)

l4 = Label(window, text="RGN")
l4.grid(row=1, column=2)

l5 = Label(window, text="IND")
l5.grid(row=2, column=0)

l6 = Label(window, text="TNP")
l6.grid(row=2, column=2)

l7 = Label(window, text="NNP")
l7.grid(row=3, column=0)

l8 = Label(window, text="ADR")
l8.grid(row=3, column=2)

l9 = Label(window, text="RKC")
l9.grid(row=4, column=0)

l10 = Label(window, text="NAMEP")
l10.grid(row=4, column=2)

l11 = Label(window, text="NEWNUM")
l11.grid(row=5, column=0)

l12 = Label(window, text="TELEF")
l12.grid(row=5, column=2)

l13 = Label(window, text="REGN")
l13.grid(row=6, column=0)

l14 = Label(window, text="OKPO")
l14.grid(row=6, column=2)

l15 = Label(window, text="DT_IZM")
l15.grid(row=7, column=0)

l16 = Label(window, text="KSNP")
l16.grid(row=7, column=2)

l17 = Label(window, text="DATE_IN")
l17.grid(row=8, column=0)

l18 = Label(window, text="DATE_CH")
l18.grid(row=8, column=2)

real_text = StringVar()
e1 = Entry(window, textvariable=real_text)
e1.grid(row=0, column=1)

pzn_text = StringVar()
e2 = Entry(window, textvariable=pzn_text)
e2.grid(row=0, column=3)

'''e2 = Listbox(window, height=6, width=25)
e2.grid(row=0, column=3)

e2.bind('<<ListboxSelect>>', get_selected_row)'''

uer_text = StringVar()
e3 = Entry(window, textvariable=uer_text)
e3.grid(row=1, column=1)

rgn_text = StringVar()
e4 = Entry(window, textvariable=rgn_text)
e4.grid(row=1, column=3)

ind_text = StringVar()
e5 = Entry(window, textvariable=ind_text)
e5.grid(row=2, column=1)

tnp_text = StringVar()
e6 = Entry(window, textvariable=tnp_text)
e6.grid(row=2, column=3)

nnp_text = StringVar()
e7 = Entry(window, textvariable=nnp_text)
e7.grid(row=3, column=1)

adr_text = StringVar()
e8 = Entry(window, textvariable=adr_text)
e8.grid(row=3, column=3)

rkc_text = StringVar()
e9 = Entry(window, textvariable=rkc_text)
e9.grid(row=4, column=1)

namep_text = StringVar()
e10 = Entry(window, textvariable=namep_text)
e10.grid(row=4, column=3)

newnum_text = StringVar()
e11 = Entry(window, textvariable=newnum_text)
e11.grid(row=5, column=1)

telef_text = StringVar()
e12 = Entry(window, textvariable=telef_text)
e12.grid(row=5, column=3)

regn_text = StringVar()
e13 = Entry(window, textvariable=regn_text)
e13.grid(row=6, column=1)

okpo_text = StringVar()
e14 = Entry(window, textvariable=okpo_text)
e14.grid(row=6, column=3)

dt_izm_text = StringVar()
e15 = Entry(window, textvariable=dt_izm_text)
e15.grid(row=7, column=1)

ksnp_text = StringVar()
e16 = Entry(window, textvariable=ksnp_text)
e16.grid(row=7, column=3)

date_in_text = StringVar()
e17 = Entry(window, textvariable=date_in_text)
e17.grid(row=8, column=1)

date_ch_text = StringVar()
e18 = Entry(window, textvariable=date_ch_text)
e18.grid(row=8, column=3)

list1 = Listbox(window, height=6, width=95)
list1.grid(row=25, column=0, rowspan=6, columnspan=2)

list1.bind('<<ListboxSelect>>', get_selected_row)


sb1 = Scrollbar(window)
sb1.grid(row=25, column=2, rowspan=6)
list1.config(yscrollcommand=sb1.set)
sb1.config(command=list1.yview)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=5)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=5)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=5)

b4 = Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=5, column=5)

b5 = Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=5)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=5)
window.mainloop()

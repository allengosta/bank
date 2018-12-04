import sqlite3

import dbf

table = dbf.Table("BNKSEEK.DBF", codepage='cp866')
# table.open('read-only')
table.open()

print(table.field_names)

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


def connect():
    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bank (real TEXT, "
                "pzn INTEGER, uer INTEGER, rgn INTEGER, ind INTEGER, tnp INTEGER , nnp TEXT, adr TEXT,"
                "rkc INTEGER, namep TEXT, newnum INTEGER PRIMARY KEY, telef TEXT, regn TEXT, okpo INTEGER,"
                "dt_izm DATE, ksnp INTEGER, date_in DATE, date_ch DATE )")
    conn.commit()
    '''for i in table:
        cur.execute("INSERT INTO bank VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (i['real'],
                                                                                       i['pzn'], i['uer'],
                                                                                       i['rgn'], i['ind'],
                                                                                       i['tnp'], i['nnp'],
                                                                                       i['adr'], i['rkc'],
                                                                                       i['namep'], i['newnum'],
                                                                                       i['telef'], i['regn'],
                                                                                       i['okpo'], i['dt_izm'],
                                                                                       i['ksnp'], i['date_in'],
                                                                                       i['date_ch']))
        conn.commit()'''
    conn.close()

def insert(real, pzn, uer, rgn, ind, tnp, nnp, adr, rkc, namep, telef, regn, okpo, dt_izm, ksnp, date_in, date_ch, newnum):
    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    #the NULL parameter is for the auto-incremented id
    cur.execute("INSERT INTO bank VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (real, pzn, uer, rgn, ind, tnp, nnp,
                                                                                 adr, rkc, namep, newnum,
                                      telef, regn, okpo, dt_izm, ksnp, date_in, date_ch))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("SELECT b.real, p.name, u.uername, r.name, b.ind, t.shortname, b.nnp, b.adr, b.rkc, b.namep, "
                "b.newnum, b.telef, b.regn, b.okpo, b.dt_izm, b.ksnp, b.date_in, b.date_ch "
                "FROM bank b join reg_tb r on b.rgn=r.rgn join pzn_tb p on p.pzn=b.pzn "
                "join tnp_tb t on t.tnp=b.tnp join uer_tb u on u.uer=b.uer")
    rows = cur.fetchall()
    conn.close()
    return rows


def view_pzn():
    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("SELECT p.name from pzn_tb p")
    rows = cur.fetchall()
    conn.close()
    return rows

def view_reg():
    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("SELECT p.name from reg_tb p")
    rows = cur.fetchall()
    conn.close()
    return rows

def view_uer():
    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("SELECT p.uername from uer_tb p")
    rows = cur.fetchall()
    conn.close()
    return rows


def view_tnp():
    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("SELECT p.shortname from tnp_tb p")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(newnum="", pzn="", rgn=""):
    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bank WHERE newnum = ? OR pzn = ? OR rgn = ? ", (newnum, pzn, rgn))
    rows = cur.fetchall()
    print(rows)
    conn.close()
    return rows

def delete(newnum):
    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM bank WHERE newnum = ?", (newnum,))
    conn.commit()
    conn.close()

def update(real, pzn, uer, rgn, ind, tnp, nnp, adr, rkc, namep, telef, regn, okpo, dt_izm, ksnp, date_in, date_ch, newnum):
    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("UPDATE bank SET real = ?, pzn = ?, uer = ?, rgn = ?,"
                "ind = ?, tnp = ?, nnp = ?, adr = ?, rkc = ?, namep = ?,"
                "telef = ?, regn = ?, okpo = ?, dt_izm = ?, ksnp = ?,"
                "date_in = ?, date_ch = ?"
                " WHERE newnum = ?", (real, pzn, uer, rgn, ind, tnp, nnp, adr, rkc, namep,
                                      telef, regn, okpo, dt_izm, ksnp, date_in, date_ch, newnum))
    conn.commit()
    conn.close()

connect()
#insert("another novel", "James W.", 2017, 1234)
#update(2, title = "new book", author= "DH", year= 2005, isbn= 5555)
# print(view())
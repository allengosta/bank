import sqlite3

import dbf

table = dbf.Table("UER.DBF", codepage='cp866')
# table.open('read-only')
table.open()

print(table.field_names)

lt = []
dt = {}

for i in table:
    print(i)
    lt.append(dt)


def connect():
    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS uer_tb (vkey TEXT, "
                "uer INTEGER, uername TEXT)")
    conn.commit()
    for i in table:
        cur.execute("INSERT INTO uer_tb VALUES(?,?,?)", (i['vkey'], i['uer'],
                                                             i['uername']))
        conn.commit()
    conn.close()
    
    
connect()
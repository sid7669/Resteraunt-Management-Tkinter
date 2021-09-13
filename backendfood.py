import sqlite3

def connect():
    con=sqlite3.connect("account.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS list (r integer, d integer,f integer ,s integer , k integer , c integer ,m integer, p integer , ch integer )")
    con.commit()
    con.close()

def insert(r,d,f,s,k,c,m,p,ch):
    con=sqlite3.connect("account.db")
    cur=con.cursor()
    cur.execute("INSERT INTO list VALUES(?,?,?,?,?,?,?,?,?)",(r,d,f,s,k,c,m,p,ch))
    con.commit()
    con.close()

def view():
    con=sqlite3.connect("account.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM list")
    rows= cur.fetchall()
    con.close()
    return rows

def delete(r):
    con=sqlite3.connect("account.db")
    cur=con.cursor()
    cur.execute("DELETE FROM list WHERE r=?",(r,))
    con.commit()
    con.close()


connect()
#insert(9,8,7,6,4,1,0,0,0)
#delete(9)
#print(view())

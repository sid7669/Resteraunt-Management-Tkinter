import sqlite3

def connect():
    con=sqlite3.connect("account.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS list (l integer, c integer,fa integer ,sh integer , j integer , ra integer ,ma integer, ba integer , cd integer )")
    con.commit()
    con.close()

def insert(l,c,fa,sh,j,ra,ma,ba,cd):
   con=sqlite3.connect("account.db")
   cur=con.cursor()
   cur.execute("INSERT INTO list VALUES(?,?,?,?,?,?,?,?,?)",(l,c,fa,sh,j,ra,ma,ba,cd))
   con.commit()
   con.close()

def view():
    con=sqlite3.connect("account.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM list")
    rows= cur.fetchall()
    con.close()
    return rows

def delete(l):
    con=sqlite3.connect("account.db")
    cur=con.cursor()
    cur.execute("DELETE FROM list WHERE l=?",(l,))
    con.commit()
    con.close()


connect()
# insert(9,8,7,6,4,1,0,0,0)
# delete(9,)
# print(view())

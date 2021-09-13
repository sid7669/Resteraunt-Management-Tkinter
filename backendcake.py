import sqlite3
import pandas as p

def connect():
    con=sqlite3.connect("account.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS list (o integer, a integer,kk integer ,v integer , bn integer , br integer ,pi integer, co integer , bf integer )")
    con.commit()
    df=p.read_sql_query("SELECT * from list",con)
#    print(df.head())
    con.close()




def insert(o,a,kk,v,bn,br,pi,co,bf):
   con=sqlite3.connect("account.db")
   cur=con.cursor()
   cur.execute("INSERT INTO list VALUES(?,?,?,?,?,?,?,?,?)",(o,a,kk,v,bn,br,pi,co,bf))
   con.commit()
   con.close()

def view():
    con=sqlite3.connect("account.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM list")
    rows= cur.fetchall()
    con.close()
    return rows

def delete(o):
    con=sqlite3.connect("account.db")
    cur=con.cursor()
    cur.execute("DELETE FROM list WHERE r=?",(o,))
    con.commit()
    con.close()


connect()
# insert(19,18,17,16,14,11,10,10,10)
# delete(9,)
#print(view())

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pyautogui
import random
import time;
import tempfile
import os
import datetime
import tkinter.messagebox



window=Toplevel()
window.title("Record System")



def receipt():
    txt.insert(END,CustmId.get(),Firstname.get(),Phonenumber.get(),mem.get())




def save():
    f= filedialog.askopenfilename()
    p=txt.get("1.0","end-1c")
    file=open("Record_Holder.txt" ,"a+")
    if f is None:
        return
    file.write(p)

    file.close()

def refresh():
    Firstname.set("")
    mem.set("")
    Phonenumber.set("")
    CustmId.set("")
    iDate.set(time.strftime("%d/%m/%y"))
    iTime.set(time.strftime("%H:%M:%S"))

def exit():
    exit=tkinter.messagebox.askyesno("Record System","Yes for confirm")
    if exit>0:
        window.destroy()


def order():
    import menu

iDate=StringVar()
iDate.set(time.strftime("%d/%m/%y"))
iTime=StringVar()
iTime.set(time.strftime("%H:%M:%S"))
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()

Firstname=StringVar()
mem= StringVar()
Phonenumber=StringVar()
Phonenumber.set("+91")
CustmId=StringVar()



mnframe=Frame(window,bg="green",width=136,height=100)
mnframe.grid()

Top=Frame(mnframe,bd=5,relief="ridge")
Top.pack(side="top")

lb=Label(Top,width=36,font=("arial",39,"bold"),text="Customer Record System",justify="center")
lb.grid(padx=50)

fb2=LabelFrame(mnframe,width=59,bd=5,height=400,font=("arial",15,"bold"),text="Customer Information",foreground="white",relief="ridge",bg="blue")
fb2.pack(padx=3,side="top")

fb3=LabelFrame(mnframe,width=150,bd=5,height=200,font=("arial",15,"bold"),text="Details",foreground="white",relief="ridge",bg="blue")
fb3.pack(padx=38,side="top")


lb2=Label(fb2,width=15,font=("arial",15,"bold"),text="Customer ID",foreground="white",bg="blue",bd="7")
lb2.grid(row=0,column=0,sticky="w")
lb2txt=Entry(fb2,width=15,font=("arial",15,"bold"),textvariable= CustmId, bd="7",state="disabled")
lb2txt.grid(row=0,column=1,sticky="w")

lb2=Label(fb2,width=15,font=("arial",15,"bold"),text="Customer Name",foreground="white",bg="blue",bd="7")
lb2.grid(row=1,column=0,sticky="w")
lb2txt=Entry(fb2,width=15,font=("arial",15,"bold"),textvariable= Firstname,bd="7")
lb2txt.grid(row=1,column=1,sticky="w")
lb2=Label(fb2,width=20,font=("arial",15,"bold"),text="Date",foreground="white",bg="blue",bd="7")
lb2.grid(row=0,column=2,sticky="w")
lb2txt=Entry(fb2,width=15,font=("arial",15,"bold"),textvariable=mem,bd="7")
lb2txt.grid(row=1,column=5,sticky="w")
lb2txt=Entry(fb2,width=15,font=("arial",15,"bold"),textvariable=iDate,bd="7",state="disabled")
lb2txt.grid(row=0,column=3,sticky="w")
lb3=Label(fb2,width=20,font=("arial",15,"bold"),text="Time",foreground="white",bg="blue",bd="7")
lb3.grid(row=1,column=2,sticky="ne")
lb3txt=Entry(fb2,width=15,font=("arial",15,"bold"),textvariable=iTime,bd="7",state="disabled")
lb3txt.grid(row=1,column=3,sticky="ne")




lb2=Label(fb2,width=20,font=("arial",15,"bold"),text="Phone Number",foreground="white",bg="blue",bd="7")
lb2.grid(row=0,column=4,sticky="w")
lb2txt=Entry(fb2,width=15,font=("arial",15,"bold"),textvariable= Phonenumber,bd="7")
lb2txt.grid(row=0,column=5,sticky="w")

lb2=Label(fb2,width=20,font=("arial",15,"bold"),text="Accomodation",foreground="white",bg="blue",bd="7")
lb2.grid(row=1,column=4,sticky="w")




txt=Text(fb3,width=113,height=10,font=("arial",15,"bold"))
txt.grid(row=0,column=0,columnspan=7)
txt.insert(END,"Custmor Id\t\t  Customer Name\t\t  Accomodation\t\t  Phone Number\t\t  Date\t\t  Time\n")


btn=Button(fb3,bd=5,font=("arial",15,"bold"),text="RECEIPT",width=7)
btn.grid(row=1,column=0,pady=10)
btn=Button(fb3,bd=5,font=("arial",15,"bold"),text="SAVE",width=7,command=save)
btn.grid(row=1,column=1,pady=10)
btn=Button(fb3,bd=5,font=("arial",15,"bold"),text="REFRESH",width=7,command=refresh)
btn.grid(row=1,column=2,pady=10)
btn=Button(fb3,bd=5,font=("arial",15,"bold"),text="ORDER",width=7,command=order)
btn.grid(row=1,column=3,pady=10)
btn=Button(fb3,bd=5,font=("arial",15,"bold"),text="EXIT",width=7,command=exit)
btn.grid(row=1,column=4,pady=10)


window.mainloop()

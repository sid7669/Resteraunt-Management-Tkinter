from tkinter import  *
from PIL import Image,ImageTk
import tkinter.messagebox



window=Tk()
#path="colosseum.jpg"
#img=ImageTk.PhotoImage(Image.open(path))


def login():
    if (e.get()=="Siddharth" and q.get()=="qwerty") or (e.get()=="Satyam" and q.get()=="123456"):
        import recordd
    elif(e.get()=="Siddharth" and q.get()=="123456") or (e.get()=="Satyam" and q.get()=="qwerty"):
        login=tkinter.messagebox.askretrycancel("Login Error","Invalid User ID Password")
    else:
        login=tkinter.messagebox.askretrycancel("Login Error","User ID not found")










f=Frame(window)
f.grid()

f2=Frame(f)
f2.pack(side="left",)
lb2=Label(f2,text="Siddharth")
lb2.pack(padx=50)

f3=Frame(f)
f3.pack(side="right")
lb3=Label(f3,text="is")
lb3.pack(padx=50)

f4=Frame(f)
f4.pack(side="top")
lb4=Label(f4,text="my")
lb4.pack(padx=50)

f5=Frame(f)
f5.pack(side="top")
lb5=Label(f5,text="User Name")
lb5.grid(row=0,column=0)
e=StringVar()
user=Entry(f5,textvariable=e)
user.grid(row=0,column=1)
lb6=Label(f5,text="Password")
lb6.grid(row=1,column=0)
q=StringVar()
pas=Entry(f5,textvariable=q,show="*")
pas.grid(row=1,column=1)

f6=Frame(f)
f6.pack(side="top")
b7=Button(f6,text="LOGIN",width=6,command=login)
b7.grid(row=0,column=0,padx=5)
b8=Button(f6,text="RESET",width=6)
b8.grid(row=0,column=1,padx=5)
b9=Button(f6,text="EXIT",width=6)
b9.grid(row=0,column=2,padx=5)





window.mainloop()

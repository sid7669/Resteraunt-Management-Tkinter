from tkinter import *

window=Tk()

var_c=IntVar()
F3=Frame(window,width=250,height=550,relief="ridge",border=3,bg="brown")
F3.grid(row=2,column=6,rowspan=14,columnspan=5)

var_c=IntVar()
l_c=Entry(window,textvariable=var_c,width="26")
l_c.grid(row=3,column=6,columnspan=5)

b1=Button(window,text="7",width=6,height=2,border=10)
b1.grid(row=4,column=6)

b2=Button(window,text="8",width=6,height=2,border=10)
b2.grid(row=4,column=7)

b3=Button(window,text="9",width=6,height=2,border=10)
b3.grid(row=4,column=8)

b4=Button(window,text="+",width=6,height=2,border=10)
b4.grid(row=4,column=9)

b5=Button(window,text="4",width=6,height=2,border=10)
b5.grid(row=5,column=6)

b6=Button(window,text="5",width=6,height=2,border=10)
b6.grid(row=5,column=7)

b7=Button(window,text="6",width=6,height=2,border=10)
b7.grid(row=5,column=8)

b8=Button(window,text="-",width=6,height=2,border=10)
b8.grid(row=5,column=9)

b9=Button(window,text="1",width=6,height=2,border=10)
b9.grid(row=6,column=6)

b10=Button(window,text="2",width=6,height=2,border=10)
b10.grid(row=6,column=7)

b11=Button(window,text="3",width=6,height=2,border=10)
b11.grid(row=6,column=8)

b12=Button(window,text="*",width=6,height=2,border=10)
b12.grid(row=6,column=9)

b13=Button(window,text="=",width=6,height=2,border=10)
b13.grid(row=7,column=6)

b14=Button(window,text="Clear",width=6,height=2,border=10)
b14.grid(row=7,column=7)

b15=Button(window,text="0",width=6,height=2,border=10)
b15.grid(row=7,column=8)

b16=Button(window,text="/",width=6,height=2,border=10)
b16.grid(row=7,column=9)

#list
t1=Text(window,width=30,height=16)
t1.grid(row=8,column=6,rowspan=7,columnspan=5)


b17=Button(window,text="Receipt",width=6,height=2,border=10)
b17.grid(row=15,column=6)

b18=Button(window,text="Save",width=6,height=2,border=10)
b18.grid(row=15,column=7)

b19=Button(window,text="Send",width=6,height=2,border=10)
b19.grid(row=15,column=8)

b20=Button(window,text="Reset",width=6,height=2,border=10)
b20.grid(row=15,column=9)






window.mainloop()

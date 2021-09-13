from tkinter import *
import backendcake
import backenddrink
import backendfood
from tkinter import filedialog



#Food backend start
def add_r():
    def a():
        aa=StringVar()
        aa=s1.get()+"           \t"+str(e1_value.get())+"      \t"+str(e1_value.get()*20)+"\n"
        return aa
    backendfood.insert(e1_value.get(),e4_value.get(),e7_value.get(),e10_value.get(),e13_value.get(),e16_value.get(),e19_value.get(),e22_value.get(),e25_value.get())
    t1.insert(END,a())

def add_d():
    def b():
        bb=StringVar()
        bb=s4.get()+"           \t"+str(e4_value.get())+"      \t"+str(e4_value.get()*240)+"\n"
        return bb
    backendfood.insert(e1_value.get(),e4_value.get(),e7_value.get(),e10_value.get(),e13_value.get(),e16_value.get(),e19_value.get(),e22_value.get(),e25_value.get())
    t1.insert(END,b())

def add_f():
    def c():
        cc=StringVar()
        cc=s7.get()+"           \t"+str(e7_value.get())+"      \t"+str(e7_value.get()*380)+"\n"
        return cc
    backendfood.insert(e1_value.get(),e4_value.get(),e7_value.get(),e10_value.get(),e13_value.get(),e16_value.get(),e19_value.get(),e22_value.get(),e25_value.get())
    t1.insert(END,c())

def add_s():
    def d():
        dd=StringVar()
        dd=s10.get()+"          \t"+str(e10_value.get())+"      \t"+str(e10_value.get()*210)+"\n"
        return dd
    backendfood.insert(e1_value.get(),e4_value.get(),e7_value.get(),e10_value.get(),e13_value.get(),e16_value.get(),e19_value.get(),e22_value.get(),e25_value.get())
    t1.insert(END,d())

def add_k():
    def e():
        ee=StringVar()
        ee=s13.get()+"          \t"+str(e13_value.get())+"      \t"+str(e13_value.get()*240)+"\n"
        return ee
    backendfood.insert(e1_value.get(),e4_value.get(),e7_value.get(),e10_value.get(),e13_value.get(),e16_value.get(),e19_value.get(),e22_value.get(),e25_value.get())
    t1.insert(END,e())

def add_c():
    def f():
        ff=StringVar()
        ff=s16.get()+"         \t"+str(e16_value.get())+"      \t"+str(e16_value.get()*150)+"\n"
        return ff
    backendfood.insert(e1_value.get(),e4_value.get(),e7_value.get(),e10_value.get(),e13_value.get(),e16_value.get(),e19_value.get(),e22_value.get(),e25_value.get())
    t1.insert(END,f())

def add_m():
    def g():
        gg=StringVar()
        gg=s19.get()+"         \t"+str(e19_value.get())+"      \t"+str(e19_value.get()*320)+"\n"
        return gg
    backendfood.insert(e1_value.get(),e4_value.get(),e7_value.get(),e10_value.get(),e13_value.get(),e16_value.get(),e19_value.get(),e22_value.get(),e25_value.get())
    t1.insert(END,g())

def add_p():
    def h():
        hh=StringVar()
        hh=s22.get()+"         \t"+str(e22_value.get())+"      \t"+str(e22_value.get()*300)+"\n"
        return hh
    backendfood.insert(e1_value.get(),e4_value.get(),e7_value.get(),e10_value.get(),e13_value.get(),e16_value.get(),e19_value.get(),e22_value.get(),e25_value.get())
    t1.insert(END,h())

def add_ch():
    def i():
        ii=StringVar()
        ii=s25.get()+"        \t"+str(e25_value.get())+"      \t"+str(e25_value.get()*310)+"\n"
        return ii
    backendfood.insert(e1_value.get(),e4_value.get(),e7_value.get(),e10_value.get(),e13_value.get(),e16_value.get(),e19_value.get(),e22_value.get(),e25_value.get())
    t1.insert(END,i())

def add_food():
    sum=(e1_value.get()*20)+(e4_value.get()*240)+(e7_value.get()*380)+(e10_value.get()*210)+(e13_value.get()*240)+(e16_value.get()*150)+(e19_value.get()*320)+(e22_value.get()*300)+(e25_value.get()*310)
    list_food.insert(END,(sum))
    return sum
#end

#Drink backend start
def add_l():
    def j():
        jj=StringVar()
        jj=s2.get()+"          \t"+str(e2_value.get())+"      \t"+str(e2_value.get()*60)+"\n"
        return jj
    backenddrink.insert(e2_value.get(),e5_value.get(),e8_value.get(),e11_value.get(),e14_value.get(),e17_value.get(),e20_value.get(),e23_value.get(),e26_value.get())
    t1.insert(END,j())

def add_cof():
    def k():
        kk=StringVar()
        kk=s5.get()+"         \t"+str(e5_value.get())+"      \t"+str(e5_value.get()*70)+"\n"
        return kk
    backenddrink.insert(e2_value.get(),e5_value.get(),e8_value.get(),e11_value.get(),e14_value.get(),e17_value.get(),e20_value.get(),e23_value.get(),e26_value.get())
    t1.insert(END,k())

def add_fa():
    def l():
        ll=StringVar()
        ll=s8.get()+"         \t"+str(e8_value.get())+"      \t"+str(e8_value.get()*60)+"\n"
        return ll
    backenddrink.insert(e2_value.get(),e5_value.get(),e8_value.get(),e11_value.get(),e14_value.get(),e17_value.get(),e20_value.get(),e23_value.get(),e26_value.get())
    t1.insert(END,l())

def add_sh():
    def m():
        mm=StringVar()
        mm=s11.get()+"       \t"+str(e11_value.get())+"      \t"+str(e11_value.get()*50)+"\n"
        return mm
    backenddrink.insert(e2_value.get(),e5_value.get(),e8_value.get(),e11_value.get(),e14_value.get(),e17_value.get(),e20_value.get(),e23_value.get(),e26_value.get())
    t1.insert(END,m())

def add_j():
    def n():
        nn=StringVar()
        nn=s14.get()+"      \t"+str(e14_value.get())+"      \t"+str(e14_value.get()*50)+"\n"
        return nn
    backenddrink.insert(e2_value.get(),e5_value.get(),e8_value.get(),e11_value.get(),e14_value.get(),e17_value.get(),e20_value.get(),e23_value.get(),e26_value.get())
    t1.insert(END,n())

def add_ra():
    def o():
        oo=StringVar()
        oo=s17.get()+"         \t"+str(e17_value.get())+"      \t"+str(e17_value.get()*70)+"\n"
        return oo
    backenddrink.insert(e2_value.get(),e5_value.get(),e8_value.get(),e11_value.get(),e14_value.get(),e17_value.get(),e20_value.get(),e23_value.get(),e26_value.get())
    t1.insert(END,o())

def add_ma():
    def p():
        pp=StringVar()
        pp=s20.get()+"    \t"+str(e20_value.get())+"      \t"+str(e20_value.get()*40)+"\n"
        return pp
    backenddrink.insert(e2_value.get(),e5_value.get(),e8_value.get(),e11_value.get(),e14_value.get(),e17_value.get(),e20_value.get(),e23_value.get(),e26_value.get())
    t1.insert(END,p())

def add_ba():
    def q():
        qq=StringVar()
        qq=s23.get()+"     \t"+str(e16_value.get())+"      \t"+str(e16_value.get()*110)+"\n"
        return qq
    backenddrink.insert(e2_value.get(),e5_value.get(),e8_value.get(),e11_value.get(),e14_value.get(),e17_value.get(),e20_value.get(),e23_value.get(),e26_value.get())
    t1.insert(END,q())

def add_cd():
    def r():
        rr=StringVar()
        rr=s26.get()+"    \t"+str(e26_value.get())+"      \t"+str(e26_value.get()*60)+"\n"
        return rr
    backenddrink.insert(e2_value.get(),e5_value.get(),e8_value.get(),e11_value.get(),e14_value.get(),e17_value.get(),e20_value.get(),e23_value.get(),e26_value.get())
    t1.insert(END,r())

def add_drink():
    sum2=e2_value.get()*60+e5_value.get()*70+e8_value.get()*60+e11_value.get()*50+e14_value.get()*50+e17_value.get()*70+e20_value.get()*40+e23_value.get()*110+e26_value.get()*60
    list_drink.insert(END,(sum2))
    return sum2
#end

#cake backend start
def add_o():
    def s():
        ss=StringVar()
        ss=s3.get()+"           \t"+str(e3_value.get())+"      \t"+str(e3_value.get()*470)+"\n"
        return ss
    backendcake.insert(e3_value.get(),e6_value.get(),e9_value.get(),e12_value.get(),e15_value.get(),e18_value.get(),e21_value.get(),e24_value.get(),e27_value.get())
    t1.insert(END,s())

def add_a():
    def t():
        tt=StringVar()
        tt=s6.get()+"          \t"+str(e6_value.get())+"      \t"+str(e6_value.get()*400)+"\n"
        return tt
    backendcake.insert(e3_value.get(),e6_value.get(),e9_value.get(),e12_value.get(),e15_value.get(),e18_value.get(),e21_value.get(),e24_value.get(),e27_value.get())
    t1.insert(END,t())

def add_kk():
    def u():
        uu=StringVar()
        uu=s9.get()+"         \t"+str(e9_value.get())+"      \t"+str(e9_value.get()*380)+"\n"
        return uu
    backendcake.insert(e3_value.get(),e6_value.get(),e9_value.get(),e12_value.get(),e15_value.get(),e18_value.get(),e21_value.get(),e24_value.get(),e27_value.get())
    t1.insert(END,u())

def add_v():
    def v():
        vv=StringVar()
        vv=s12.get()+"        \t"+str(e12_value.get())+"      \t"+str(e12_value.get()*380)+"\n"
        return vv
    backendcake.insert(e3_value.get(),e6_value.get(),e9_value.get(),e12_value.get(),e15_value.get(),e18_value.get(),e21_value.get(),e24_value.get(),e27_value.get())
    t1.insert(END,v())

def add_bn():
    def w():
        ww=StringVar()
        ww=s15.get()+"         \t"+str(e15_value.get())+"      \t"+str(e15_value.get()*400)+"\n"
        return ww
    backendcake.insert(e3_value.get(),e6_value.get(),e9_value.get(),e12_value.get(),e15_value.get(),e18_value.get(),e21_value.get(),e24_value.get(),e27_value.get())
    t1.insert(END,w())

def add_br():
    def x():
        xx=StringVar()
        xx=s18.get()+"       \t"+str(e18_value.get())+"      \t"+str(e18_value.get()*250)+"\n"
        return xx
    backendcake.insert(e3_value.get(),e6_value.get(),e9_value.get(),e12_value.get(),e15_value.get(),e18_value.get(),e21_value.get(),e24_value.get(),e27_value.get())
    t1.insert(END,x())

def add_pi():
    def y():
        yy=StringVar()
        yy=s21.get()+"      \t"+str(e21_value.get())+"      \t"+str(e21_value.get()*350)+"\n"
        return yy
    backendcake.insert(e3_value.get(),e6_value.get(),e9_value.get(),e12_value.get(),e15_value.get(),e18_value.get(),e21_value.get(),e24_value.get(),e27_value.get())
    t1.insert(END,y())

def add_co():
    def z():
        zz=StringVar()
        zz=s24.get()+"\t"+str(e24_value.get())+"\n"
        return zz
    backendcake.insert(e3_value.get(),e6_value.get(),e9_value.get(),e12_value.get(),e15_value.get(),e18_value.get(),e21_value.get(),e24_value.get(),e27_value.get())
    t1.insert(END,z())

def add_bf():
    def ab():
        abc=StringVar()
        abc=s27.get()+"   \t"+str(e27_value.get())+"      \t"+str(e27_value.get()*500)+"\n"
        return abc
    backendcake.insert(e3_value.get(),e6_value.get(),e9_value.get(),e12_value.get(),e15_value.get(),e18_value.get(),e21_value.get(),e24_value.get(),e27_value.get())
    t1.insert(END,ab())

def add_cake():
    sum3=e3_value.get()*470+e6_value.get()*400+e9_value.get()*380+e12_value.get()*380+e15_value.get()*400+e18_value.get()*250+e21_value.get()*350+e24_value.get()*360+e27_value.get()*500
    list_cake.insert(END,(sum3))
    return sum3
#end

#sub Total
def sub_total():
    sum4=add_food()+add_cake()+add_drink()
    list_sub.insert(END,(sum4))
    return sum4

#service charges
def serv_charge():
    tax=sub_total()*(0.12)
    list_tax.insert(END,(tax))
    return tax

#Total
def total():
    tot=sub_total()+serv_charge()
    list_tot.insert(END,(tot))
    t1.insert(END,sub_total())
    t1.insert(END,serv_charge())
    t1.insert(END,tot)
    return tot





def saveas():
    #f= filedialog.askopenfilename()
    p=t1.get("1.0","end-1c")
    file=open("Record_Holder.txt" ,"a+")
    #if f is None:
    #    return
    file.write(p)

    file.close()

def print():
    q=t1.get("1.0","end-1c")
    filename=tempfile.mktemp(".txt")
    open(filename,"w").write(q)
    os.startfile(filename,"print")




#graphical interface
window=Toplevel()


#start
F=Frame(window,width=1350,height=50,relief="ridge",border=3,bg="brown")
F.grid(row=0,column=0,rowspan=2,columnspan=10)

L=Label(window,text="Resteraunt Account Management",bg="brown",foreground="yellow")
L.grid(row=0,column=0,rowspan=1,columnspan=10)
#end

#list

l1=Label(window,text="Food",foreground="brown")
l1.grid(row=2,column=0)

f1=Frame(window,width=350,height=370,relief="ridge",border=3)
f1.grid(row=3,column=0,rowspan=9,columnspan=2)


l2=Label(window,text="Drinks",foreground="brown")
l2.grid(row=2,column=2)

f2=Frame(window,width=400,height=370,relief="ridge",border=3)
f2.grid(row=3,column=2,rowspan=9,columnspan=2)

l3=Label(window,text="Cakes",foreground="brown")
l3.grid(row=2,column=4)

f3=Frame(window,width=350,height=370,relief="ridge",border=3)
f3.grid(row=3,column=4,rowspan=9,columnspan=2)

#foodlist
space=""
add=IntVar()

s1=StringVar()
s1.set("Roti")
var=IntVar()
c1=Checkbutton(window,text="Roti",variable=var,width=13,anchor="w",command=add_r)
c1.grid(row=3,column=0)

e1_value=IntVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=3,column=1)

s2=StringVar()
s2.set("Lassi")
var2=IntVar()
c2=Checkbutton(window,text="Lassi",variable=var2,width=13,anchor="w",command=add_l)
c2.grid(row=3,column=2)

e2_value=IntVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=3,column=3)

s3=StringVar()
s3.set("Oreo")
var3=IntVar()
c3=Checkbutton(window,text="Oreo",variable=var3,width=13,anchor="w",command=add_o)
c3.grid(row=3,column=4)

e3_value=IntVar()
e3=Entry(window,textvariable=e3_value)
e3.grid(row=3,column=5)

s4=StringVar()
s4.set("Daal")
var4=IntVar()
c4=Checkbutton(window,text="Daal",variable=var4,width=13,anchor="w",command=add_d)
c4.grid(row=4,column=0)

e4_value=IntVar()
e4=Entry(window,textvariable=e4_value)
e4.grid(row=4,column=1)

s5=StringVar()
s5.set("Coffee")
var5=IntVar()
c5=Checkbutton(window,text="Coffee",variable=var5,width=13,anchor="w",command=add_cof)
c5.grid(row=4,column=2)

e5_value=IntVar()
e5=Entry(window,textvariable=e5_value)
e5.grid(row=4,column=3)

s6=StringVar()
s6.set("Apple")
var6=IntVar()
c6=Checkbutton(window,text="Apple",variable=var6,width=13,anchor="w",command=add_a)
c6.grid(row=4,column=4)

e6_value=IntVar()
e6=Entry(window,textvariable=e6_value)
e6.grid(row=4,column=5)

s7=StringVar()
s7.set("Fish")
var7=IntVar()
c7=Checkbutton(window,text="Fish",variable=var7,width=13,anchor="w",command=add_f)
c7.grid(row=5,column=0)


e7_value=IntVar()
e7=Entry(window,textvariable=e7_value)
e7.grid(row=5,column=1)

s8=StringVar()
s8.set("Faluda")
var8=IntVar()
c8=Checkbutton(window,text="Faluda",variable=var8,width=13,anchor="w",command=add_fa)
c8.grid(row=5,column=2)

e8_value=IntVar()
e8=Entry(window,textvariable=e8_value)
e8.grid(row=5,column=3)

s9=StringVar()
s9.set("KitKat")
var9=IntVar()
c9=Checkbutton(window,text="KitKat",variable=var9,width=13,anchor="w",command=add_kk)
c9.grid(row=5,column=4)

e9_value=IntVar()
e9=Entry(window,textvariable=e9_value)
e9.grid(row=5,column=5)

s10=StringVar()
s10.set("Sabji")
var10=IntVar()
c10=Checkbutton(window,text="Sabji",variable=var10,width=13,anchor="w",command=add_s)
c10.grid(row=6,column=0,)

e10_value=IntVar()
e10=Entry(window,textvariable=e10_value)
e10.grid(row=6,column=1)

s11=StringVar()
s11.set("Shikanji")
var11=IntVar()
c11=Checkbutton(window,text="Shikanji",variable=var11,width=13,anchor="w",command=add_sh)
c11.grid(row=6,column=2)

e11_value=IntVar()
e11=Entry(window,textvariable=e11_value)
e11.grid(row=6,column=3)

s12=StringVar()
s12.set("Vanilla")
var12=IntVar()
c12=Checkbutton(window,text="Vanilla",variable=var12,width=13,anchor="w",command=add_v)
c12.grid(row=6,column=4)

e12_value=IntVar()
e12=Entry(window,textvariable=e12_value)
e12.grid(row=6,column=5)

s13=StringVar()
s13.set("Kebab")
var13=IntVar()
c13=Checkbutton(window,text="Kebab",variable=var13,width=13,anchor="w",command=add_k)
c13.grid(row=7,column=0)

e13_value=IntVar()
e13=Entry(window,textvariable=e13_value)
e13.grid(row=7,column=1)

s14=StringVar()
s14.set("Jal-Jeera")
var14=IntVar()
c14=Checkbutton(window,text="Jal-Jeera",variable=var14,width=13,anchor="w",command=add_j)
c14.grid(row=7,column=2)

e14_value=IntVar()
e14=Entry(window,textvariable=e14_value)
e14.grid(row=7,column=3)

s15=StringVar()
s15.set("Banana")
var15=IntVar()
c15=Checkbutton(window,text="Banana",variable=var15,width=13,anchor="w",command=add_bn)
c15.grid(row=7,column=4)

e15_value=IntVar()
e15=Entry(window,textvariable=e15_value)
e15.grid(row=7,column=5)

s16=StringVar()
s16.set("Chawal")
var16=IntVar()
c16=Checkbutton(window,text="Chawal",variable=var16,width=13,anchor="w",command=add_c)
c16.grid(row=8,column=0)

e16_value=IntVar()
e16=Entry(window,textvariable=e16_value)
e16.grid(row=8,column=1)

s17=StringVar()
s17.set("Mojito")
var17=IntVar()
c17=Checkbutton(window,text="Mojito",variable=var17,width=13,anchor="w",command=add_ra)
c17.grid(row=8,column=2)

e17_value=IntVar()
e17=Entry(window,textvariable=e17_value)
e17.grid(row=8,column=3)

s18=StringVar()
s18.set("Brownie")
var18=IntVar()
c18=Checkbutton(window,text="Brownie",variable=var18,width=13,anchor="w",command=add_br)
c18.grid(row=8,column=4)

e18_value=IntVar()
e18=Entry(window,textvariable=e18_value)
e18.grid(row=8,column=5)

s19=StringVar()
s19.set("Mutton")
var19=IntVar()
c19=Checkbutton(window,text="Mutton",variable=var19,width=13,anchor="w",command=add_m)
c19.grid(row=9,column=0)

e19_value=IntVar()
e19=Entry(window,textvariable=e19_value)
e19.grid(row=9,column=1)

s20=StringVar()
s20.set("Masala Chai")
var20=IntVar()
c20=Checkbutton(window,text="Masala Chai",variable=var20,width=13,anchor="w",command=add_ma)
c20.grid(row=9,column=2)

e20_value=IntVar()
e20=Entry(window,textvariable=e20_value)
e20.grid(row=9,column=3)

s21=StringVar()
s21.set("Pineapple")
var21=IntVar()
c21=Checkbutton(window,text="Pineapple",variable=var21,width=13,anchor="w",command=add_pi)
c21.grid(row=9,column=4)

e21_value=IntVar()
e21=Entry(window,textvariable=e21_value)
e21.grid(row=9,column=5)

s22=StringVar()
s22.set("Paneer")
var22=IntVar()
c22=Checkbutton(window,text="Paneer",variable=var22,width=13,anchor="w",command=add_p)
c22.grid(row=10,column=0)

e22_value=IntVar()
e22=Entry(window,textvariable=e22_value)
e22.grid(row=10,column=1)

s23=StringVar()
s23.set("Milk Shake")
var23=IntVar()
c23=Checkbutton(window,text="Milk Shake",variable=var23,width=13,anchor="w",command=add_ba)
c23.grid(row=10,column=2)

e23_value=IntVar()
e23=Entry(window,textvariable=e23_value)
e23.grid(row=10,column=3)

s24=StringVar()
s24.set("Chocolate")
var24=IntVar()
c24=Checkbutton(window,text="Chocolate",variable=var24,width=13,anchor="w",command=add_co)
c24.grid(row=10,column=4)

e24_value=IntVar()
e24=Entry(window,textvariable=e24_value)
e24.grid(row=10,column=5)

s25=StringVar()
s25.set("Chicken")
var25=IntVar()
c25=Checkbutton(window,text="Chicken",variable=var25,width=13,anchor="w",command=add_ch)
c25.grid(row=11,column=0)

e25_value=IntVar()
e25=Entry(window,textvariable=e25_value)
e25.grid(row=11,column=1)

s26=StringVar()
s26.set("Cold Drinks")
var26=IntVar()
c26=Checkbutton(window,text="Cold Drinks",variable=var26,width=13,anchor="w",command=add_cd)
c26.grid(row=11,column=2)

e26_value=IntVar()
e26=Entry(window,textvariable=e26_value)
e26.grid(row=11,column=3)

s27=StringVar()
s27.set("Black Forest")
var27=IntVar()
c27=Checkbutton(window,text="Black Forest",variable=var27,width=13,anchor="w",command=add_bf)
c27.grid(row=11,column=4)

e27_value=IntVar()
e27=Entry(window,textvariable=e27_value)
e27.grid(row=11,column=5)

#bottom part

F2=Frame(window,width=1100,height=150,relief="ridge",border=3,bg="brown")
F2.grid(row=13,column=0,rowspan=4,columnspan=6)

l4=Button(window,text="Cost of Drinks",bg="brown",border=10,width=13,command=add_drink)
l4.grid(row=13,column=0,columnspan=1)
list_drink=Listbox(window,width=20,height=1,border=5,relief="sunken")
list_drink.grid(row=13,column=2)

l5=Button(window,text="Cost of Cake",bg="brown",border=10,width=13,command=add_cake)
l5.grid(row=14,column=0,columnspan=1)
list_cake=Listbox(window,width=20,height=1,border=5,relief="sunken")
list_cake.grid(row=14,column=2)

l6=Button(window,text="Cost of Foods",border=10,width=13,command=add_food)
l6.grid(row=15,column=0,columnspan=1)
list_food=Listbox(window,width=20,height=1,border=5,relief="sunken")
list_food.grid(row=15,column=2)


l7=Button(window,text="Sub Total",bg="brown",border=10,width=13,command=sub_total)
l7.grid(row=13,column=3,columnspan=1)
list_sub=Listbox(window,width=20,height=1,border=5,relief="sunken")
list_sub.grid(row=13,column=5)


l8=Button(window,text="Service Charge",bg="brown",border=10,width=13,command=serv_charge)
l8.grid(row=14,column=3,columnspan=1)
list_tax=Listbox(window,width=20,height=1,border=5,relief="sunken")
list_tax.grid(row=14,column=5)

l9=Button(window,text="Total Cost",bg="brown",border=10,width=13,command=total)
l9.grid(row=15,column=3,columnspan=1)
list_tot=Listbox(window,width=20,height=1,border=5,relief="sunken")
list_tot.grid(row=15,column=5)



#list
t1=Text(window,width=31,height=30,bd=5,relief="sunken")
t1.grid(row=3,column=6,rowspan=11,columnspan=5)
sb1=Scrollbar(window)
sb1.grid(row=8,column=9,rowspan=7)
t1.configure(yscrollcommand=sb1.set)
sb1.configure(command=t1.yview)

t1.insert(END,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
t1.insert(END,"ITEM\t    QUANTITY\t PRICE\n")
t1.insert(END,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

b17=Button(window,text="Receipt",width=6,height=2,border=10)
b17.grid(row=15,column=6)

b18=Button(window,text="Save",width=6,height=2,border=10,command=saveas)
b18.grid(row=15,column=7)

b19=Button(window,text="Bill",width=6,height=2,border=10,command=print)
b19.grid(row=15,column=8)

b20=Button(window,text="Reset",width=6,height=2,border=10)
b20.grid(row=15,column=9)




window.mainloop()

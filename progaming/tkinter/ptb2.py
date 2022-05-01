
from tkinter import *
from math import *

def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringHSC.set("")
    stringKQ.set("")

def giaiAction():
    a = float(stringHSA.get())
    b = float(stringHSB.get())
    c = float(stringHSC.get())

    delta = b*b - 4*(a*c)
    if delta < 0:
        stringKQ.set("Vo nghiem")
    elif delta == 0:
        stringKQ.set("x1 = x2 = " + str(-b / (2*a)))
    else:
        stringKQ.set("x1 = " + str((-b + sqrt(delta))/(2*a))+ "va x2 = " + str((-b-sqrt(delta))/(2*a)))




root = Tk()

stringHSA = StringVar()
stringHSB = StringVar()
stringHSC = StringVar()
stringKQ = StringVar()

root.title("http://dinhhuanchu.com")
root.resizable(width=True, height=True)
root.minsize(height=160,width=250)

Label(root,text="Giai phuong trinh bac 2",fg="red",font=("tohama",16),justify=CENTER).grid(row=0,columnspan=2)

Label(root,text="He so a:").grid(row=1,column=0)
Entry(root,width=30,textvariable=stringHSA).grid(row=1,column=1)

Label(root,text="He so b:").grid(row=2,column=0)
Entry(root,width=30,textvariable=stringHSB).grid(row=2,column=1)

Label(root,text="He so c:").grid(row=3,column=0)
Entry(root,width=30,textvariable=stringHSC).grid(row=3,column=1)

frameButton = Frame()
Button(frameButton,text="Giai",command=giaiAction).pack(side=LEFT)
Button(frameButton,text="Tiep",command=tiepAction).pack(side=LEFT)
Button(frameButton,text="Thoat",command=quit).pack(side=LEFT)
frameButton.grid(row=4,column=1)

Label(root,text="Ket Qua:").grid(row=5,column=0)
Entry(root,width=30,textvariable=stringKQ).grid(row=5,column=1)

root.mainloop()
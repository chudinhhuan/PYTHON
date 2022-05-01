from tkinter import *


def congAction():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a+b)
def truAction():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a-b)

def nhanAction():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a*b)

def chiaAction():
    a = float(stringA.get())
    b = float(stringB.get())
    stringKQ.set(a/b)




root = Tk()

stringA = StringVar()
stringB = StringVar()
stringKQ = StringVar()

root.minsize(height=160,width=220)
root.resizable(width=True,height=True)
Label(root,text="Cộng Trừ Nhân Chia",fg="blue",font=("tahoma",16)).grid(row=0,columnspan=3)

frameButton = Frame(root)
Button(frameButton,text="Cộng",command=congAction).pack(side=TOP,fill=X)
Button(frameButton,text="Trừ",command=truAction).pack(side=TOP,fill=X)
Button(frameButton,text="Nhân",command=nhanAction).pack(side=TOP,fill=X)
Button(frameButton,text="Chia",command=chiaAction).pack(side=TOP,fill=X)
frameButton.grid(row=1,column=0,rowspan=4)

Label(root,text="So a:").grid(row=1,column=1)
Entry(root,width=15,textvariable=stringA).grid(row=1,column=2)

Label(root,text="So b:").grid(row=2,column=1)
Entry(root,width=15,textvariable=stringB).grid(row=2,column=2)

Label(root,text="Ket qua:").grid(row=3,column=1)
Entry(root,width=15,textvariable=stringKQ).grid(row=3,column=2)

Button(root,text="Thoat",command=quit).grid(row=4,column=2)




mainloop()
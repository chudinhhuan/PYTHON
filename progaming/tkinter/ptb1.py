from tkinter import *

def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringKQ.set("")

def giaiAction():
    a = float(stringHSA.get())
    b = float(stringHSB.get())

    if a == 0  and b == 0:
        stringKQ.set("Vo nghiem")
    elif a == 0 and b!= 0:
        stringKQ.set("Vo nghiem")
    else:
        stringKQ.set("x = "+ str(-b/a))
root = Tk()

stringHSA = StringVar()
stringHSB = StringVar()
stringKQ = StringVar()


root.title("http://phuongtrinhbac1.com")
root.resizable(height=True,width=True)
root.minsize(height=120,width=200)

Label(root,text="Phuong trinh bac 1",fg="red",font=("tahoma",16),justify=CENTER).grid(row=0,columnspan=2)

Label(root,text="He so a:").grid(row=1,column=0)
Entry(root,width=30,textvariable=stringHSA).grid(row=1,column=1)

Label(root,text="He so b:").grid(row=2,column=0)
Entry(root,width=30,textvariable=stringHSB).grid(row=2,column=1)

frameButton = Frame()
Button(frameButton,text="Giai",command=giaiAction,height=2,width=3).pack(side=LEFT)
Button(frameButton,text="Tiep",command=tiepAction,height=2,width=3).pack(side=LEFT)
Button(frameButton,text="Thoat",command=root.quit,height=2,width=3).pack(side=LEFT)
frameButton.grid(row=3,columnspan=2)

Label(root,text="Ket Qua",height=5).grid(row=4,column=0)
Entry(root,width=30,textvariable=stringKQ).grid(row=4,column=1)



root.mainloop()

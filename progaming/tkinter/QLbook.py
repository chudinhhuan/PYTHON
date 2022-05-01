from tkinter import *
from XuLyFileBook import *
def themAction():
    line  =  stringMa.get() + ";" + stringTen.get() + ";" + stringNam.get()
    LuuFile(line)
    stringTen.set("")
    stringMa.set("")
    stringNam.set("")
    showSach()
def showSach():
    arrSach = DocFile()
    listbosx.delete(0,END)
    for item in arrSach:
        listbosx.insert(END,item)

def SapXep():
    arrSach = DocFile()
    for i in range(len(arrSach)):
        for j in range(len(arrSach)):
            a =  arrSach[i]
            b = arrSach[j]
            if a[2] > b[2]:
                arrSach[i] = b
                arrSach[j] = a
    listbosx.delete(0,END)
    for item in arrSach:
        listbosx.insert(END,item)

def timAction():
    arrSach = DocFile()
    ma = stringMa.get()
    ten = stringTen.get()
    nam = stringNam.get()
    for sach in arrSach:
        if sach[0] == ma or sach[1].lower() == ten.lower():
            listbosx.delete(0,END)
            listbosx.insert(END,sach)

            stringMa.set("")
            stringNam.set("")
            break
        else:
            showSach()
            stringMa.set("")
            stringNam.set("")

    

        


root =Tk()

# bien tham chieu
stringMa = StringVar()
stringTen = StringVar()
stringNam = StringVar()


root.title("QUAN LY SACH")
root.minsize(width=320,height=300)
Label(root,text="QUAN LY SACH",fg="blue",font=("cambria",16),justify=CENTER).grid(row=0,column=0,columnspan=1)
listbosx = Listbox(root,width=65)
listbosx.grid(row=1,columnspan=2)
showSach()

Label(root,text="Ma sach").grid(row=2,column=0)
Entry(root,width=30,textvariable=stringMa).grid(row=2,column=1)

Label(root,text="Ten sach").grid(row=3,column=0)
Entry(root,width=30,textvariable=stringTen).grid(row=3,column=1)

Label(root,text="Nam xua ban").grid(row=4,column=0)
Entry(root,width=30,textvariable=stringNam).grid(row=4,column=1)

frameButton = Frame(root)
Button(frameButton,text="Them",command=themAction).pack(side=LEFT)
Button(frameButton,text="Tim",command=timAction).pack(side=LEFT)
Button(frameButton,text="Sap xep",command=SapXep).pack(side=LEFT)
Button(frameButton,text="Thoat",command=root.quit).pack(side=LEFT)
frameButton.grid(row=5,column=1)



root.mainloop()
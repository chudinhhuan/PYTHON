from tkinter import *

root = Tk()
root.title('Hoc control basic') #titile 
root.resizable(height=True,width=True) # cho phep thay doi size
root.minsize(height=200,width=400) #min max

Label(root,text = 'Hello tkinter',fg='red').pack() # tao cai nhan hien thi , pack()
Button(root,text = "Click me",command=root.quit).pack() # tao nut bam , command.quit de thoat

e = StringVar()#tao ra cai bien de thay doi
e.set("http://dinhuan.com")
Entry(root,textvariable = e,width=30).pack() # nhap vao o button


root.mainloop()
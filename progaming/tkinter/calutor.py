from tkinter import *
from playsound import playsound


def btnClick(numbers):
    global operator
    # playsound("tit.wav",block=False)
    operator += str(numbers)
    text_Input.set(operator)


def btnClear():
    global operator
    # playsound("tit.wav",block=False)
    operator = ""
    text_Input.set("")
    
def btnEquals():
    global operator
    # playsound("tit.wav",block=False)
    kq = str(eval(operator))
    text_Input.set(kq)

root = Tk()
root.title("Calculator")
operator = ""
text_Input = StringVar()
textDisplay = Entry(root,width=30,font=("arial",20,"bold"),textvariable=text_Input,bd=20,insertborderwidth=4,bg="aqua",justify="right").grid(columnspan=4)

#  cac nut
bt7 = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text="7",command=lambda:btnClick(7),bg="silver").grid(row=1,column=0)  
bt8 = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text="8",command=lambda:btnClick(8),bg="silver").grid(row=1,column=1)  
bt9 = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text="9",command=lambda:btnClick(9),bg="silver").grid(row=1,column=2)  
btDe = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text="/",command=lambda:btnClick("/"),bg="silver").grid(row=1,column=3)  
# ----------------------------------------------------
bt4 = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text="4",command=lambda:btnClick(4),bg="silver").grid(row=2,column=0)  
bt5 = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text="5",command=lambda:btnClick(5),bg="silver").grid(row=2,column=1)  
bt6 = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text="6",command=lambda:btnClick(6),bg="silver").grid(row=2,column=2)  
btMu = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text="x",command=lambda:btnClick("*"),bg="silver").grid(row=2,column=3)  
# ----------------------------------------------------
bt1 = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text="1",command=lambda:btnClick(1),bg="silver").grid(row=3,column=0)  
bt2 = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text="2",command=lambda:btnClick(2),bg="silver").grid(row=3,column=1)  
bt3 = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text="3",command=lambda:btnClick(3),bg="silver").grid(row=3,column=2)  
btSub = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text="-",command=lambda:btnClick("-"),bg="silver").grid(row=3,column=3)  
# ----------------------------------------------------
btClear = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text="Clr",command=btnClear,bg="silver").grid(row=4,column=0)  
btdo = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text=".",command=lambda:btnClick("."),bg="silver").grid(row=4,column=1)  
bt0 = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text="0",command=lambda:btnClick(0),bg="silver").grid(row=4,column=2)  
btAdd = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text="+",command=lambda:btnClick("+"),bg="silver").grid(row=4,column=3) 

btopen = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text="(",command=lambda:btnClick("("),bg="silver").grid(row=5,column=0)  
btcl = Button(root,padx=30,bd=8,fg="black",font=("arial",20,"bold"),text=")",command=lambda:btnClick(")"),bg="silver").grid(row=5,column=1)  
btEquals = Button(root,padx=70,bd=8,fg="black",font=("arial",20,"bold"),text="=",command=btnEquals,bg="silver").grid(row=5,column=2,columnspan=2)  



root.mainloop()
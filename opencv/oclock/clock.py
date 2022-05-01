from tkinter import*
from time import*

def show():
    t=strftime('%H:%M:%S')
    tlb.config(text=t)
    
    d=strftime('%d:%m:%y')
    dlb.config(text=d)
    
    wd.after(500,show)
    
wd =Tk()
wd.title('ĐỒNG HỒ')
wd.iconbitmap('clock.ico')
wd.wm_attributes('-topmost',True)
tlb=Label(wd,font=('Arial',50),fg='#FFFFFF',bg='#0D8A42')
tlb.pack()

dlb=Label(wd,font=('InkFree',25),fg='#0D8A42')
dlb.pack()
show()

wd.mainloop()

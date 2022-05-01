
import imp


import pyautogui, pyperclip,random,time

print('spam')
msg = input('nhap noi dung spam : ').split(' || ')
n = int(input('nhap so lan spam: '))
m = float(input('nhap time delay: '))

print('chuan bi')
for i in range(5,0,-1):
    print(i,end='...',flush='True')
print('start')

for i in range(n):
    pyperclip.copy(random.choice(msg))
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    time.sleep(m)
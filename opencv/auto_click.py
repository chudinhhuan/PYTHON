import pyautogui, time
delay  = float(input('nhap time delay: '))
so_lan_click = int(input('nhap so lan click: '))

print('di chuyen chuot toi vi tri can click')
print('bat dau trong vong ... ')

for i in range(5,0,-1):
    print(i)
    time.sleep(1)
    
x,y = pyautogui.position()
for _ in range(so_lan_click):
    pyautogui.click(x,y)
    time.sleep(delay)  
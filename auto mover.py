import tkinter as tk
import pyautogui
import time

root = tk.Tk()

global clickon
clickon = False

global moveon
moveon = False

def AutoMove():
    global moveon
    time.sleep(0.5)
    pyautogui.press('a')
    pyautogui.press('d')
    time.sleep(0.5)
def AutoClick():
    global clickon
    print("Starting AutoClick function")
    if clickon == False:
        clickon = True
        print("AutoClick turned on")
        while clickon:
            time.sleep(0.5)
            if clickon:
                pyautogui.leftClick()
            time.sleep(0.5)
        print("AutoClick turned off")
    else:
        clickon = False
        print("AutoClick turned off")
    print("End of function")




canvas = tk.Canvas(root, height= 400, width= 600, bg='gray5')
canvas.pack()

frame = tk.Frame(root, bg='gray10')
frame.place(relwidth=0.9, relheight=0.83, relx= 0.05, rely= 0.07)

automover = tk.Button(frame, text='Auto Mover', padx=30, pady= 10, fg= 'black', bg='firebrick1', command= AutoMove)
automover.pack()

autoclicker = tk.Button(frame, text='Auto Clicker', padx=27, pady= 10, fg= 'black', bg='firebrick1', command = AutoClick)
autoclicker.pack(pady= 50)




root.mainloop()


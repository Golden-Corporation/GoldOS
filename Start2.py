import os
from tkinter import *

os.system('sudo cp $PWD/NewLogo.png /usr/share/plymouth/themes/spinner/watermark.png')
os.system('sudo cp $PWD/GoldOSMiniLogo.png /user/share/plymouth/themes/spinner/bgrt-fallback.png')
os.system('sudo cp $PWD/GoldOSMiniLogo.png /usr/share/plymouth/themes/spinner/bgrt-fallback.png')


window = Tk() # Only run when all other install processes are done.

def Clean():
    os.system('gsettings set org.gnome.desktop.background picture-uri file:$PWD/Assets/CleanGold.png')
    window.destroy()
    
def DClean():
    os.system('gsettings set org.gnome.desktop.background picture-uri file:$PWD/Assets/CleanGoldDark.png')
    window.destroy()
    
def Firey():
    os.system('gsettings set org.gnome.desktop.background picture-uri file:$PWD/Assets/GoldFirey.png')
    window.destroy()
    
def DFirey():
    os.system('gsettings set org.gnome.desktop.background picture-uri file:$PWD/Assets/GoldFireyDark.png')
    window.destroy()
    
def Horri():
    os.system('gsettings set org.gnome.desktop.background picture-uri file:$PWD/Assets/GoldHorizon.png')
    window.destroy()

def DHorri():
    os.system('gsettings set org.gnome.desktop.background picture-uri file:$PWD/Assets/GoldHorizonDark.png')
    window.destroy()

clean = PhotoImage(file = 'Assets/Small/CleanGold.png')
cleanB = Button(window, image = clean, command = Clean).grid(column = 1, row = 1)

cleanD = PhotoImage(file = 'Assets/Small/CleanGoldDark.png')
cleanDB = Button(window, image = cleanD, command = DClean).grid(column = 1, row = 2)

Gold = PhotoImage(file = 'Assets/Small/GoldFirey.png')
GoldB = Button(window, image = Gold, command = Firey).grid(column = 2, row = 1)

GoldD = PhotoImage(file = 'Assets/Small/GoldFireyDark.png')
GoldDB = Button(window, image = GoldD, command = DFirey).grid(column = 2, row = 2)

Horr = PhotoImage(file = 'Assets/Small/GoldHorizon.png')
HorrB = Button(window, image = Horr, command = Horri).grid(column = 3, row = 1)

HorrD = PhotoImage(file = 'Assets/Small/GoldHorizonDark.png')
HorrDB = Button(window, image = HorrD, command = DHorri).grid(column = 3, row = 2)

window['bg'] = '#FFBF00'
window.title('Choose BG')
window.geometry("630x242+150+300")
window.resizable(False, False)
window.mainloop()

import os
import time

input('Before you start installing, note that this installer is a developer version and may be not ready for use. Press enter if you want to continue.')
print('Installing.')

os.system('sudo apt install plymouth-themes')
os.system('gsettings set org.gnome.shell.extensions.dash-to-dock dock-position BOTTOM')
os.system('gsettings set org.gnome.desktop.background picture-uri file:$PWD/BG.png')

time.sleep(2.5)

os.system('sudo mv $PWD/NewLogo.png /usr/share/plymouth/themes/spinner/watermark.png')

try:
    os.system('sudo mv $PWD/GoldOSMiniLogo.png /usr/share/plymouth/themes/spinner/bgrt-fallback.png')
finally:
    pass

print('Install complete! Your system will reboot in 5 seconds.')

time.sleep(5)

os.system('sudo reboot')

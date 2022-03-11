import os
import time

input('Start installing? ')
print('Installing.')
print('Setup may require for you to enter your password a few times.')
time.sleep(5)

os.system('sudo apt install plymouth-themes')
os.system('gsettings set org.gnome.shell.extensions.dash-to-dock dock-position BOTTOM')
os.system('gsettings set org.gnome.desktop.background picture-uri file:$PWD/BG.png')

time.sleep(2.5)

os.system('sudo mv $PWD/NewLogo.png /usr/share/plymouth/themes/spinner/watermark.png')
os.system('sudo mv $PWD/GoldOSMiniLogo.png /user/share/plymouth/themes/spinner/bgrt-fallback.png')

print('Install complete! Your system will reboot in 5 seconds.')

time.sleep(5)

os.system('sudo reboot')

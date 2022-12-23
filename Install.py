import os
import time

print("WARNING: This is currently being re-written and this is not recomended to be installed :\\")
print("Install at your own risk; come back later for better code :)")
input('Start installing? ')
print('Installing.')
print('Please wait for a little while, while we prepare.')
print('If you see anything about a lock, please reboot your computer.')

time.sleep(3)

os.system('sudo apt-get update') # Always run this first, can fix broken installs.

os.system('sudo apt -y install plymouth-themes')
os.system('sudo apt -y install python3-tk')
os.system('sudo apt -y install git')

print('\nFinishing up.')

os.system('python3 Start2.py')

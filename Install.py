import os
import time

input('Start installing? ')
print('Installing.')
print('Setup will restart your computer later into the installation.')

os.system('sudo apt install plymouth-themes')
os.system('sudo apt install python3-tk')

os.system('python3 Start2.py')

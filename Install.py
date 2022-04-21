import os
import time

input('Start installing? ')
print('Installing.')
print('Please wait for a little while, while we prepare.')

time.sleep(3)

os.system('sudo apt -y install plymouth-themes')
os.system('sudo apt -y install python3-tk')
os.system('sudo apt-get -y install git')

print('\nFinishing up.')

os.system('python3 Start2.py')

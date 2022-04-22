import os
import time

input('Start installing? ')
print('Installing.')
print('Please wait for a little while, while we prepare.')

time.sleep(3)

# Next lines are to stop update locks from working if the user has the program running.
os.system('sudo killall -9 synaptic')
os.system('sudo rm /var/lib/dpkg/lock-frontend')
os.system('sudo rm /var/lib/dpkg/lock')

os.system('sudo apt-get update') # Always run this first, can fix broken installs.

os.system('sudo apt -y install plymouth-themes')
os.system('sudo apt -y install python3-tk')
os.system('sudo apt -y install git')

print('\nFinishing up.')

os.system('python3 Start2.py')

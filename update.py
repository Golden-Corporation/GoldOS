import os
import json

updateAvailable = False
updateId = ''
letter = ''
localletter = ''

version = open(r"/var/cache/Gversion.txt", "r")
versionDict = json.loads(version.read())

os.system('sudo git clone https://github.com/Golden-Corporation/GoldOS /tmp/gOScache')

newVersion = open(r"/tmp/gOScache/VerNum.txt", "r")
newVersionDict = json.loads(newVersion.read())

if versionDict['topRel'] < newVersionDict['topRel']:
    updateAvailable = True

elif versionDict['featureRel'] < newVersionDict['featureRel']:
    updateAvailable = True

elif versionDict['patchRel'] < newVersionDict['patchRel']:
    updateAvailable = True

elif versionDict['minpatchRel'] < newVersionDict['minpatchRel']:
    updateAvailable = True

if newVersionDict['minpatchRel'] != 0:
    letter = chr(ord('`') + newVersionDict['minpatchRel'])

if versionDict['minpatchRel'] != 0:
    localletter = chr(ord('`') + versionDict['minpatchRel'])

if updateAvailable == True:

    updateId = 'GoldOS ' + letter + str(newVersionDict['topRel']) + '.' + str(newVersionDict['featureRel']) + '.' + str(newVersionDict['patchRel'])
    localUpdateId = 'GoldOS ' + localletter + str(versionDict['topRel']) + '.' + str(versionDict['featureRel']) + '.' + str(versionDict['patchRel'])

    print(f'New update found ({updateId}).')
    print(f'Your current version is {localUpdateId}')
    input(f'Press enter to update to {updateId}')
    os.system('python3 /tmp/gOScache/Install.py')

else:
    print('No new updates found.')

# Run these next lines at the end.
version.close()
newVersion.close()
os.system('sudo rm -r /tmp/gOScache')

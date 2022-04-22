import os
import json

updateAvailable = False
updateId = ''

version = open(r"/var/cache/version.txt", "r")
versionDict = json.loads(version.read())

os.system('git clone https://github.com/Golden-Corporation/GoldOS /tmp/gOScache')

newVersion = open(r"/tmp/gOScache/VerNum.txt", "r")
newVersionDict = json.loads(version.read())

if versionDict['topRel'] < newVersionDict['topRel']:
    updateAvailable = True

elif versionDict['featureRel'] < newVersionDict['featureRel']:
    updateAvailable = True

elif versionDict['patchRel'] < newVersionDict['patchRel']:
    updateAvailable = True

elif versionDict['minpatchRel'] < newVersionDict['minpatchRel']:
    updateAvailable = True

if updateAvailable == True:
    letter = ''

    if newVersionDict['minpatchRel'] != 0:
        letter = chr(ord('`') + newVersionDict['minpatchRel'])
    
    updateId = 'GoldOS ' + letter + str(newVersionDict['topRel']) + '.' + str(newVersionDict['featureRel']) + '.' + str(newVersionDict['patchRel'])

    print(f'new update found ({updateId})')

# Run these next lines at the end.
version.close()
newVersion.close()
os.system('sudo rm -r /tmp/gOScache')

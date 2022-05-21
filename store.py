import tkinter as tk
import os
import json
import random
import webbrowser

os.system('sudo git clone https://github.com/Golden-Corporation/GoldOSApps /tmp/gOScache')

apps = open(r"/tmp/gOScache/AppList.txt", "r")
appsFile = apps.read()
print(appsFile)
appsList = (appsFile.split(', '))

#appsList[len(appsList) - 1] = (appsList[len(appsList) - 1].replace(f'\\n', ''))
print(appsList[1])

app1dataFile = open(f'/tmp/gOScache/{appsList[0]}/MetaData.txt')
app1data = json.loads(app1dataFile.read())

app2dataFile = open('/tmp/gOScache/' + appsList[1] + '/MetaData.txt')
app2data = json.loads(app2dataFile.read())

class App:
    def __init__(self, root):
        #setting title
        root.title("GoldOS Store")
        #setting window size
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        width=700
        height=screenheight / 2
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)

        AppName1=tk.Label(root)
        AppName1["fg"] = "#333333"
        AppName1["justify"] = "center"
        AppName1["text"] = app1data["Name"]
        AppName1.place(x=30,y=195,width=300,height=180)

        AppDesc1=tk.Label(root)
        AppDesc1["fg"] = "#333333"
        AppDesc1["justify"] = "left"
        AppDesc1["text"] = app1data["Description"]
        AppDesc1.place(x=30,y=325,width=240,height=15)

        Download1=tk.Button(root)
        Download1["bg"] = "#52e341"
        Download1["fg"] = "#ffffff"
        Download1["justify"] = "center"
        Download1["text"] = "Download"
        Download1.place(x=30,y=270,width=70,height=25)
        Download1["command"] = self.Download1_command

        AppName2=tk.Label(root)
        AppName2["fg"] = "#333333"
        AppName2["justify"] = "center"
        AppName2["text"] = app2data["Name"]
        AppName2.place(x=300,y=195,width=360,height=180)

        AppDesc2=tk.Label(root)
        AppDesc2["fg"] = "#333333"
        AppDesc2["justify"] = "left"
        AppDesc2["text"] = app2data["Description"]
        AppDesc2.place(x=325,y=325,width=240,height=15)

        Download2=tk.Button(root)
        Download2["bg"] = "#01ff12"
        Download2["fg"] = "#ffffff"
        Download2["justify"] = "center"
        Download2["text"] = "Download"
        Download2.place(x=330,y=270,width=70,height=25)
        Download2["command"] = self.Download2_command

    def Download1_command(self):
        print("command")


    def Download2_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

apps.close()
app1dataFile.close()
app2dataFile.close()

os.system('sudo rm -r /tmp/gOScache')

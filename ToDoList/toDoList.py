#!/usr/bin/python
'''
    Name: Kyle Just

    Description:
        This will keep track of a weekly todo list and convienently display it
        to you

'''
import tkinter
from varname import argname
import re
import inspect
import pickle
import colorsys


def listAtts(obj):
    config = obj.configure()
    if isinstance(config, dict):
        print(argname('obj') + ': \'' + str(obj) + '\'')
        lenList = []
        for word in obj.keys():
            lenList.append(len(word))
        for x in config:
            print(x, end=' ' * (max(lenList) - len(x) + 2))
            print(config.get(x))
        print('\n')
    else:
        print(config)

###################### User defined objects ###################################


class settings:
    def __init__(self, x, y, color):
        self.window_x = x
        self.window_y = y
        self.RESOLUTION = str(self.window_x) + "x" + str(self.window_y)
        self.baseColor = color

    def setWindow(self, x, y):
        self.window_x = x
        self.window_y = y

    def getWindowx(self):
        return self.window_x

    def getWindowy(self):
        return self.window_y

    def getResolution(self):
        return self.RESOLUTION

    def getBaseColor(self):
        return "#" + self.baseColor

    def getColorA(self):
        pass


class tditem:
    def __init__(self, args):
        self.completed = False
        for arg in args:
            if re.match(r"^http", str(arg)) is not None:
                self.link = str(arg)
            elif re.match(r"^[A-Z]:", str(arg)) is not None:
                self.file = str(arg)
            else:
                self.text = str(arg)

    def complete(self):
        self.complete = True

    def uncomplete(self):
        self.completed = False

    def getCompleted(self):
        return self.completed

    def getText(self):
        if hasattr(self, 'text'):
            return self.text
        else:
            return None

    def getLink(self):
        if hasattr(self, 'link'):
            return self.link
        else:
            return None

    def getFile(self):
        if hasattr(self, 'file'):
            return self.file
        else:
            return None
########################### End of user defined objects########################

########################### Button Methods ####################################


def saveList(list):
    with open("list.pickle", 'wb') as f:
        pickle.dump(list, f)
    print("List saved!")


def saveSettings(settings):
    with open("settings.pickle", 'wb') as f:
        pickle.dump(settings, f)
    print("Settings saved!")


def saveAs():
    pass


def loadList():
    global list
    with open("list.pickle", 'rb') as f:
        list = pickle.load(f)
    print("List loaded!")


def loadSettings():
    global sett
    with open("settings.pickle", 'rb') as f:
        sett = pickle.load(f)
    print("Settings loaded")


def loadListFile():
    pass


def export():
    pass


def printList():
    for i in range(len(list)):
        print(list[i].getText())
        print(list[i].getLink())
        print(list[i].getFile())


def nextTask():
    list.append(list.pop(0))
    toDoText.set(list[0].text)
    print("Onto the next task!")


def prevTask():
    list.insert(0, list.pop(len(list)-1))
    toDoText.set(list[0].text)
    print("Wait, back to the previous task!")


def addTask(position, aList):
    addChild = tkinter.Toplevel(window)
    addChild.geometry("450x550")
    addChild.config(bg="#282E52")
    addChild.title("Add Task")

    list.insert(position, tditem(aList))


def remTask(task):
    list.remove(task)


def editTask():
    editChild = tkinter.Toplevel(window)
    editChild.geometry("450x550")
    editChild.config(bg="#282E52")
    editChild.title("Edit Task")


def help():
    helpChild = tkinter.Toplevel(window)
    helpChild.geometry("250x250")
    helpChild.config(bg="#282E52")
    helpChild.title("Help")


def markComplete(task):
    task.complete()


############################# End of button methods ###########################
'''
#Settings to use if files stop working
sett = settings(420, 176, '6675D1')
list = [tditem(["https://www.google.com", "X:\\CPP\\", "Do your homeword"]),
        tditem(["https://www.yahoo.com", "Play gamez"]),
        tditem(["Just be nice :)"])]
save(list, sett)
'''
list = None
sett = None
loadList()
loadSettings()
for item in list:
    print(item.getText())
############################# Start window building ###########################
window = tkinter.Tk()
window.title("To-Do List")
window.config(bg="#485394")
window.geometry(sett.getResolution())
toDoLabel = tkinter.Label(window,
                          bg="#485394",
                          fg="#ABB1D9",
                          font=('monotype', 16),
                          justify='center',
                          height=0,
                          width=20)
toDoLabel.place(relx=0.5,
                rely=0.5,
                anchor='center')
toDoText = tkinter.StringVar(toDoLabel)
toDoLabel.config(textvariable=toDoText)
toDoText.set(list[0].text)

menuBar = tkinter.Menu(window)  # Menu bar to hold all other menus
################### Start of the file menu ####################################
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_command(label="Test", command=printList)
fileMenu.add_command(label="Save", command=lambda: [saveList(list),
                                                    saveSettings(sett)])
fileMenu.add_command(label="Save As", command=saveAs)
fileMenu.add_command(label="Export", command=export)
fileMenu.add_command(label="Load", command=loadListFile)
fileMenu.add_command(label="Refresh", command=loadList)
menuBar.add_cascade(label="File", menu=fileMenu)
################### Start of the edit menu ####################################
editMenu = tkinter.Menu(menuBar)
editMenu.add_command(label="Edit Task", command=editTask)
menuBar.add_cascade(label="Edit", menu=editMenu) #!!Add textboxes for this
####################### Help Button ###########################################
menuBar.add_command(label="Help", command=help)
window.config(menu=menuBar)
############################# End of Menu Config ##############################


btnFrame = tkinter.Frame(window,
                         bg="#485394",
                         width=17,
                         height=30)
btnFrame.place(relx=0.75,
               rely=0.5,
               x=10,
               y=0,
               anchor='center')
nextBtn = tkinter.Button(btnFrame,
                         bg="#282E52",
                         width=1,
                         command=nextTask)
nextBtn.pack()
prevBtn = tkinter.Button(btnFrame,
                         bg="#282E52",
                         width=1,
                         command=prevTask)
prevBtn.pack()

########################End of window building#################################
window.mainloop()
saveSettings(sett)
saveList(list)

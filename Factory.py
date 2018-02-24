#Game: Factory
#Name: Bill Zhang

from tkinter import*
import time
'''
root = Tk() #root window
print = Label(root, text= "print this text") #creates label
print.pack() #positions the label
root.mainloop() #puts root in constant loop
'''

class Factory():
    #constructor
    def __init__(self):

        #Management Data Variables
        self.factories = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
#                         0  1  2  3  4  5  6  7  8  9  10 11
        self.cookies = 0

        #Graphical Setup
        self.master = Tk() #defines window

        self.cookieButton = Button(self.master, text="Click for Cookies", command=self.cookieClick)
        self.cookieLabel = Label(self.master, text="Cookies: " + str(self.cookies) + "\n")

        self.factory0Button = Button(self.master, text="Auto-Clicker", command=self.factory0Click)
        self.factory0 = Label(self.master, text="Auto-Clickers: " + str(self.factories[0]) + "\n")

        self.factory1Button = Button(self.master, text="Computer Bots", command=self.factory1Click)
        self.factory1 = Label(self.master, text="Computer Bots: " + str(self.factories[1]) + "\n")


        #packing
        self.cookieButton.pack()
        self.cookieLabel.pack()
        self.factory0Button.pack()
        self.factory0.pack()
        self.factory1Button.pack()
        self.factory1.pack()

        #YOU SHALL NOT PASS!1!!
        self.master.mainloop()

    def cookieClick(self):
        self.cookies = self.cookies + 1
        self.cookieLabel.config(text="Cookies: " + str(self.cookies) + "\n")
    def factory0Click(self):
        self.factories[0] = self.factories[0] + 1
        self.factory0.config(text="Auto-Clickers: " + str(self.factories[0]) + "\n")
    def factory1Click(self):
        self.factories[1] = self.factories[1] + 1
        self.factory1.config(text="Computer Bots: " + str(self.factories[1]) + "\n")

game = Factory() #Constructs the object by running __init__(self)
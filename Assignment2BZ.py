#Game: Factory
#Name: Bill Zhang

from tkinter import*
import time
import math
import BZ3
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
        self.factories = [0, 0, 0, 0, 0]
        #                 0  1  2  3  4
        self.factoryPrice = [200, 500, 800, 1500, 2300]
        self.multi = [0, 0, 0, 0, 0]
        #             0  1  2  3  4
        self.multiPrice = [100, 2400, 8000, 13000, 50000]
        self.cookies = 0
        self.cookieMulti = 1
        #Graphical Setup
        self.master = Tk() #defines window
        self.master.minsize(width=240, height=550)

        self.cookieButton = Button(self.master, text="\n" + "Click for Cookies" + "\n", bg="red", fg="white", command=self.cookieClick)
        self.cookieLabel = Label(self.master, text="Cookies: " + str(self.cookies) + "\n")
        #factory buttons--------------------------------
        self.factory0Button = Button(self.master, text="Auto-Clicker", bg="blue", fg="white", command=self.factory0Click)
        self.factory0Price = Label(self.master, text="Price: " + str(self.factoryPrice[0]))
        self.factory0 = Label(self.master, text="Auto-Clickers: " + str(self.factories[0]) + "\n")

        self.factory1Button = Button(self.master, text="Computer Bots", bg="blue", fg="white", command=self.factory1Click)
        self.factory1Price = Label(self.master, text="Price: " + str(self.factoryPrice[1]))
        self.factory1 = Label(self.master, text="Computer Bots: " + str(self.factories[1]) + "\n")

        self.factory2Button = Button(self.master, text="Servers", bg="blue", fg="white",command=self.factory1Click)
        self.factory2Price = Label(self.master, text="Price: " + str(self.factoryPrice[2]))
        self.factory2 = Label(self.master, text="Servers: " + str(self.factories[2]) + "\n")

        self.factory3Button = Button(self.master, text="Labs", bg="blue", fg="white",command=self.factory3Click)
        self.factory3Price = Label(self.master, text="Price: " + str(self.factoryPrice[3]))
        self.factory3 = Label(self.master, text="Labs: " + str(self.factories[3]) + "\n")

        self.factory4Button = Button(self.master, text="Wormhole", bg="blue", fg="white",command=self.factory4Click)
        self.factory4Price = Label(self.master, text="Price: " + str(self.factoryPrice[4]))
        self.factory4 = Label(self.master, text="Wormholes: " + str(self.factories[4]) + "\n")

        #multi buttons-------------------------------------
        self.multi0Button = Button(self.master, text="Double Clicker", bg="green", fg="white", command=self.multi0Click)
        self.multi0 = Label(self.master, text="Double Clicker: " + str(self.multi[0]) + "\n")
        self.multi0Price = Label(self.master, text="Price: " + str(self.multiPrice[0]))

        self.multi1Button = Button(self.master, text="Triple Clicker", bg="green", fg="white", command=self.multi1Click)
        self.multi1 = Label(self.master, text="Triple Clicker: " + str(self.multi[1]) + "\n")
        self.multi1Price = Label(self.master, text="Price: " + str(self.multiPrice[1]))

        self.multi2Button = Button(self.master, text="Quintuple Clicker", bg="green", fg="white", command=self.multi2Click)
        self.multi2 = Label(self.master, text="Quintuple Clicker: " + str(self.multi[2]) + "\n")
        self.multi2Price = Label(self.master, text="Price: " + str(self.multiPrice[2]))

        self.multi3Button = Button(self.master, text="Decuple Clicker", bg="green", fg="white", command=self.multi3Click)
        self.multi3 = Label(self.master, text="Decuple Clicker: " + str(self.multi[3]) + "\n")
        self.multi3Price = Label(self.master, text="Price: " + str(self.multiPrice[3]))

        self.multi4Button = Button(self.master, text="Centuple Clicker", bg="green", fg="white", command=self.multi4Click)
        self.multi4 = Label(self.master, text="Centuple Clicker: " + str(self.multi[4]) + "\n")
        self.multi4Price = Label(self.master, text="Price: " + str(self.multiPrice[4]))
        #save botton--------------------
        self.saveButton = Button(self.master, text="Save Game", command=self.save)
        self.loadButton = Button(self.master, text="Load Game", command=self.load)

        #packing
        self.cookieButton.pack()
        self.cookieButton.place(x=65, y=0)
        self.cookieLabel.pack()
        self.cookieLabel.place(x=65, y=60)

        self.factory0Button.pack()
        self.factory0Button.place(x=10, y=90)
        self.factory0Price.pack()
        self.factory0Price.place(x=10, y=120)
        self.factory0.pack()
        self.factory0.place(x=10, y=140)
        self.factory1Button.pack()
        self.factory1Button.place(x=10, y=170)
        self.factory1Price.pack()
        self.factory1Price.place(x=10, y=200)
        self.factory1.pack()
        self.factory1.place(x=10, y=220)

        self.factory2Button.pack()
        self.factory2Button.place(x=10, y=250)
        self.factory2Price.pack()
        self.factory2Price.place(x=10, y=280)
        self.factory2.pack()
        self.factory2.place(x=10, y=300)

        self.factory3Button.pack()
        self.factory3Button.place(x=10, y=330)
        self.factory3Price.pack()
        self.factory3Price.place(x=10, y=360)
        self.factory3.pack()
        self.factory3.place(x=10, y=380)

        self.factory4Button.pack()
        self.factory4Button.place(x=10, y=410)
        self.factory4Price.pack()
        self.factory4Price.place(x=10, y=440)
        self.factory4.pack()
        self.factory4.place(x=10, y=460)

        self.multi0Button.pack()
        self.multi0Button.place(x=130, y=90)
        self.multi0Price.pack()
        self.multi0Price.place(x=130, y=120)
        self.multi0.pack()
        self.multi0.place(x=130, y=140)

        self.multi1Button.pack()
        self.multi1Button.place(x=130, y=170)
        self.multi1Price.pack()
        self.multi1Price.place(x=130, y=200)
        self.multi1.pack()
        self.multi1.place(x=130, y=220)

        self.multi2Button.pack()
        self.multi2Button.place(x=130, y=250)
        self.multi2Price.pack()
        self.multi2Price.place(x=130, y=280)
        self.multi2.pack()
        self.multi2.place(x=130, y=300)

        self.multi3Button.pack()
        self.multi3Button.place(x=130, y=330)
        self.multi3Price.pack()
        self.multi3Price.place(x=130, y=360)
        self.multi3.pack()
        self.multi3.place(x=130, y=380)

        self.multi4Button.pack()
        self.multi4Button.place(x=130, y=410)
        self.multi4Price.pack()
        self.multi4Price.place(x=130, y=440)
        self.multi4.pack()
        self.multi4.place(x=130, y=460)

        self.saveButton.pack()
        self.saveButton.place(x=75, y=490)
        self.loadButton.pack()
        self.loadButton.place(x=75, y=520)

        self.timer_tick()

        #do not pass, things outside of mainloop will not run
        self.master.mainloop()



    def timer_tick(self):
        self.master.after(1000,self.timer_tick)
        self.cookies = self.cookies + self.factories[0] * 1 * self.cookieMulti
        self.cookies = self.cookies + self.factories[1] * 3 * self.cookieMulti
        self.cookies = self.cookies + self.factories[2] * 5 * self.cookieMulti
        self.cookies = self.cookies + self.factories[3] * 10 * self.cookieMulti
        self.cookies = self.cookies + self.factories[4] * 25 * self.cookieMulti

        #text auto-update
        self.cookieLabel.config(text="Cookies: " + str(self.cookies) + "\n")

    def cookieClick(self):
        self.cookies = self.cookies + self.cookieMulti
        self.cookieLabel.config(text="Cookies: " + str(self.cookies) + "\n")

    #factory button functions----------------------------
    def factory0Click(self):
        if self.cookies >= self.factoryPrice[0]:
            self.cookies = self.cookies - self.factoryPrice[0]
            self.factoryPrice[0] = int((self.factoryPrice[0]* 2.5)//1)
            self.factories[0] = self.factories[0] + 1
            self.factory0.config(text="Auto-Clickers: " + str(self.factories[0]) + "\n")
            self.factory0Price.config(text="Price: " + str(self.factoryPrice[0]))
            self.cookieLabel.config(text="Cookies: " + str(self.cookies) + "\n")
    def factory1Click(self):
        if self.cookies >= self.factoryPrice[1]:
            self.cookies = self.cookies - self.factoryPrice[1]
            self.factoryPrice[1] = int((self.factoryPrice[1] * 2.5)//1)
            self.factories[1] = self.factories[1] + 1
            self.factory1Price.config(text="Price: " + str(self.factoryPrice[1]))
            self.factory1.config(text="Computer Bots: " + str(self.factories[1]) + "\n")
        self.cookieLabel.config(text="Cookies: " + str(self.cookies) + "\n")
    def factory2Click(self):
        if self.cookies >= self.factoryPrice[2]:
            self.cookies = self.cookies - self.factoryPrice[2]
            self.factoryPrice[2] = int((self.factoryPrice[2] * 2.5) // 1)
            self.factories[2] = self.factories[2] + 1
            self.factory2Price.config(text="Price: " + str(self.factoryPrice[2]))
            self.factory2.config(text="Servers: " + str(self.factories[2]) + "\n")
        self.cookieLabel.config(text="Cookies: " + str(self.cookies) + "\n")
    def factory3Click(self):
        if self.cookies >= self.factoryPrice[3]:
            self.cookies = self.cookies - self.factoryPrice[3]
            self.factoryPrice[3] = int((self.factoryPrice[3] * 2.5)//1)
            self.factories[3] = self.factories[3] + 1
            self.factory3Price.config(text="Price: " + str(self.factoryPrice[3]))
            self.factory3.config(text="Labs: " + str(self.factories[3]) + "\n")
        self.cookieLabel.config(text="Cookies: " + str(self.cookies) + "\n")
    def factory4Click(self):
        if self.cookies >= self.factoryPrice[4]:
            self.cookies = self.cookies - self.factoryPrice[4]
            self.factoryPrice[4] = int((self.factoryPrice[4] * 2.5)//1)
            self.factories[4] = self.factories[4] + 1
            self.factory4Price.config(text="Price: " + str(self.factoryPrice[4]))
            self.factory4.config(text="Wormholes: " + str(self.factories[4]) + "\n")
        self.cookieLabel.config(text="Cookies: " + str(self.cookies) + "\n")

    #multi button functions--------------------------
    def multi0Click(self):
        if self.cookies >= self.multiPrice[0]:
            self.cookies = self.cookies - self.multiPrice[0]
            self.multiPrice[0] = int((self.multiPrice[0] * 13)//1)
            self.multi[0] = self.multi[0] + 1
            self.cookieMulti = (2 ** self.multi[0]) * (3 ** self.multi[1]) * (5 ** self.multi[2]) * (10 ** self.multi[3]) * (100 ** self.multi[4])
            self.multi0.config(text="Double Clicker: " + str(self.multi[0]) + "\n")
            self.multi0Price.config(text="Price: " + str(self.multiPrice[0]))
            self.cookieLabel.config(text="Cookies: " + str(self.cookies) + "\n")
    def multi1Click(self):
        if self.cookies >= self.multiPrice[1]:
            self.cookies = self.cookies - self.multiPrice[1]
            self.multiPrice[1] = int((self.multiPrice[1] * 37) // 1)
            self.multi[1] = self.multi[1] + 1
            self.cookieMulti = (2 ** self.multi[0]) * (3 ** self.multi[1]) * (5 ** self.multi[2]) * (10 ** self.multi[3]) * (100 ** self.multi[4])
            self.multi1.config(text="Triple Clicker: " + str(self.multi[1]) + "\n")
            self.multi1Price.config(text="Price: " + str(self.multiPrice[1]))
            self.cookieLabel.config(text="Cookies: " + str(self.cookies) + "\n")
    def multi2Click(self):
        if self.cookies >= self.multiPrice[2]:
            self.cookies = self.cookies - self.multiPrice[2]
            self.multiPrice[2] = int((self.multiPrice[2] * 132) // 1)
            self.multi[2] = self.multi[2] + 1
            self.cookieMulti = (2 ** self.multi[0]) * (3 ** self.multi[1]) * (5 ** self.multi[2]) * (10 ** self.multi[3]) * (100 ** self.multi[4])
            self.multi2.config(text="Quintuple Clicker: " + str(self.multi[2]) + "\n")
            self.multi2Price.config(text="Price: " + str(self.multiPrice[2]))
            self.cookieLabel.config(text="Cookies: " + str(self.cookies) + "\n")
    def multi3Click(self):
        if self.cookies >= self.multiPrice[3]:
            self.cookies = self.cookies - self.multiPrice[3]
            self.multiPrice[3] = int((self.multiPrice[3] * 384) // 1)
            self.multi[3] = self.multi[3] + 1
            self.cookieMulti = (2 ** self.multi[0]) * (3 ** self.multi[1]) * (5 ** self.multi[2]) * (10 ** self.multi[3]) * (100 ** self.multi[4])
            self.multi3.config(text="Decuple Clicker: " + str(self.multi[3]) + "\n")
            self.multi3Price.config(text="Price: " + str(self.multiPrice[3]))
            self.cookieLabel.config(text="Cookies: " + str(self.cookies) + "\n")
    def multi4Click(self):
        if self.cookies >= self.multiPrice[4]:
            self.cookies = self.cookies - self.multiPrice[4]
            self.multiPrice[4] = int((self.multiPrice[4] * 1454) // 1)
            self.multi[4] = self.multi[4] + 1
            self.cookieMulti = (2 ** self.multi[0]) * (3 ** self.multi[1]) * (5 ** self.multi[2]) * (10 ** self.multi[3]) * (100 ** self.multi[4])
            self.multi4.config(text="Centuple Clicker: " + str(self.multi[4]) + "\n")
            self.multi4Price.config(text="Price: " + str(self.multiPrice[4]))
            self.cookieLabel.config(text="Cookies: " + str(self.cookies) + "\n")
    #save function-----------------------------
    def save(self):
        saveFile = open("saveFile.txt", "w")
        for i in range(4):
            saveFile.write(str(self.factories[i])+"*")
        saveFile.write(str(self.factories[4]))
        saveFile.write("-")
        for i in range(5):
            saveFile.write(str(self.factoryPrice[i])+"*")
        saveFile.write(str(self.factoryPrice[4]))
        saveFile.write("-")
        for i in range(5):
            saveFile.write(str(self.multi[i])+"*")
        saveFile.write(str(self.multi[4]))
        saveFile.write("-")
        for i in range(5):
            saveFile.write(str(self.multiPrice[i])+"*")
        saveFile.write(str(self.multiPrice[4]))
        saveFile.write("-"+str(self.cookies))
    def load(self):
        saveFile = open("saveFile.txt", "r")
        saveData = saveFile.read()
        split = saveData.split("-")
        self.factories = split[0].split("*")
        for i in range(5):
            self.factories[i] = int(self.factories[i])
        self.factoryPrice = split[1].split("*")
        for i in range(5):
            self.factoryPrice[i] = int(self.factoryPrice[i])
        self.multi = split[2].split("*")
        for i in range(5):
            self.multi[i] = int(self.multi[i])
        self.multiPrice = split[3].split("*")
        for i in range(5):
            self.multiPrice[i] = int(self.multiPrice[i])
        self.cookies = split[4].split("*")
        self.cookies = int(self.cookies[0])

game = Factory() #Constructs the object by running __init__(self)
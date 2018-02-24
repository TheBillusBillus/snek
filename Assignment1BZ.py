#Name: Bill Zhang
#Date: 10/13/2016
#Discription: Assignment 1, game, survival, text based
#***************************************************************************************************
#Imports
import time
import random
#***************************************************************************************************
#Start
sc = 0.3#sleep constant
def main():#intro to the game
    print("\n\n\n\n\n\n\n\n\n\nHello.")
    time.sleep(sc * 2)
    print("Welcome to the Forest.")
    time.sleep(sc * 3)
    print("Your goal is to simply make it out alive.")
    time.sleep(sc * 5)
    print("This game is turn based.")
    time.sleep(sc * 3)
    print("Be careful about what you choose.")
    time.sleep(sc * 3)
    print("You can not go back!")
    time.sleep(sc * 3)
    start = input("Are you ready for this? (y/n)\n")
    #Game start and restart loop
    while start.lower() == "y" or start.lower() == "yes":
        game()#calls up game
        start = input("\n\n\n\n\n\n\n\n\n\nWould you like to restart the game? (y/n)\n")
    print("\n\n\n\n\n\n\n\n\n\nThanks for playing!")
    time.sleep(5)
#Function(s)
def strike(text): #Strike function to strike through text
    return ''.join([u'\u0336{}'.format(c) for c in text])
def bar(stat):#health food and water bar function
    bar = ""
    for i in range(0, stat, 5):#for every 5 of a certain stat, it prints a shaded block and returns it
        bar = bar + "▓"
    return bar
def menu(stats, inv, fire): #main game menu
    print("\n\n\n\n\n\n\n\n\n\n|--- Menu ---|")
    if inv[5] > 0:
        print("01. Hunt")
    else:
        print("01. "+strike("Hunt"))#some options are not availible at times and will be struck through if certain requirements are met or not met
    print("02. Collect Wood")
    if fire == 0 and inv[0] > 0:
        print("03. Start fire")
    else:
        print("03. "+strike("Start Fire"))
    if fire == 1 and inv[1] > 0:
        print("04. Cook Meat")
    else:
        print("04. "+strike("Cook Meat"))
    if fire == 1 and inv[3] == 0:
        print("05. Boil Water")
    else:
        print("05. "+strike("Boil Water"))
    print("06. Eat")
    if inv[3] > 0:
        print("07. Drink")
    else:
        print("07. "+strike("Drink"))
    print("08. Travel")
    print("09. Sleep")
    print("10. Stats")
'''
Description of Method:
prints out stats by importing 2 lists and a variable
'''
def liststats(fire, stats, inv):
    if fire == 1:
        fireStr = "Yes"
    else:
        fireStr = "No"
    print("HP   : "+bar(stats[0]))#prints bar form of HP FOOD and WATER
    print("FOOD : "+bar(stats[1]))
    print("WATER: "+bar(stats[2]))
    print("|HP: " + str(stats[0]) + "|FOOD: " + str(stats[1]) + "|WATER: " + str(stats[2]) + "|STAMINA: " + str(stats[3]) + "|DISTANCE: " + str(stats[4]) + "|")
    print("|WOOD: " + str(inv[0]) + "|RAW MEAT: " + str(inv[1]) + "|COOKED MEAT: " + str(inv[2]) + "|CLEAN WATER: " + str(inv[3]) + "|MRE: " + str(inv[4]) + "|AMMO: " + str(inv[5]) + "|")
    print("|Fire: " + fireStr + "|")
'''
the full game it self
asks player to pick an option and bases what to do on that
'''
def save(stats, inv, fire):
    saveFile = open("saveFileAssignment1.txt", "w")
    saveName = input("Save Name: ")
    print1 = ""
    print2 = ""
    for i in range(len(stats)):
        print1 = str[i]
    for i in range(len(inv)):
        print2 = str[i]
    saveFile.write(saveName)
def game():
    #variables and stats reset after game
    stats = [100, 100, 100, 300, 500]  #Stats -> 0. Health|1. Food|2. Water|3. Stamina|4. Distance
    inv = [0, 0, 0, 0, 3, 50]  #Inventory -> 0. Wood|1. Raw Meat|2. Cooked Meat|3. Water|4. MRE|5. Ammo
    alive = 1 #if 1, it is true, if 0 it is false
    fire = 0
    chopperMulti = 1000 #change of getting a chopper, used to generate random int
    print("\n\n\n\n\n\n\n\n\n\n**A blinding light fills the room.**")
    time.sleep(sc * 3)
    print("You feel yourself falling...")
    time.sleep(sc * 3)
    print("You find a lanyard hanging behind you.")
    para = input("Pull lanyard? (Type \"pull\" to pull)\n").lower()
    if para.lower() == "pull":
        time.sleep(sc * 3)
        print ("A parachute opens behind you and you land safely at a clearing.")#some basic info on the game
        time.sleep(sc * 3)
        print ("On the ground, you find a large metal chest painted Red.")
        time.sleep(sc * 3)
        print ("Inside, you find a rifle, 50 rounds of ammunition, an axe, and 3 MREs")
        time.sleep(sc * 3)
        print ("You also find other useful equipment that could potentially help you along the way.")
        time.sleep(sc * 3)
        print ("On the bottom, there is a note explaining how to to use everything.")
        time.sleep(sc * 3)
        print ("(Your rifle will be used while hunting and ammunition will be consumed automaticly.)")
        time.sleep(sc * 3)
        print ("(MREs will add 100 FOOD and 1000 WATER)")
        time.sleep(sc * 3)
        while alive == 1:#goes into the real game, stats are now used to define life and death
            #main game
            menu(stats, inv, fire)#prints main menu each time
            opt = input("What would you like to do?\n").lower()#menu selection
            if opt == "1" or opt == "01" or opt == "hunt": #Hunting
                if inv[5] == 0:#ammo check
                    print("You do not have any AMMO!")
                else:
                    print("You started looking for animal tracks...")
                    time.sleep(sc * 3)
                    t = random.randrange(2,3)   #time spent
                    t = str(t)#converts and prints time spent
                    print(t+" hours later.")
                    t = int(t)#converts time spent back for maths
                    food = t*5
                    water = t*8
                    stam = t*10
                    f = random.randrange(5)     #found or not found animal by rng
                    if f >= 1:
                        a = random.randrange(3) #animal selection by rng
                        '''
                        Currently your game holds 4 animals.  Then there is an update and you now have
                        2 new animals.  This means you have to add a number of new if statments

                        Better approach: Create parallel array/list that contain all the information
                        use the a value to access the index which drives the data

                        animals = ["Wild Pig","Goat","Rabbit","Bear","Monguse"]
                        meat = [4,3,1,10,25]

                        Step 2: Would be you would populate this from a file.
                        '''
                        if a == 0:
                            aName = "Wild Pig"
                            meat = 4            #amount of meat u get
                            ammo = random.randrange(1,3) #ammo(s) used
                            dmg = 0#dmg taken
                        elif a == 1:
                            aName = "Goat"
                            meat = 3
                            ammo = 1
                            dmg = 0
                        elif a == 2:
                            aName = "Rabbit"
                            meat = 1
                            ammo = random.randrange(1,4)
                            dmg = 0
                        else:
                            aName = "Bear"
                            meat = 10
                            ammo = random.randrange(1,7)
                            ifdmg = random.randrange(3)  #if you were hurt selection by rng
                            if ifdmg == 0:
                                dmg = random.randrange(10,25)
                            else:
                                dmg = 0
                        ammo = str(ammo)#converts ammo, meat and dmg taken for print
                        meat = str(meat)
                        dmg = str(dmg)
                        time.sleep(sc * 5)
                        '''
                        create a function cprint(string,1)
                        '''
                        print("You spotted a "+aName+"...")
                        time.sleep(sc * 3)
                        print("You slowly approached the "+aName+" and took aim...")
                        time.sleep(sc * 3)
                        '''
                        deal with plural and non-plural
                        '''
                        print("You took "+ammo+" shot(s)...")
                        time.sleep(sc * 3)
                        print("The "+aName+" dropped dead.")
                        time.sleep(sc * 3)
                        print("You got "+meat+" piece(s) of meat.")
                        time.sleep(sc * 3)
                        print("In the process of killing the "+aName+", you took "+dmg+" damage.")
                        time.sleep(sc * 5)
                        ammo = int(ammo)#converts ammo, meat and dmg back for maths
                        meat = int(meat)
                        dmg = int(dmg)
                        stats[0] = stats[0]-dmg#calculates and updates dmg, food, water, stam, meat and ammo
                        stats[1] = stats[1]-food
                        stats[2] = stats[2]-water
                        stats[3] = stats[3]-stam
                        inv[1] = inv[1]+meat
                        inv[5] = inv[5]-ammo
                        #Death check
                        if stats[0] <= 0 or stats[1] <= 0 or stats[1] <= 0:
                            dead(stats)
                            return
                        time.sleep(sc * 5)
                    else:
                        food = t * 5
                        water = t * 8
                        stam = t * 10
                        print ("You did not find anything.")
                        stats[1] = stats[1] - food#updates food, water, stam
                        stats[2] = stats[2] - water
                        stats[3] = stats[3] - stam
                        if stats[0] <= 0 or stats[1] <= 0 or stats[1] <= 0:
                            #death check
                            dead(stats)
                            return
                        time.sleep(sc * 5)
            elif opt == "2" or opt == "02" or opt\
                    == "wood": #Collect wood
                time.sleep(sc * 5)
                print("You started looking for dry wood...")
                time.sleep(sc * 3)
                wood = random.randrange(2,4)#amount of food found by rng
                wood = str(wood)
                print("You found "+wood+" pieces of WOOD.")
                wood = int(wood)
                time.sleep(sc * 5)
                inv[0] = inv[0] + wood#updates, inv and stats
                stats[1] = stats[1]-5
                stats[2] = stats[2]-6
                stats[3] = stats[3]-10
                if stats[0] <= 0 or stats[1] <= 0 or stats[1] <= 0:
                    #death check
                    dead(stats)
                    return
            elif opt == "3" or opt == "03" or opt == "fire": #start fire
                if fire == 0 and inv[0] > 1:
                    time.sleep(sc * 5)
                    print("You found the lighter in your bag...")
                    time.sleep(sc * 3)
                    print("You made shavings using your knife and a log.")
                    time.sleep(sc * 3)
                    print("You tried to light the shavings on fire...")
                    time.sleep(sc * 3)
                    fireStart = random.randrange(19)
                    if fireStart == (0,2):#if between 0 and 2, you burn yourself
                        time.sleep(sc * 3)
                        print("You accidentally burnt your hands and put out the fire.")
                        time.sleep(sc * 3)
                        print("You took 5 dmg.")
                        time.sleep(sc * 5)
                        stats[0] = stats[0]-5
                        if stats[0] <= 0:
                            dead(stats)
                            return
                    elif fireStart == (3,5):#if between 3 and 5, loose wood
                        time.sleep(sc * 5)
                        print("The wood shavings seems too wet to be lit.")
                        time.sleep(sc * 3)
                        print("You wasted 1 piece of WOOD.")
                        time.sleep(sc * 3)
                        inv[0] = inv[0]-1
                    else:#any other value gives you a fire
                        time.sleep(sc * 5)
                        print("It worked, you now have a fire!")
                        time.sleep(sc * 3)
                        print("You used one piece of WOOD.")
                        time.sleep(sc * 5)
                        fire = 1#gives fire
                        inv[0] = inv[0]-1
                        if stats[0] <= 0 or stats[1] <= 0 or stats[1] <= 0:
                            dead(stats)#death check
                            return
                elif inv[0] == 0:#gives reason why you cant start a fire
                    print("You do not have any WOOD!")
                else:
                    print("You already have a fire!")
            elif opt == "4" or opt == "04" or opt\
                    == "cook": #cook meat
                if fire == 1 and inv[0] >= 1 and inv[1] >= 1:#fire and meat check
                    ifdmg = random.randrange(1,10)
                    if ifdmg == 1:#if ifdmg is 1, you burn yourself
                        print("As you were cooking your meat, you accidentally burnt your hands.")
                        print("You took 15 DMG.")
                        stats[0] = stats[0]-15
                    elif ifdmg == 2:#if ifdmg is 2, you loose what you cooked
                        print("You accidentally dropped you meat into the fire.")
                        print("It is no longer edible. :(")
                        inv[1] = inv[1]-1
                    else:#anything else gives you cooked meat
                        time.sleep(sc * 5)
                        print("You added a piece of WOOD to the fire and cooked your RAW MEAT.")
                        time.sleep(sc * 5)
                        inv[0] = inv[0]-1#updates inv, uses up 1 wood per cooked meat
                        inv[1] = inv[1]-1
                        inv[2] = inv[2]+1
                        stats[2] = stats[2]-5
                    if stats[0] <= 0 or stats[1] <= 0 or stats[1] <= 0:
                        dead(stats)
                        return
                elif fire == 0:#gives reason why you cant cook
                    time.sleep(sc * 5)
                    print("You do not have a fire!")
                elif inv[0] == 0:
                    time.sleep(sc * 5)
                    print("You do not have any WOOD!")
                else:
                    time.sleep(sc * 5)
                    print("You do not have any RAW MEAT to cook!")
            elif opt == "5" or opt == "05" or opt\
                    == "boil" or opt\
                    == "boil water":#boil water
                if inv[3] != 0:#check for water in bottle
                    time.sleep(sc * 5)
                    print("You still have WATER in your bottle!")
                if fire == 1:#checks for fire
                    ifdmg = random.randrange(1,5)
                    if ifdmg == 1:#dmg check, if ifdmg is 1, you burn yourself
                        time.sleep(sc * 5)
                        print("You accidentally spilt the water as it was boiling.")
                        time.sleep(sc * 3)
                        print("You took 25 DMG and put out the fire.")
                        time.sleep(sc * 5)
                        fire = 0
                        stats[0] = stats[0]-25
                    else:#else, you get water
                        time.sleep(sc * 5)
                        print("You filled your metal pot with water.")
                        time.sleep(sc * 3)
                        print("And boiled the water with your campfire.")
                        time.sleep(sc * 3)
                        print("You filled your water bottles")
                        inv[3] = 3
                        stats[1] = stats[1]-5
                        time.sleep(sc * 5)
                else:#cant boil water without fire
                    time.sleep(sc * 5)
                    print("You do not have a fire!")
                    time.sleep(sc * 5)
            elif opt == "6" or opt == "06" or opt == "eat":#eat
                typeFood = input("\n\n\n\n\n\n\n\n\n\n|---Food---|\n0. Back\n1. Raw Meat\n2. Cooked Meat\n3. MRE\nWhat would you like to eat?\n")
                if typeFood == "0":#takes you back to main menu
                    time.sleep(sc * .5)
                elif typeFood == "1":#eats raw meat
                    if inv[1] >= 1:
                        time.sleep(sc * 5)
                        print("You ate a piece of RAW MEAT...")
                        ifdmg = random.randrange(1, 10)
                        if ifdmg >= 5:#check if dmg is taken by rng
                            time.sleep(sc * 3)
                            print("You got sick and threw up!")
                            time.sleep(sc * 3)
                            print("You took 15 DMG.")
                            time.sleep(sc * 3)
                            dmg = 15
                            food = 0
                        else:
                            time.sleep(sc * 3)
                            print("Luckily, you didn't get sick.")
                            time.sleep(sc * 3)
                            print("You gained 10 FOOD.")
                            time.sleep(sc * 3)
                            dmg = 0
                            food = 10
                        stats[0] = stats[0]+food#updates food and dmg
                        stats[1] = stats[1]-dmg
                    else:
                        print("You do not have any RAW MEAT")
                        time.sleep(sc * 5)
                elif typeFood == "2":#eats cooked meat
                    if inv[2] >= 1:
                        time.sleep(sc * 5)
                        print("You ate a piece of COOKED MEAT and gained 10 HP and 20 FOOD.")
                        inv[2] = inv[2]-1
                        stats[0] = stats[0]+10
                        stats[1] = stats[1]+20
                        time.sleep(sc * 5)
                    else:
                        print("You do not have any COOKED MEAT.")
                    time.sleep(sc * 3)
                elif typeFood == "3":
                    if inv[4] >= 1:
                        time.sleep (sc * 5)
                        print("You took your time as you ate one of your precious MREs...")
                        time.sleep(sc * 3)
                        print("The food was great! You gained 100 FOOD and 100 WATER")
                        time.sleep(sc * 5)
                        stats[1] = stats[1]+100
                        stats[2] = stats[2]+100
                        inv[4] = inv[4]-1
                    else:
                        print("You do not have any MREs left!")
                else:
                    print("Invalid Command!")
                    time.sleep(sc * 5)
            elif opt == "7" or opt == "07" or opt\
                    == "drink":#drink
                if inv[3] >= 1:
                    time.sleep(sc * 3)
                    print("You took a drink from your water bottle.")
                    time.sleep(sc * 3)
                    print("You gained 20 WATER.")
                    inv[3] = inv[3]-1
                    stats[2] = stats[2]+50
                    time.sleep(sc * 5)
                else:
                    print("You do not have any WATER to drink.")
            elif opt == "8" or opt == "08" or opt\
                    == "travel":#travel
                if stats[3] >= 70:
                    chopper = random.randrange(1, chopperMulti)
                    if chopper == 1:
                        time.sleep(sc * 5)
                        print("You could not believe your eyes!")
                        time.sleep(sc * 3)
                        print("You found a shinny new helicopter in a large clearing.")
                        time.sleep(sc * 3)
                        print("You climbed inside and engaged the autopilot system.")
                        time.sleep(sc * 3)
                        print("2 hours later, you were enjoying a warm bath at the airport hotel\nwith your new helicopter parked outside your window.")
                        time.sleep(sc * 3)
                        print("Congratulations, you have won the game!")
                        time.sleep(sc * 5)
                        return
                    else:
                        dis = (random.randrange(4, 7))
                        dis = str(dis)
                        time.sleep(sc * 5)
                        print("You walked for "+dis+" hours...")
                        dis = int(dis)
                        disKM = str(dis*5)
                        time.sleep(sc * 3)
                        print("You traveled "+disKM+"km closer to the edge of the forest.")
                        disKM = int(disKM)
                        stats[4] = stats[4]-disKM
                        time.sleep(sc * 5)
                        stats[1] = stats[1]-dis*3
                        stats[2] = stats[2]-dis*5
                        stats[3] = stats[3]-dis*20
                        fire = 0
                    if stats[0] <= 0 or stats[1] <= 0 or stats[1] <= 0:
                        dead(stats)
                        return
                    elif stats[4] <= 0:
                        print("Congratulations! You made it out of the forest alive!")
                        time.sleep(sc * 5)
                        return
                else:
                    print("You do not have enough STAMINA to travel!")
                    time.sleep(sc * 5)
            elif opt == "9" or opt == "09" or opt\
                    == "sleep" or opt\
                    == "rest":
                time.sleep(sc * 3)
                print("Your slept for a few hours.")
                time.sleep(sc * 3)
                print("Your refilled your STAMINA.")
                time.sleep(sc * 3)
                stats[3]=300
            elif opt == "0" or opt == "10" or opt\
                    == "stats" or opt\
                    == "stat":     #Opens stats menu
                liststats(fire, stats, inv)
                time.sleep(sc * 5)
            elif opt == "123123123" or opt\
                    == "test":
                stats[0] = 10000
                stats[1] = 10000
                stats[2] = 10000
                stats[3] = 10000
                stats[4] = 10
                inv[0] = 100
                inv[1] = 100
                inv[2] = 100
                inv[3] = 100
                inv[4] = 100
                inv[5] = 100
                fire = 1
                chopperMulti = 2
                print("Cheat activated!")
            elif opt == "suicide":
                print("You committed suicide.")
                dead()
            elif opt == "exit":
                save(stats, inv, fire)
            else:
                print ("\n\n\n\n\n\n\n\n\n\nInvalid command!")
                time.sleep(sc * 5)
        print("\n\n\n\n\n\n\n\n\n\nYou were asked to stay alive... You have failed.")
    else:
        time.sleep(sc * 5)
        #End of game story if parachute was not pulled
        print("A few seconds later, you realise that you were falling from an aircraft.")
        time.sleep(sc * 3)
        print("The lanyard is for opening your parachute...")
        time.sleep(sc * 3)
        print("You pulled the lanyard but it was too late.")
        time.sleep(sc * 3)
        print("You were asked to stay alive... You have failed.")
        return
def dead(stats): #Death message
    print("Game Over!")
    if stats[0] <= 0:
        print("You died of blood loss.")
    if stats[1] <= 0:
        print("You died of starvation.")
    if stats[2] <= 0:
        print("You died of thirst.")
main()

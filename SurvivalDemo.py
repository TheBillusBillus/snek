import random

def game():

    #element 0 represents health
    #element 1 represent
    stats = [1,2,3,4]
    inv = [0,0,]
    print(stats[0])
    print(stats[1])
    print(stats[2])
    print(stats[3])
    alive = 0;

    while alive == 0:
        print(random.randint(0,100))
        print("Menu")
        print("1) Hunt")
        print("2) xxxx")
        option = input("What do you do?")


        if option == 1:
            print("You go hunting")






game()
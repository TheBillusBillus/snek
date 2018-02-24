#Name: Bill Zhang
#Date:10/27/2016
#Discription: Tournament Selection
a = input()
b = input()
c = input()
d = input()
e = input()
f = input()
wins = 0
if a == "W":
    wins = wins + 1
if b == "W":
    wins = wins + 1
if c == "W":
    wins = wins + 1
if d == "W":
    wins = wins + 1
if e == "W":
    wins = wins + 1
if f == "W":
    wins = wins + 1
if wins == 5 or wins == 6:
    print("1")
elif wins == 3 or wins == 4:
    print("2")
elif wins == 1 or wins == 2:
    print("3")
else:
    print("-1")
x = float(input("Number to round: "))
x = x*10000
a = x//100
b = x/100
dif = b-a
if dif >= 0.5:
    a = (a+1)/100
    print (a)
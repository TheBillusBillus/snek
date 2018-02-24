import math
n = True
while n == True:
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    x = (-b+math.sqrt(b**2-(4*a*c)))/2*a
    y = (-b-math.sqrt(b**2-(4*a*c)))/2*a
    print (x, y)
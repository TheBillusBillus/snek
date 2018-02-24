import math
import time
invalid_input = True
x  = 0
x0 = 0
v0 = 0
t  = 0
a  = 0
def start() :
    opt = input ("Choose your option:\n1. Solve for x\n2. Solve for x0\n3. Solve for v0\n4. Solve for t\n5. Solve for a\nInput: ")
    if opt == "x":
        #x = x0 + v0*t + (1/2)*a*(t**2)
        x0 = float (input ("Displacement (Initial): "))     #define variables
        v0 = float (input ("Velocity (Initial): "))
        t  = float (input ("Time: "))
        a  = float (input ("Acceleration: "))
        x = x0 + v0*t + (1/2)*a*(t**2)                      #calc
        print (x)                                           #print
        time.sleep(5)
    elif opt == "x0":
        #x0 = x - (v0*t) - ((1/2)*a*(t**2)
        x  = float (input ("Displacement (Final): "))
        v0 = float (input ("Velocity (Initial): "))
        t  = float (input ("Time: "))
        a  = float (input ("Acceleration: "))
        x0 = x - (v0*t) - ((1/2)*a*(t**2))
        print (x0)
        time.sleep(5)
    elif opt == "v0":
        #v0 = (x-x0)/t - a*t
        x0 = float(input("Displacement (Initial): "))
        x  = float (input ("Displacement (Final): "))
        t  = float (input ("Time: "))
        a  = float (input ("Acceleration: "))
        v0 = (x-x0)/t - a*t
        print (v0)
        time.sleep(5)
    elif opt == "a":
        #a  = (x-x0)/t - v*t
        x0 = float(input("Displacement (Initial): "))
        x  = float (input ("Displacement (Final): "))
        v0 = float (input ("Velocity (Initial): "))
        t  = float (input ("Time: "))
        a  = (x-x0)/t - v0*t
        print (a)
        time.sleep(5)
    elif opt == "t":
        #t  = (-v0 + math.sqrt(-v0**2 - 4*a*x0))/2*a
        try:
            x0 = float(input("Displacement (Initial): "))
            x  = float (input ("Displacement (Final): "))
            v0 = float (input ("Velocity (Initial): "))
            a  = float (input ("Acceleration: "))
            t  = (-v0 + math.sqrt(v0**2 - 4*a*x0)) / 2*a
            print (t)
            time.sleep(5)
        except ValueError:
            print ("Cannot Square Root Negative Values!")
            time.sleep(5)
    else:
        print ("Invalid Option!")
        time.sleep(5)
while invalid_input:
        start()
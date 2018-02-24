#Name: Bill Zhang
#Date:10/27/2016
#Discription: Triangle Times
a = int(input())
b = int(input())
c = int(input())
sum = a+b+c
if 0 < a <180 and 0 < b <180 and 0 < c <180 and sum == 180:
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
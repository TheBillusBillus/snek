#Name: Bill Zhang
#Date:10/27/2016
#Discription: Sounds fishy!
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b < c < d:
    print("Fish Rising")
elif a > b > c > d:
    print("Fish Diving")
elif a == b == c == d:
    print("Fish at Constant Depth")
else:
    print("No Fish")
#how to take different types of inputs
#strings
#intigers
#and floats
print("*******************************")
print("welcome to my example program")
print("*******************************")
#used input function to take input
name = input("what is your name? ")
print ("welcome",name)
age = input("how old are you? ")#all inputs are considered to be strings
print ("you are "+age+" years old")#age is an integer, not a string
#comp. can not calculate integers
#strings must be converted to integers before being calculated
int_age = int(age)
int_age5 = (int_age)+5
age5 = str (int_age5)
print = ("you will be "+age5+" in 5 years")

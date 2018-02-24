#1. everything is taken as a str
#2. we cannot do math with str
#x = 9 (int)
#y = "9" (str)
#z = 9.0 (float)

#if # will stay as word, leave as str
#if math, then convert to int
friends = input ("How many friends do you have? ")#leaving as str because it stays as one throughout the program

age = input("Insert age here: ")

int_age = int(age)#converts str [age] to int [int_age] for math
print ("Your age is "+age)
int_age = int_age+10#does math
age = str(int_age)#back to str to print
print("You will be "+age+" in 10 years")
#Name: Bill Zhang
#Date: 9/24/2016
#Discription: Mad Libs, how to take inputs and covert to int. and float, how to output int. and float

#take numbers as floats directly if you want to use it for math

#states date and time
import datetime
time = datetime.datetime.now()
print (time)

#declears variables (words and numbers)
print ("please fill in the following")
int1 = int (input("first #: "))#int1
float1 = float (input("second #: "))#float1-3
float2 = int (input ("third #: "))
float3 = int (input ("forth #: "))

#finds length of a random word
wordRandom = input ("random word:")
length1 = len(wordRandom)
length1 = int(length1)

#calcultions and conversion back to str.
int1 = int1+200
float1 = float1*length1
float2 = float2*2000
float3 = float3+5
int1 = str(int1)
float1 = str(float1)
float2 = str(float2)
float3 = str(float3)

#more values defined
noun1 = input ("first noun: ")
noun2 = input ("second noun (plural): ")
noun3 = input ("third noun: ")
noun4 = input ("forth noun (plural): ")
verb1 = input ("verb: ")
namePerson1 = input ("first person's name: ")#names as str
namePerson2 = input ("second person's name: ")
namePerson3 = input ("third person's name: ")
namePerson4 = input ("forth person's name: ")
nameGroup1 = input ("name of first organization: ")
nameGroup2 = input ("name of second organization: ")

#start of printing story
print ("PRESIDENT "+namePerson1+ ":")
print ("As I discussed in my speech earlier today before the "+nameGroup1+",")
print ("our "+nameGroup2+" system is facing a number of "+noun2+",")
print ("none of which can be solved by a single "+noun1+".")
print ("And for that matter, none of which can be solved solely by "+noun3+".")
print ("I want to thank "+namePerson2+", "+namePerson3+", and my friend, "+namePerson4+",")
print ("for bringing these leaders together here today. I'm pleased to announce that "+int1+" companies,")
print ("large and small, have stepped up and committed more than $"+float1+"0,")
print ("including in-kind contributions that are all designed to help "+verb1+" more than "+float2)
print (noun4+" across more than "+float3+" countries.")

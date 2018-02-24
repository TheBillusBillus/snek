#NOTES ABOUT WHILE LOOPS:

# A while loop is called a CONDITIONAL LOOP. It is used when you don't know how many times the loop will need to run.
# A while loop checks a condition at the start of the loop and then checks it again at
# the end of the loop to see if it needs to execute again.


# ****It is very important that:
# - YOUR VARIABLE BEING USED IN YOUR CONDITION IS ALREADY INITIALIZED BEFORE THE LOOP
# - YOUR CONDITION VARIABLE HAS THE OPPORTUNITY TO CHANGE WITHIN THE LOOP (OTHERWISE
#   THE LOOP WILL GO ON FOREVER)

#WHILE LOOP STRUCTURE:
#  condition variable initialization
#  while <continuationCondition> :
#       do main action to be repeated
#       prepare variables for the next time through the loop
#*****************************************************************************************************************

#Example 1:

# Suppose you are playing an adventure game and you have to make a choice for your character to either run or walk.
# Write a short code segment that asks the user if they want to run or walk; however,
# You should keep asking them until they type in one of the two valid answers
# EXTENSION: you should allow the user to enter all variations of "walk" and all variations of "run"
# eg. WALK, wALk, Walk, etc.

'''
ans = input("Choose to run or walk\n")
while ans.lower() != "walk" and ans.lower() != "run":
    ans = input("invalid answer\n")
    print("please choose run or walk!")
if ans.lower() == "walk":
    print ("You are walking!")
else:
    print ("You are running!")
'''

#***************************************************************************************************************
#Example 2:

# 1) Write a code segment that generates a random number between 1 and 10 and stores it in a variable.
# 2) You should then asks the user to try and guess the number by asking them to input an integer between 1 and 10
# 2) If the user enters an invalid number that is not between 1 and 10, you should continue to ask them to enter an
#    integer until a valid number is entered
# 5) You should then print "Congrats, you guessed the right number" if they guess the correct number or "Sorry, incorrect
#    guess." if they guess the wrong number.
'''
import random
ans = random.randrange(1,10)
guess = int(input(""))
while guess <1 or guess > 10:
    guess = int(input(""))
if guess == ans:
    print("You guessed right!")
else:
    print("You guessed wrong!")
'''
#****************************************************************************************************************
#Example 3:

# Write a program that continually asks the user to enter an integer value. However, once the user enters 0, they
# are no longer asked to enter any more values.
# Once all inputs are taken, it prints out the sum of all of the values have been entered
'''
ans = int(1)
sum = 0
while ans != 0:
    ans = float(input(""))
    sum = sum + ans
print(sum)
'''
#****************************************************************************************************************
#Example 4:

# Write a program that does the exact same thing as Example 3
# Once all inputs are taken, it prints out the sum of all of the values that have been entered AND
# it also prints out the average of all of the values that have been entered
'''
ans = 1
sum = 0
count = -1
while ans != 0:
    ans = float(input(""))
    sum = sum + ans
    count = count + 1
print(sum)
print(sum/count)
'''
#****************************************************************************************************************
#Example 5:

# Write a program that continues to ask the user to enter a string until they enter a string that begins with the letter "a"
# The program should print out a final string that consists of the last two letters of every string that was entered
# Example: If the user enters "cat" then "muffin" and then "art", then "atinrt" would be printed out.

# Extension 1: if the word is less than 2 letters long, attach the entire word to the final string
# Extension 2: do not include the last two letters of the final word that was entered
'''
str = ("  ")
last = ("")
while str[0] != "a":
    str = input("")
    if len(str) >= 2:
        last=last+str[-2]+str[-1]
    else:
        last=last+str
print(last[:-2])
'''
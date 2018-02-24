#Bill Zhang
#March.28.2017
#Python3 Tools Class

#listMax
#finds the largest value in a list
def listMax(list):
    maxval = list[0]
    for i in range (1, len(list), 1):
        maxval = max(maxval, list[i])
    return maxval
#same as max(list)
list = (1, 2, 3, 4, 5, -1, -2, -3, -4)

#matchFirstTwo
#returns true if first two elements are matching
def matchFirstTwo(list):
    if len(list < 2):
        return False
    if list[0] == list [1]:
        return True
    return False

#moddedSum
#returns the sum of every second value
def moddedSum(list):
    sum = 0
    for i in range(0, len(list), 2):
        sum = sum+list[i]
    return sum

#adjacentReturn(list, n):
#returns all values adjacent to n in list
def adjacentCheck(list, n):
    ans = []
    if len(list)<  2:
        return []
    if list[0] == n:
        ans.append(list[1])
    for i in range(1, len(list)-1,1):
        if list[i] == n:
            ans.append(list[i-1]+list[i+1])
    if len(list) == 2:
        if list[1] == n:
            ans.append(list[0])
    return (ans)

#firstAndLastB
#return the first and last letters of each element in reverse order
def firstAndLastB():
    str = ""
    for i in range(len(list)-1,-1,-1):
        word = list(i)
        str = str+word[0]+word[-1]
    return str

#splitRaw
#same as split()
def splitRaw(str, split):
    strList = []
    start = 0
    for i in range(len(str)):
        if str[i] == split:
            e = i
            strList.append(str[start:e])
            start = e + 1
    strList.append(str[start:(len(str))])
    return strList

#randList
#makes a list with length n consisting of integers between low and high inclusive
def randList(n, low, high):
    import random
    returnlist = []
    for i in range(n):
        returnlist.append(random.randrange(low, high+1))
    return returnlist

#swap1032
#swaps the position of odd and even positions of strings
def swap1032(str):
    swap = ""
    for i in range(len(str)):
        if i%2 == 1:
            swap = swap + str[i] + str[i-1]
    return swap

#isPalindrome
#checks if a str is the same when read from left to right and right to left
def isPalindrome(str):
    for i in range(len(str)//2):
        if str[i] != str[-i-1]:
            return False
    return True

#reverseList(list)
#reverses the list
def reverseList(list):
    rev = []
    for i in range(len(list)):
        rev.append(list[-i-1])
    print(rev)

#intInput
#makes sure an input is an int and prevents crash if it is not
def intInput(prompt, error_message):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            return(error_message)

#writeToFile(fileName, list)
#writes a list to a file
def writeToFile(fileName, list):
    file = open(fileName, "w")
    file.write(str(list))

#removeElement(list, n)
#remove n from list
def removeElement(list, n):
    rtn = []
    for i in range(len(list)):
        if list[i] != n:
            rtn.append(list[i])

#countMaxBlock
#counts the max streak of the same letters
def countMaxBlock(str):
    if len(str) == 0:
        return "0"
    if len(str) == 1:
        return "1"
    ltr = str[0]
    count = 0
    streaks = []
    end = 0
    for i in range(len(str)):
        if str[i] == ltr:
            count = count + 1
        else:
            streaks.append(count)
            count = 1
            ltr = str[i]
        if i == len(str) - 1:
            streaks.append(count)
    for i in range(len(streaks)):
        end = max(end, streaks[i])
    return end

#countMaxBlock2
#countMaxBlock with only one loop
def countMaxBlock2(str):
    if len(str) == 0:
        return "0"
    if len(str) == 1:
        return "1"
    ltr = str[0]
    count = 0
    end = 0
    for i in range(len(str)):
        if str[i] == ltr:
            count = count + 1
        else:
            end = max(end, count)
            count = 1
            ltr = str[i]
        if i == len(str) - 1:
            end = max(end, count)
    return end

#randomNumber
#returns a random int between 2 ints, inclusive
def randomNumber():
    import random
    while True:
        a = int(input("Min: "))
        b = int(input("Max: "))
        print(random.randrange(a, b+1))

#count
#counts from start to int by add
def count(start, int, add):
    int = abs(int)
    while start < int + 1:
        print(start)
        start = start + add

#testAnswer
#while the answer is wrong, repeat again, takes 2 strings, prints results as strings
def testAnswer(question, answer):
    while True:
        print(question)
        res = input("")
        if res == answer:
            print("Correct!")
            return
        print("Try again.")
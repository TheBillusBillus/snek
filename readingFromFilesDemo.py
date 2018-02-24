nameFile = open("names.txt", "r")

nameContent = nameFile.read()#will read all of names.txt
nameListMain = nameContent.split("|")
nameListTest = []
start = 0
count = 0
for i in range(len(nameContent)):
    if nameContent[i] == "|":
        count = count+1
for i in range(len(nameContent)):
    if nameContent[i] == "|":
        e = i
        nameListTest.append(nameContent[start:e])
        start = e + 1
nameListTest.append(nameContent[start:(len(nameContent))])
print(count)
print(nameContent)
print(nameListMain)
print(nameListTest)
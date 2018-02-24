k = int(input())
data = {}
for i in range(k):
    data[i] = input().split(" ")
for i in range(k):
    for j in range(k):
        data[i][j] = int(data[i][j])

xdif = data [0][k-1] - data[0][0]
ydif = data [k-1][0] - data[0][0]

output = {}
dataout = {}
for i in range(k):
    output[i] = ""
    dataout[i] = {}

if xdif > 0 and ydif > 0: #case 1 x pos y pos
    dataout = data

elif xdif < 0 and ydif < 0: #case 3 x neg y neg
    for x in range(k):
        for y in range(k):
            dataout[x][y] = data[k-x-1][k-y-1]


elif xdif < 0 and ydif > 0: #case 4 x pos y neg
    #print("c4")
    for x in range(k):
        for y in range(k):
            dataout[x][y] = data[y][k-x-1]
elif xdif > 0 and ydif < 0: #case 2 x neg y pos
    #print("c2")
    for x in range(k):
        for y in range(k):
             dataout[x][y] = data[k-y-1][x]

for i in range(k):
    for j in range(k):
        output[i] = output[i] + str(dataout[i][j]) + " "

for i in range(k):
    print(output[i])


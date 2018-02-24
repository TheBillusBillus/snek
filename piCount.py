pifile = open("pimil.txt", "r")
pi = pifile.read()
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(pi)):
    for j in range(10):
        if int(pi[i]) == j:
            count[j] = count[j] + 1
            print(str(pi[i]))
print(count)
print(len(pi))
print(sum(count))
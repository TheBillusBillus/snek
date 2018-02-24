#opens file "scores.txt" and "w" define will it will do to it
scoreFile = open("scores.txt", "w")

name = input("Enter Your Username: ")

scoreFile.write(name)
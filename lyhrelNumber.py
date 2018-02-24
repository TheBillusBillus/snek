def palindrome(int):
    string = str(int)
    for i in range((len(string))//2):
        if string[i] != string[-i-1]:
            return False
    return True

def run(x):
    if palindrome(x) == False:
        add = ""
        for i in range(len(x)):
            add = add+x[-i-1]
        x = str(int(x)+int(add))
        print(x)
        run(x)
    return

def main():
    start = input("Starting Number: ")
    run(start)
    print("Palindrome found!\n\n\n")
    main()
main()
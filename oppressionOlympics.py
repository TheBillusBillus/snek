def main():
    run = True
    while run == True:
        game()
        runStr = input("Would you like to play again? (Y/N): ")
        if runStr.lower() == "n" or runStr.lower() =="no":
            run = False

def printls(list):
    for i in range(len(list)):
        print(list[i])

def game():
    intro = "Welcome to the Opprhttps://me.me/i/anonymous-id-svtk8oi9-2-02-16-16-live-in-australia-someone-tries-12259860ession Olympics!\nYou know the game! You know the rules! You know the drill\nNow get on with it and see how oppressed you are!"
    print(intro)

    score = 0
    rac = ["1. White", "2. Black", "3. Latino/Hispanic", "4. Native American", "5. East Asian", "6. South Asian", "7. Pacific Islander", "8. Mixed Race"]
    gen = ["1. Cisgender Male", "2. Androgynous", "3. Female Cisgender", "4. Trans (FtM)", "5. Trans (MtF)", "6. Hijra", "7. Third Gender", "8. Intersex"]
    sex = ["1. Straight", "2. Bisexual", "3. Plushies", "4. Zoophilia", "5. Object Sexuality", "6. Gay", "7. Lesbian", "8. Asexual"]
    dis = ["1. AIDS/Cancer", "2. Quad/Paraplegic", "3. Blind", "4. Alcoholic/Addict", "5. Birth Defect", "6. Mental Illness", "7. Eating Disorder", "8. Deaf"]
    rel = ["1. Protestant", "2. Catholic", "3. Atheist", "4. Buddhist", "5. Sikh", "6. Hindu", "7. Jewish", "8. Muslim"]
    soc = ["1. Homeless", "2. Incarcerated", "3. Unemployed", "4. Abuse Survivor", "5. Hopelessly in Debt", "6. High School Dropout", "7. Minimum Wage Earner", "8. Overeducated and Underemployed"]
    phy = ["1. Steroidal", "2. Tall", "3. Short", "4. Ugly", "5. Pretty", "6. Amputee", "7. Skinny", "8. Fat"]
    all = ["1. Nuts", "2. Shellfish", "3. Gluten", "4. Penicillin", "5. Bee Stings", "6. Cats/Dogs", "7. Latex", "8. Hay Fever"]

    print("\n\n")
    printls(rac)
    score = score + int(input("Race: "))
    print("\n\n")
    printls(gen)
    score = score + int(input("Gender: "))
    print("\n\n")
    printls(sex)
    score = score + int(input("Sexuality: "))
    print("\n\n")
    printls(dis)
    score = score + int(input("Disability: "))
    print("\n\n")
    printls(rel)
    score = score + int(input("Religion: "))
    print("\n\n")
    printls(soc)
    score = score + int(input("Socioeconomics: "))
    print("\n\n")
    printls(phy)
    score = score + int(input("Physique: "))
    print("\n\n")
    printls(all)
    score = score + int(input("Allergies: "))

    score = score//8
    print("\n\n\nScore: "+str(score))

    print("1 = Alex Jones/P J. Watson/Richard Spencer")
    print("2 = J. B. Peterson/Sargon/Gavin McInnes")
    print("3 = Roaming Millennial/Chris Ray Gun/Some Black Guy")
    print("4 = Milo/Blaire White/Lauren Southern")
    print("5 = Normie")
    print("6 = J. K. Rowling/Emma Watson")
    print("7 = Trigglypuff/Anita Sarkeesian")
    print("8 = Big Red/Smuggllypuff\n\n\n")

main()
print("Credits:\nEugene Wolters: GAWKER IS LITERALLY HOSTING THE OPPRESSION OLYMPICS\nhttp://www.critical-theory.com/gawker-literally-hosting-oppression-olympics/")

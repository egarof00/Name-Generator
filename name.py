from random import *

#Create the list of words you want to choose from.
i=0
firstnameList = ["Creep", "Doom", "Indominous", "Rex", "Hannibal", "Mademoiselle", "Calamity"]
lastnamelist = ["Wrecker", "Destroyer", "Thrasher", "Panther", "Cougar", "Inferno", "Crucible", "Bane", "Soul"]
#Generates a random integer.
print("Welcome to my random video game name generator!!")
start = input("Type 'go' to start!")
while i<3:
    if start == "go":
        aRandomIndex1 = randint(0, len(firstnameList)-1)
        aRandomIndex2 = randint(0, len(lastnamelist)-1)
        print((firstnameList[aRandomIndex1]) + " " + (lastnamelist[aRandomIndex2]))
        i += 1
    again = input("Want to try again? Type 'y' to get another name.")
    if again == "y":
        aRandomIndex1 = randint(0, len(firstnameList)-1)
        aRandomIndex2 = randint(0, len(lastnamelist)-1)
        print((firstnameList[aRandomIndex1]) + " " + (lastnamelist[aRandomIndex2]))
        i += 1
        break

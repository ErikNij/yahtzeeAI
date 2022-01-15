from random import seed
from random import randint

NumberOfDie = 5


# A function that creates N random ints and returns them in an array
def ListOfRandNumbs(NumbOfRandNumbs):
    ListNumbs = [0]*NumbOfRandNumbs
    for i in range(0, NumbOfRandNumbs):
        ListNumbs[i] = randint(1, 6)
    return ListNumbs


def RRDice(OldRole):  # Function that asks and re reolls some dice
    ReRollStr = input(
        "Which dice would you like to re roll? Please number the dice 1-5 with no spaces.")
    #  Asking which dice want to be re rolled.
    #  determining how many dice are being re rolled
    numbOfReRollDice = len(ReRollStr)
    # getting new rand numbs for the dice
    NewDice = ListOfRandNumbs(numbOfReRollDice)
    NewRole = OldRole
    # extracting which dice are being rolled
    ReRollDiceNumbers = [0]*numbOfReRollDice
    for i in range(0, numbOfReRollDice):
        # putting the dice indices into an array
        ReRollDiceNumbers[i] = int(ReRollStr[i])-1
        NewRole[ReRollDiceNumbers[i]] = NewDice[i]
    return NewRole


Role1 = ListOfRandNumbs(NumberOfDie)
print(Role1)

Role2 = RRDice(Role1)
print(Role2)
Role3 = RRDice(Role2)
print(Role3)

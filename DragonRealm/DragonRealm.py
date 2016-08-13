import random
import time

def displayIntro():
    print("You walk into a forest and find some caves")

def chooseCave():
    choice = ''
    while choice!='1' and choice!='2':
        print("You see two caves in front of you,choose one:")
        choice = input()
        print (choice)
    return choice


def checkCave(choice):
    print("The dragon comes close to you")
    goodDragon = random.randint(1,2)
    time.sleep(2)
    if choice==str(goodDragon):
        print("You got treasure")
    else:
        print("You have been eaten")

playAgain = 'yes'
while playAgain=='yes' or playAgain=='y':
    displayIntro()
    choice = chooseCave()
    checkCave(choice)
    print("Play again? (Yes/No)")
    playAgain = input().lower()


import random

print("Hello, what is your name?")
name = input()

guesses = 0
number = random.randint(1,20)
print(number)
print("Hello, %s! Do you want to play a game?"%name)
print("Great, Im thinking of a number between 1 to 20!")
while guesses<5:
    print("What is your guess?")
    answer = int(input())
    guesses+=1
    if answer>number:
        print("Your guess is too high, Try again!")
    if answer<number:
        print("Your guess is too low, Try again!")
    if answer==number:
        break
if answer==number:
    print("Correct, the number was: "+str(number))
if answer!=number:
    print("Loser, the number was: "+str(number))

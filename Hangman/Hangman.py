import random

HANGMANPICS = ['''
                                            o========XX
                                              |      ||
                                                     ||
                                                     ||
                                                     ||
                                                     ||
                                                     ||
                                                     ||
                                                     ||
                                                     ||
                                            |========||
                                            |========XX
                                            ''','''
                                            o========XX
                                              |      ||
                                            (0_0)    ||
                                                     ||
                                                     ||
                                                     ||
                                                     ||
                                                     ||
                                                     ||
                                                     ||
                                            |========||
                                            |=========X
                                            ''','''
                                            o========XX
                                              |      ||
                                            (0_0)    ||
                                              |      ||
                                              |      ||
                                                     ||
                                                     ||
                                                     ||
                                                     ||
                                                     ||
                                            |========||
                                            |=========X
                                            ''','''
                                            o========XX
                                              |      ||
                                            (0_0)    ||
                                              |      ||
                                           o--|      ||
                                           |  |      ||
                                           x         ||
                                                     ||
                                                     ||
                                                     ||
                                                     ||
                                            |========||
                                            |=========X
                                           ''','''
                                            o========XX
                                              |      ||
                                            (0_0)    ||
                                              |      ||
                                           o--|--o   ||
                                           |  |  |   ||
                                           x  |  x   ||
                                                     ||
                                                     ||
                                                     ||
                                                     ||
                                            |========||
                                            |=========X
                                            ''','''
                                            o========XX
                                              |      ||
                                            (0_0)    ||
                                              |      ||
                                           o--|--o   ||
                                           |  |  |   ||
                                           x  |  x   ||
                                              |      ||
                                            /        ||
                                           /         ||
                                                     ||
                                            |========||
                                            |=========X
                                            ''','''
                                            o========XX
                                              |      ||
                                            (0_0)    ||
                                              |      ||
                                           o--|--o   ||
                                           |  |  |   ||
                                           x  |  x   ||
                                              |      ||
                                            /   \    ||
                                           /     \   ||
                                                     ||
                                            |========||
                                            |=========X
                                            ''','''
                                            o========XX
                                              |      ||
                                            (x_x)    ||
                                              |      ||
                                           o--|--o   ||
                                           |  |  |   ||
                                           x  |  x   ||
                                              |      ||
                                            /   \    ||
                                           /     \   ||
                                                     ||
                                            |========||
                                            |=========X
                                             ''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog ' \
        'donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose ' \
        'mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon ' \
        'seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle ' \
        'weasel whale wolf wombat zebra'.split()

def getRandomWords(wordsList):
    wordIndex = random.randint(0,len(wordsList)-1)
    #print(wordsList[wordIndex])
    return wordsList[wordIndex]

def displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:',end=' ')
    for letter in missedLetters:
        print(letter,end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i]+secretWord[i]+blanks[i+1:]
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuessed(alreadyGuessed):
    while True:
        print("Guess a letter:")
        guess = input().lower()
        if len(guess)!=1:
            print("Please enter a single letter")
        elif guess in alreadyGuessed:
            print("Letter already guessed, choose again!")
        elif guess not in 'abcdefghijklmnopqurstuvwxyz':
            print("Please guess a LETTER")
        else:
            return guess

def playAgain():
    print("Do you want to play again?(yes/no)")
    return input().lower().startswith('y')


hangman = ['''
                         ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █
                        ▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █
                        ▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
                        ░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
                        ░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
                         ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒
                         ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
                         ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░
                         ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░

''']
print(hangman[0])

gameover = ['''
                          ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
                         ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
                        ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
                        ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
                        ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
                         ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
                          ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
                        ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
                              ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░
                                                                             ░
''']


missedLetters=''
correctLetters=''
secretWord = getRandomWords(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
    guess = getGuessed(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters+guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Yay, you guessed the word.\n The secret word is:"+secretWord+" \nYou have won!")
            gameIsDone = True
    else:
        missedLetters = missedLetters+guess
        if len(missedLetters)==len(HANGMANPICS)-1:
            displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
            print(gameover[0])
            print("\nWrong Guesses:"+str(len(missedLetters))+
                  " \nCorrect Guesses:"+str(len(correctLetters))+" \nSecret Word:"+secretWord+"")
            gameIsDone=True

    if gameIsDone:
        if playAgain():
            missedLetters=''
            correctLetters=''
            secretWord=getRandomWords(words)
            gameIsDone=False
        else:
            break
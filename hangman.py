import random

HANGMAN_PICS=["""

    +---+
        |
        |
        |
       === ""","""

    +---+
    O   |
        |
        |
       === ""","""

    +---+
    O   |
    |   |
        |
       === ""","""

    +---+
    O   |
   /|   |
        |
       === ""","""

    +---+
    O   |
   /|\  |
        |
       === """, """

    +---+
    O   |
   /|\  |
   /    |
       === """, """

    +---+
    O   |
   /|\  |
   / \  |
       === """
]



        

words = """ant baboon badger bat bear beaver camel cat clam cobra cougar
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt otter owl panda
parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
skunk sloth snake spider stork swan tiger toad trout turkey turtle
weasel whale wolf wombat zebra""".split()

def getRandomWord(Wordlist):
    word=Wordlist[random.randint(0,len(Wordlist)-1)]
    return word



def displayBoard(missedLetters,correctLetters,secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    


    print("Missed letters:",end=" ")
    for letter in missedLetters:
        print(letter,end='')
    
    print()

    blanks='_ '*len(secretWord)
    
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks=blanks[:i]+secretWord[i]+blanks[i+1:]
           

    for letter in blanks:
        print(letter,end="")

    print()



def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter....')
        guess=input()
        guess=guess.lower()

        if len(guess)!=1:
            print("Kindly enter a single letter.")

        elif guess in alreadyGuessed:
            print("You have already guessed that letter.Choose again.")

        elif guess not in 'abcdegfhijklmnopqrstuvwxyz':
            print("Kindly enter a letter.")

        else:
            return guess


def playAgain():
    print("Would you like to play again?(yes or no)")
    return input().lower().startswith('y')













print('******HANGMAN******')
missedLetters=""
correctLetters=""
secretWord=getRandomWord(words)

gameIsDone=False

while True:
    displayBoard(missedLetters,correctLetters,secretWord)

    #Allows player to enter the letter
    guess=getGuess(correctLetters+missedLetters)
    
    if guess in secretWord:
        
        correctLetters=correctLetters+guess
      
       
    
    # to check if player has won the game
        foundAllLetters=True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters=False
                break
        
        
        if foundAllLetters:
            print("You won boss!.."+ "here's is your secret word->"+secretWord)
            gameIsDone=True

    else:
        missedLetters=missedLetters+guess

        # to check if players has guessed too many times and lost

        if len(missedLetters)==len(HANGMAN_PICS)-1:
            displayBoard(missedLetters,correctLetters,secretWord)
            print("You have run out of guesses!\n After"+
               str(len(missedLetters))+" missed guesses and "+
               str(len(correctLetters))+"correct guesses",
               "word was "+secretWord)
            gameIsDone=True


    #Asking player if they wanna play again
    if gameIsDone:
        if playAgain():
            missedLetters=""
            correctLetters=""
            secretWord=getRandomWord(words)
            gameIsDone=False

        else:
            print("Thanks for playing...")
            break




















from random import choice

def getRandomWord():
    wordlist="""ant baboon badger bat bear beaver camel cat clam cobra cougar
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt otter owl panda
parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
skunk sloth snake spider stork swan tiger toad trout turkey turtle
weasel whale wolf wombat zebra""".split()
    return choice(wordlist)



def display(missedLetters,correctLetter,hiddenWord):
   
    global wongame
    if missedLetters:
        print("missed",end=" ")
        for letter in missedLetters:
            
            print(letter,end=" ")

    blanks=[]
    for letter in hiddenWord:
        if letter in correctLetter:
            blanks.append(letter)
        else:
            blanks.append("_")

    print("\n")
    print(" ".join(blanks))
    print("\n")

    

    
        



def takeInput(usedLetters):
    print("Guess a letter")
    while True:
        letter=input().lower()
        if len(letter)!=1:
            print("Enter single letter")

        elif letter in usedLetters:
            print("You have already used up that letter. Pick another one")

        
        elif letter not in "abcdefghijklmnopqrstuvwxyz":
            print("letter cannot be special character or any other character !")

        else:
            return letter


def playGame():
    print("you wanna play the game again (y/n)?")
    return input().lower().startswith('y')

missedLetters=""
correctLetters=""
hiddenWord=getRandomWord()
gameIsDone=False


def main():
    global missedLetters,correctLetters,hiddenWord,gameIsDone
    display(missedLetters,correctLetters,hiddenWord)
    while True:
        guess=takeInput(missedLetters+correctLetters)
        
        if guess in hiddenWord:
            correctLetters+=guess
            display(missedLetters,correctLetters,hiddenWord)

            foundAllLetters=True
            for letter in hiddenWord:
                if letter not in correctLetters:
                    foundAllLetters=False
                    break

            if foundAllLetters:
                print("You won boss!.."+ "here's is your secret word->"+hiddenWord)
                gameIsDone=True

        else:
            missedLetters+=guess
            display(missedLetters,correctLetters,hiddenWord)
            if len(missedLetters+correctLetters)==6:
                print("You ran out of 6 chances")
                gameIsDone=True

        if gameIsDone:
            if playGame():
                missedLetters=""
                correctLetters=""
                hiddenWord=getRandomWord()
                gameIsDone=False
            else:
                print("Thanks for playing do come again!")
                break
        
    
  





if __name__=="__main__":

    main()

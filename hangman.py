import re
import random
from asciiHangmans import hangmans
from words import wordList

def getBooleanResponse():
    yesResponses = [ "y", "yes", "yup" ]
    noResponses = [ "n", "no", "nope" ]
    
    getInput = True

    response = input().lower()
    
    while getInput:
        if response in yesResponses:
            return True
        elif response in noResponses:
            return False
        else:
            print("Sorry, I couldn't understand your response. Please respond with y (for yes) or n (for no).")
            response = input().lower()

def printGuesses(correctGuesses, incorrectGuesses):
    print(
        "Correct Guesses:",
        "none" if len(correctGuesses) == 0 else ", ".join(correctGuesses)
    )
    
    print(
        "Incorrect Guesses:",
        "none" if len(incorrectGuesses) == 0 else ", ".join(incorrectGuesses)
    )

def randomWord():
    return random.choice(wordList)

def showLetter(word, hangman, displayLetter):
    displayLetterLower = displayLetter.lower() # lowercase the letter
    # note: in this program, the letter is always lowercase before even being passed to the function, but I'm calling .lower() again as to not confuse other programmers, among other reasons
    
    # replace all occurrences of the guess in the hangman variable
    return "".join([letter if letter.lower() == displayLetterLower else hangman[i] for i, letter in enumerate(word)])

def printGame(hangman, triesLeft, blankChar, correctGuesses, incorrectGuesses):
    formatted = "".join([
        " "+blankChar if letter == blankChar and i >= 1 and hangman[i-1] == blankChar
        else " "*3 if letter == " " and (hangman[i-1] == blankChar or hangman[i+1] == blankChar)
        else letter
        for i, letter in enumerate(hangman)
    ])

    printGuesses(correctGuesses, incorrectGuesses)
    
    print(hangmans[triesLeft])
    
    print(formatted)

def startGame():
    blankChar = "_"

    word = randomWord();
    hangman = blankChar*len(word)

    noGuess = [ " ", "!", ".", ",", "'", "\"", ":", ";" ] # characters that don't need to be guessed show up in the word by default

    alreadyGuessed = []
    correctGuesses = []
    incorrectGuesses = []
    
    triesLeft = 6

    for char in noGuess:
        hangman = showLetter(word, hangman, char)

    printGame(hangman, triesLeft, blankChar, correctGuesses, incorrectGuesses)

    while hangman != word and triesLeft != 0:
        print()
        print("Guess a letter.")
        
        guess = input().lower()
        guessLen = len(guess)

        if guessLen == 0:
            print("You must provide a character to guess!")
        elif guessLen > 1:
            print("Just to confirm: You would like to guess that the word/phrase is \"" + guess + "\"? (y/n)")

            confirmation = getBooleanResponse()

            if confirmation:
                if (guess == word.lower()):
                    hangman = word
                else:
                    triesLeft -= 1
                    print("Good guess, but that isn't the solution!")
                print()
                printGame(hangman, triesLeft, blankChar, correctGuesses, incorrectGuesses)
            else:
                print("Okay, I'll disregard your guess.")
        elif guess in noGuess:
            print("You can't guess that letter!")
        elif guess in alreadyGuessed:
            print("You've already guessed that letter!")
        else:
            alreadyGuessed.append(guess)
            
            if guess not in word.lower():
                incorrectGuesses.append(guess)
                triesLeft -= 1
                print("That letter is not in the word!")
            else:
                correctGuesses.append(guess)
                hangman = showLetter(word, hangman, guess)

            print()

            if hangman == word:
                print("Congratulations! You guessed all the letters in the word!")
            else:
                printGame(hangman, triesLeft, blankChar, correctGuesses, incorrectGuesses)

        if triesLeft == 0:
            print();
            print("Uh oh! You ran out of tries. The word/phrase was \"" + word + ".\" Better luck next time!")

def main():
    print("Welcome to hangman! I'll give you a word/phrase and you can try to guess it!")
    print()

    play = True
    
    while play:
        startGame()

        print()
        print("Would you like to play again? (y/n)")

        playAgain = getBooleanResponse();

        if playAgain:
            play = True
            print("Okay! Good luck!")
        else:
            play = False
            print("Alright, see you around!")

if __name__ == "__main__":
    main()

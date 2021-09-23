countries = ['canada', 'mexico', 'france']
guessedLetters = []
guessesLeft = 10

def pickWord():
    country = countries[1] # figure out how to pick randomly
    return country
    
    
    global secretWord
    secretWord = ['m', 'e', 'x', 'i', 'c', 'o']
    # come back to this later so that the program does it itself
    
def createWordDisplay():
    global displayWord
    displayWord = []
    for i in range(len(country)):
        displayWord.append('*')
        
    global 

def welcome(country):
    print('Welcome to Hangman')
    print('The word is ' + str(len(country)) + ' letters long, and the theme is countries.')

def enterGuess():
    guess = input('Guess a letter: ')
    return guess

def checkForCorrectGuess(guess, country):
    guessedCorrect = False
    for i in range(len(country)):
        if country[i] == guess:
            guessedCorrect = True
        
    if guessedCorrect:
        print('Your guess is correct!') 
    else:
        print('Your guess is incorrect.')

    updateGuesses(guess)
    displayGuesses()

def updateGuesses(guess):
    global guessedLetters
    guessedLetters.append(guess)
    global guessesLeft
    guessesLeft -= 1
    # fill in guessed letters
    
def displayGuesses():
    print('You have guessed: ')
    print(guessedLetters)
    print('You have ' + str(guessesLeft) + ' guesses left.')
    # something to display progress in word - will probably help with ending the game when the whole word is guessed

def runGame():
    while guessesLeft > 0: # or entire word is guessed
        guess = enterGuess()
        
        if guess in guessedLetters:
            print('You already guessed that.')
            displayGuesses()
        else:
            checkForCorrectGuess(guess, country)
        # end when word is guessed/guesses run out - only stops when guesses run out
    
country = pickWord()
createWordDisplay()
welcome(country)
runGame()
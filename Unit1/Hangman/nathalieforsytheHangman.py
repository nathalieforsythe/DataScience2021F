countries = ['canada', 'mexico', 'france', 'portugal', 'germany', 'denmark']
guessedLetters = []
guessesLeft = 10

def pickWord():
    country = countries[3] # figure out how to pick randomly
    return country
    
def createWordDisplay():
    global displayWord
    displayWord = []
    for i in range(len(country)):
        displayWord.append('*')
        
    global secretWord
    secretWord = []
    for i in range(len(country)):
        secretWord.append(country[i])

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
        fillInLetters(guess)
    else:
        print('Your guess is incorrect.')

    updateGuesses(guess)
    displayGuesses()

def updateGuesses(guess):
    global guessedLetters
    guessedLetters.append(guess)
    global guessesLeft
    guessesLeft -= 1
    
def fillInLetters(guess): 
    for i in range(len(secretWord)):
        if secretWord[i] == guess:
            displayWord[i] = guess
    print(displayWord)
    
def displayGuesses():
    print('You have guessed: ')
    print(guessedLetters)
    print('You have ' + str(guessesLeft) + ' guesses left.')

def runGame():
    while guessesLeft > 0 or secretWord != displayWord: 
        guess = enterGuess()
        if secretWord == displayWord: # this doesn't work
            gameOver()
        elif guess in guessedLetters:
            print('You already guessed that.')
            displayGuesses()
        else:
            checkForCorrectGuess(guess, country)
        
def gameOver():
    if displayWord == secretWord:
        print('Congratulations! You guessed the word: ' + country)
    elif guessesLeft == 0:
        print('Oh no! You are all out of guesses. The word was: ' + country)
    
country = pickWord()
createWordDisplay()
welcome(country)
runGame()
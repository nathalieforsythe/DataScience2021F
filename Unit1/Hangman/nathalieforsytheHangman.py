countries = ['canada', 'mexico', 'france'] # strip, lower? (in pickWord)
guessedLetters = []
guessesLeft = 10

def runGame():
    country = pickWord()
    welcome(country)
    while guessesLeft > 0: # or entire word is guessed
        guess = enterGuess()
        if guess in guessedLetters:
            print('You already guessed that.')
        elif guess not in guessedLetters:
            checkForCorrectGuess(guess, country)
        if guess not in country:
            print('Your guess is incorrect.') 
        updateGuesses(guess)
        # end when word is guessed/guesses run out - stops when guesses run out

def pickWord():
    country = countries[0] # figure out how to pick randomly
    return country

def welcome(country):
    print('Welcome to Hangman')
    print('The word is ' + str(len(country)) + ' letters long, and the theme is countries.')

def enterGuess():
    guess = input('Guess a letter: ')
    return guess
    
def checkForCorrectGuess(guess, country):
    for i in range(len(country)):
        if country[i] == guess:
            print('Your guess is correct!')
        
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
    
runGame()
countries = ['Canada', 'Mexico', 'France']
guessedLetters = []
guessesLeft = 10

def runGame():
    country = pickWord()
    welcome(country)
    while guessesLeft > 0: # or entire word is guessed
        guess = enterGuess()
        checkGuess(guess, country)
        # end when word is guessed/guesses run out

def pickWord():
    country = countries[1] # figure out how to pick randomly
    return country

def welcome(country):
    print('Welcome to Hangman')
    print('The word is ' + str(len(country)) + ' letters long, and the theme is countries.')

def enterGuess():
    guess = input('Guess a letter: ')
    guessedLetters.append(guess)
    return guess
    
def checkGuess(guess, country):
    for i in range(len(country)):
        x = country[i]
        if x == guess:
            print('Your guess is correct!')
        elif x != guess:
            print('Your guess is incorrect.')
        else:
            print('You already guessed that.')
        
def updateGuesses():
    global guessesLeft
    guessesLeft -= 1
    # fill in guessed letters
        
def displayGuesses():
    print('You have guessed: ')
    print(guessedLetters)
    print('You have ' + str(guessesLeft) + ' guesses left.')
    
runGame()
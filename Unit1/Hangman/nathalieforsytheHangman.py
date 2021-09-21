countries = ['Canada', 'Mexico', 'France']
guessedLetters = []
guessesLeft = 10

def runGame():
    pickWord()
    welcome()
    # while loop:
        # enterGuess()
        # checkGuess()
        # end when word is guessed/guesses run out
    pass

def pickWord():
    country = countries[1] # figure out how to pick randomly

def welcome():
    print('Welcome to Hangman')
    print('The word is ' + len(country) + 'letters long, and the theme is countries.')

def enterGuess():
    guess = input('Guess a letter: ')
    guessedLetters.append(guess)
    
def checkGuess():
    for letter in guessedLetters:
        if guess == true:
            print('Your guess is correct!')
            displayGuesses()
        elif guess == false:
            print('Your guess is incorrect.')
            displayGuesses()
        else:
            print('You already guessed that.')
        displayGuesses()
        enterGuess()
        
def updateGuesses():
    guessesLeft -= 1 # local variable? for some reason 
    
    
def displayGuesses():
    print('You have guessed: ')
    print(guessedLetters)
    print('You have ' + guessesLeft + 'guesses left.')

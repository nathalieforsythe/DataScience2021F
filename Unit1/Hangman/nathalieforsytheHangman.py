countries = ['Canada', 'Mexico', 'France']
guessedLetters = []
guessesLeft = 10

def runGame():
    pickWord()
    welcome()
    
    # while loop:
        # enterGuess
        # checkGuess
        # end when word is guessed/guesses run out

def pickWord():
    # country = random country
    # pick a random word from countries list
    pass

def welcome():
    print('Welcome to Hangman')
    print('The word is ' + len(country) + 'letters long, and the theme is countries.')

def enterGuess():
    guess = input('Guess a letter: ')
    guessedLetters.append(guess)
    print(guessedLetters)
    
def checkGuess():
    for letter in guessedLetters:
        if guess == true:
            print('Your guess is correct!')
            displayGuesses()
            displayGuessesLeft()
        elif guess == false:
            print('Your guess is incorrect.')
            displayGuesses()
            displayGuessesLeft()
        else:
            print('You already guessed that.')
        displayGuesses()
        enterGuess()
        
def displayGuessesLeft():
    guessesLeft -= 1 # local variable? for some reason 
    print('You have ' + guessesLeft + 'guesses left.')
    
def displayGuesses():
    print('You have guessed: ')
    print(guessedLetters)

enterGuess()

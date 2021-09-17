def names(firstname):
    p = prefix()
    print('Hello, ' + p + ' ' + firstname)
    lastname = input('What is your last name? ')
    print('Well, nice to meet you, ' + firstname + ' ' + lastname)
    
def prefix():
    return "Miss"
    
names('Nathalie')
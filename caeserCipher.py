# This is a simple program that encrypts a text using the ceasar cipher algorithm
print('''
########################################################################
# This program encrypts a given text using the caesar cipher algorithm #
########################################################################
''')

def caesarAlgorithm(letter,key,alphabets):
    '''
    Encrypts 'letter' by shifting it's position based on the value of 'key'
    '''
    
    # Checks if the letter is a part of 'alphabets'
    # i.e numbers and symbols are ignored
    if letter in alphabets:
        
        # Gets current index of the letter in alphabets
        shift = alphabets.index(letter)
        
        # Shift position
        shift += key
        
        # New position
        position = shift % len(alphabets)
        
        # Returns the new position
        return alphabets[position]

def main():
    # Enter the text to encrypt
    plainText = input('Enter text: ')
    
    # Enter the key to use for encryption
    key = int(input('Enter Key: '))

    # Creates an empty variable where the encrypted text will be stored
    cipherText = str() 
    
    # The alphabets are used to define the keyspace for this algorithm,
    # written in both lower and upper cases so it can also later 
    # be used in the program to ensure that the cipherText is 
    # also returned in whatever case the plaintext is entered in.
    # i.e with a key of 1, "pyt HON" will return "qzu IPO"
    lower_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    upper_letters = ('A','B','C','D','E','F','G','H','I','J','K','L','M',
                    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',)

    # Goes through every letter in the plaintext,
    # perform the condition checks and update the cipherText 
    # based on the return value of the caesarAlgorithm() function. 
    for letter in plainText:
        
        # Check if the letter is in lowercase
        if letter.islower():
            
            cipherText += caesarAlgorithm(letter,key,lower_letters)
        
        # Check if the letter is in UPPERCASE
        elif letter.isupper():
            
            cipherText += caesarAlgorithm(letter,key,upper_letters)
        
        # Check if the letter is a whiteSpace charater
        elif letter.isspace():
            
            cipherText += letter
        
    print(cipherText)
    
main()
# This is a simple program that decrypts a text that was 
# encrypted using the ceasar cipher algorithm

# Import pprint for 'prettifying' our print output
import pprint

print('''
#####################################################################################
# This program Decrypts texts that were encrypted using the caesar cipher algorithm #
#####################################################################################
''')

def reverseCeasarAlgorithm(letter,key,alphabets):
    '''
    Decrypts 'letter' by shifting it's position backward based on the value of 'key'
    '''

    # Get current index of letter in alphabets
    back_shift = alphabets.index(letter)
    
    # Shift position backwards
    back_shift -= key 
    
    # Returns the new position
    return alphabets[back_shift]

# Enter the text to decrypt
cipherText = input('Enter text: ')

# Creates an empty dictionary where the possible plaintexts will be stored
possible_Plaintexts = dict()

# The alphabets are used to define the keyspace for this algorithm,
# written in both lower and upper cases so it can also later 
# be used in the program to ensure that the cipherText is 
# also returned in whatever case the plaintext is entered in.
# i.e with a key of 1, "pyt HON" will return "qzu IPO"
lower_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

upper_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Based on the size of the keyspace,
# there are 25 possile keys for this algorithm
# Therefore we try to decrypt using each of the keys 
for key in range(1,len(lower_letters)):
    
    # Creates a temporary variable where the 
    # encrypted text will be stored for each key try
    plaintext = str()
    
    # Goes through every letter in the plaintext,
    # perform the condition checks and updates the cipherText 
    # based on the return value of the reverseCaesarAlgorithm() function.
    for letter in cipherText:

        # check if the letter is in lowercase
        if letter.islower():
            
            plaintext += reverseCeasarAlgorithm(letter,key,lower_letters)
        
        # check if the letter is in UPPERCASE
        elif letter.isupper():
            
            plaintext += reverseCeasarAlgorithm(letter,key,upper_letters)
        
        # Check if the letter is a whitespace character
        elif letter.isspace():
            
            plaintext += letter
    
    # Set the current 'key' and a default empty string
    # as a key:value pair in the dictionary "possible_Plaintexts"
    possible_Plaintexts.setdefault(key,'')
    
    # Assign the current 'plaintext' as new value to 'key' in the dictionary
    possible_Plaintexts[key] = plaintext

# pretty Print "possile_Plaintexts"
pprint.pprint(possible_Plaintexts)
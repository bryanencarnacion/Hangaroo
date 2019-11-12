import random
import string

LIST = "words.txt"
# This is just a sample file. You can input any text file.

def isWordGuessed(secretWord, lettersGuessed):
    
    count = 0
    for n, x in enumerate(secretWord):
        if x in lettersGuessed:
            count += 1
        if count == len(secretWord):
            return True
        else:
            return False
            
#For getGuessedWord

def getGuessedWord(secretWord, lettersGuessed):
    count = 0
    space = ['_']*len(secretWord)
    
    for n, x in enumerate(secretWord)
    if x in lettersGuessed:
        count += 1 
        blank.insert(count-1,x)
        blank.pop(count)
        if count == len(secretWord):
            return ''.join(str(e) for e in blank)
        else:
            count += 1 
            blank.insert(count-1,'_')
            blank.pop(count)
            if count == len(secretWord):
                return '',join(str(e) for e in blank)
#For getAvailableLetters

def getAvailableLetters(lettersGuessed)

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letter = letters[:]
    
    def removeletter(N1,N2):
        N1start = N1[:]
        for e in N1start:
            N2.remove(e)
            return ''.join(str(e) for e in N2)
            return removeletter(lettersGuessed, letter)
            
#For secretWord
secretWord = choose(wordlist).lower()
    hangaroo(secretWord):
        introduction = str(len(secretWord))
        lettersGuessed = []
        pick = str
        mistakes = 5 
        wordGuess = False
        
        print 'Hangaroo!'
        print 'The word is'
        print ('----------')
        
        while mistakes > 0 and mistake <= 5 and wordGuess is False:
            if secretWord == getGuessedword(secretWord, lettersGuessed):
                wordGuess = True
                break
            print ('You made') + str(mistakes) + (' guess left.')
            print ('These are the available letters:') + getAvailableLetters(lettersGuessed)
            pick = initial_input('Guess a letter:')
            if pick in secretWord:
                if pick in lettersGuessed:
                    print('You have already picked that letter!') + getGuessedWord(secretWord, lettersGuessed)
                    print('----------')
                    else:
                        lettersGuessed.append(pick)
                        mistakes -= 1
                        print ('The letter is not in the word:') + getGuessedWord(secretWord, lettersGuessed)
                        print ('----------')
                if wordGuess == True:
                    return 'Congratulations!'
                    elif mistakes == 0:
                        print('Sorry, you lose.. The word is') + secretWord
                        
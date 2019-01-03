import turtle
word =(input('Please enter a word that must be guessed'))
print('HIDING-WORD----------------------------------------')
Y=0
X=len(word)
wn = turtle.Screen()
Leonardo = turtle.Turtle()


def LetterGuessing(Y,X):
    WORD=" ".join(word)
    WORD=WORD.split()
    print (WORD)
    for i in range(X):
        print(X)
        LGuess= input('Please enter a letter')
        if LGuess not in WORD:
            X=X+1
            Y=Y+1
            print('Strike',Y)
            Strikes(Y,X)
        elif Y==5:
            break
        elif i==X-1:
            print ('Word Found!')
            print(word)
            break
        else:
            print('Correct Letter')
            Menu(Y)

                

def Strikes(Y,X):
    X=X+1
    if Y==1:
        Leonardo.forward(300)
        Leonardo.left(180)
        Leonardo.forward(150)
        Leonardo.right(90)
        print('Strike',Y)
        Menu(Y)
    elif Y==2:
        Leonardo.forward(300)
        Leonardo.right(90)
        print('Strike',Y)
        Menu(Y)
    elif Y==3:
        Leonardo.forward(150)
        Leonardo.right(180)
        print('Strike',Y)
        Menu(Y)
    elif Y==4:
        Leonardo.forward(75)
        Leonardo.left(90)
        Leonardo.forward(25)
        print('Strike',Y)
        Menu(Y)
    elif Y==5:
        for i in range(48):
            Leonardo.forward(1)
            Leonardo.right(7.5)

        for i in range(12):
            Leonardo.forward(1)
            Leonardo.right(7.5)
        Leonardo.left(90)
        Leonardo.forward(30)
        Leonardo.left(90)
        Leonardo.forward(30)
        Leonardo.right(180)
        Leonardo.forward(60)
        Leonardo.right(180)
        Leonardo.forward(30)
        Leonardo.right(90)
        Leonardo.forward(30)
        Leonardo.left(90)
        Leonardo.right(45)
        Leonardo.forward(60)
        Leonardo.right(180)
        Leonardo.forward(60)
        Leonardo.left(90)
        Leonardo.forward(60)
        Leonardo.right(180)
        Leonardo.forward(60)
        Leonardo.right(180)
        Leonardo.forward(60)
        print('Strike',Y)
        print('HANGMAN')
        print('GAME OVER')

    
def Guessing():
    for i in range(5):
        Guess=(input('Please enter a guess'))
        if Guess!=word:
            print('Strike',i+1)
            if i==0:
                Leonardo.forward(300)
                Leonardo.left(180)
                Leonardo.forward(150)
                Leonardo.right(90)
            elif i==1:
                Leonardo.forward(300)
                Leonardo.right(90)
            elif i==2:
                Leonardo.forward(150)
                Leonardo.right(180)
            elif i==3:
                Leonardo.forward(75)
                Leonardo.left(90)
                Leonardo.forward(25)
            elif i==4:
                for i in range(48):
                    Leonardo.forward(1)
                    Leonardo.right(7.5)
                for i in range(12):
                    Leonardo.forward(1)
                    Leonardo.right(7.5)
                    Leonardo.left(90)
                    Leonardo.forward(30)
                    Leonardo.left(90)
                    Leonardo.forward(30)
                    Leonardo.right(180)
                    Leonardo.forward(60)
                    Leonardo.right(180)
                    Leonardo.forward(30)
                    Leonardo.right(90)
                    Leonardo.forward(30)
                    Leonardo.left(90)
                    Leonardo.right(45)
                    Leonardo.forward(60)
                    Leonardo.right(180)
                    Leonardo.forward(60)
                    Leonardo.left(90)
                    Leonardo.forward(60)
                    Leonardo.right(180)
                    Leonardo.forward(60)
                    Leonardo.right(180)
                    Leonardo.forward(60)
                    print('HANGMAN')
        else:
            print('correct')
            break


            
def Menu(Y):
    print('')
    print('')
    print('The word is', len(word), "letters long")
    print('')
    for i in range (len(word)):
        print(' _ ', end='')
    print('')
    print('')
    print('Would you like to guess the whole word OR one letter?')
    print('Enter 1 for Letter guessing')
    print('Enter 2 for Word guessing')

    ans=str(input(''))
    if ans=='1':
        LetterGuessing(Y,X)
    elif ans=='2':
        Guessing()
    else:
        print('Please enter a valid option')
        Menu(Y)
   
    


Menu(Y)
            

    
    


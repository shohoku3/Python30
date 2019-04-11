#this is a guess number game

import random
secretNumber=random.randint(1,20)
print('I am thinking a number of between 1 and 20')

#Ask the player to guess 6 times
for guessesToken in range(1,7):
    print('Take a guess')
    guess=int(input())

    if guess<secretNumber:
        print('You guess is too low')
    elif guess>secretNumber:
        print('You gues is too high')
    else:
        break
        #this condition is the correct guess
if guess==secretNumber:
        print('You guess my number in '+ str(guessesToken) + ' guesses')
else:
        print('Nope The number I was thinking of was '+ str(secretNumber))

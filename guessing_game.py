       #Steps
# Ask a user to make a guess
# If not valid, print an error
#If number < guess, print too low
#If number > guess, print too high
#Else, print well done
import random
guess = 0 
number = random.randint(1,10) 
while guess != number:
    try:
        guess = int(input('Guess a number between 1 to 10: '))    
    except ValueError: 
        print('Try entering an integer')
    else: 
        if guess < number:
            print('Too low, try again')
        elif guess > number:
            print('Too high, try again')        
    
print('Congrats, you did it')

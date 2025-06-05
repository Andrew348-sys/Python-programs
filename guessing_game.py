       #Steps
# Ask a user to make a guess
# If not valid, print an error
#If number < guess, print too low
#If number > guess, print too high
#Else, print well done
import random

guess = 0 # Guess is first initialized to 0 so that the while loop runs.
number = random.randint(1,10) # This variable stores the generated number.
while guess != number: #This loop must run atleast once since the statement will always be true at first
    try:#It checks whether the guess variable will be assigned a value
        guess = int(input('Guess a number between 1 to 10: ')) #This one asks the user for a number and converts it to an int     
    except ValueError: # If the user enters an invalid value like a string, the code doesn't crash. It handles the valueerror by printing...
        print('Try entering an integer')
    else: #If there is no value error then the code proceeds below
        if guess < number:
            print('Too low, try again')
        elif guess > number:
            print('Too high, try again')
        
    
print('Congrats, you did it')#This line is executed when the while statement is false.
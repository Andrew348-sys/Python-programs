import random

#Ask user:roll dice
while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':          
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1},{die2})')        
    elif choice == 'n':
        print("Thank you for playing")
        break
    else:
        print('Invalid choice')
   
       


#If user enters; y
#Generate 2 random numbers
#print them
#Prompt user again
#If user enters; n
#print thankyou message
#Terminate
#Else
#print invalid choice

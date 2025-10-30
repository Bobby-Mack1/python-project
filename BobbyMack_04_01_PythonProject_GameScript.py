##############################################################################
########################### NUMBER GUESSING GAME##############################
##############################################################################

import random  #importing the .random package so that a random number can be selected.
low=1 #variable for the lowest number that a player can guess
high=100 #Variable for the highest number that a player can guess
attempts=0 #Variable that is later used to count the number of attempts a player has 
answer = random.randint(1, 100) #Variable that randomly is assigned a number between 1 and 100
max_guesses = 10 #Variable that is used as a placeholder for the max amount of guesses a player can take. This will change after a difficulty is selected
var=True #var , var2 and var3 are placeholder variables used to differentiate between loops and break out of 2 loops simoultaneously
var2 =1
var3 =1



#Play_again is a function that is used to determine whether the player wants to play again. 
#It is used twice in the main body of code for the game
# All -------------------- are purely for aesthetic purposes throughout
def play_again():
    #Variables were made global otherwise the variables in the function would not link to themselves outside of the function
    global var
    global answer
    global attempts
    global var2
    while True: #A while loop is used here to force the player to enter a specific input 
        print('--------------------------------------------------------------------------------------------------------------------')
        question = input('Would you like to play again? (Y/N): ').lower()
        print('--------------------------------------------------------------------------------------------------------------------')
        #if the player wants to play again
        if question == 'y':
            print()
            print()
            answer = random.randint(1, 100) #A new answer is generated and the players attempts are reset to 0
            attempts=0
            var2 = 1 # This resets the loop for the select_difficulty function which allows the player to change the difficulty each time they play.
            break
        #if the player doesn't want to play again
        elif question == 'n':
            print('--------------------------------------------------------------------------------------------------------------------')
            print('Thanks for playing!')
            print('--------------------------------------------------------------------------------------------------------------------')
            var = False #This ends the main loop that this function sits within
            break
        #if the player puts in the wrong input the loop will restart and not end until they have entered the correct input.
        else:
            print('--------------------------------------------------------------------------------------------------------------------')
            print(f'{question} is not a valid input. Please try again.') 
            print('--------------------------------------------------------------------------------------------------------------------')         
            continue

#The select_difficulty function is used to let the player decide if they want to read the rules and also select what difficulty they want to play on
def select_difficulty():
    #Variables were made global otherwise the variables in the function would not link to themselves outside of the function
    global var2
    global max_guesses
    global var3
    while var2 == 1: #While loops are used here to force the player to enter a specific input
        while var3 ==1:
            print('--------------------------------------------------------------------------------------------------------------------')
            print('Welcome to the number guessing game!')
            rules = input('Would you like to read the rules and objectives of the game? (Y/N):').lower()
            print('--------------------------------------------------------------------------------------------------------------------')
            #If the player wants to see the rules
            if rules == 'y':
                print('--------------------------------------------------------------------------------------------------------------------')
                print('The objective of the game is to guess a randomly generated whole number that lays between 1 and 100.')
                print('There are 3 difficulties available: easy- 10 guesses, medium- 7 guesses and hard- 5 guesses.')
                print('--------------------------------------------------------------------------------------------------------------------')
                break
            #If the player does not wish to see the rules
            elif rules == 'n':
                break
            #if the player puts in the wrong input the loop will restart and not end until they have entered the correct input.
            else:
                print('--------------------------------------------------------------------------------------------------------------------')
                print(f'{rules} is an invalid input. Please try again.')
                print('--------------------------------------------------------------------------------------------------------------------')
                continue
        print('--------------------------------------------------------------------------------------------------------------------')
        difficulty = input('Please input a difficulty by typing the first letter of either easy, medium or hard (E, M or H):').lower()
        print('--------------------------------------------------------------------------------------------------------------------')
        #if the player selects e
        if difficulty == 'e':
            max_guesses = 10 #sets the max number of guesses
            var2 = 0  #ends the loop
        #if the player selects m  
        elif difficulty == 'm':
            max_guesses = 7 # sets the max number of guesses
            var2 = 0   #ends the loop  
        #if the player selects h
        elif difficulty == 'h':
            max_guesses = 5 #sets the max number of guesses
            var2 = 0  #ends the loop
        #if the player puts in the wrong input the loop will restart and not end until they have entered the correct input.
        else:
            print('--------------------------------------------------------------------------------------------------------------------')
            print(f'{difficulty} is not a valid input. Please try again.')
            print('--------------------------------------------------------------------------------------------------------------------')
            continue 



####### GAME CODE #######

while var is True: #A loop is used to ensure that the player doesn't input the wrong thing
    select_difficulty() #runs the select difficulty function
    print('--------------------------------------------------------------------------------------------------------------------')
    guess=(input(f'Guess a whole number between {low} and {high}: '))
    print('--------------------------------------------------------------------------------------------------------------------')
    if guess.isdigit(): #ensures that player input is a number
        guess=int(guess) #ensures that the number is an integer
        attempts+=1 #counts the number of attempts
        if attempts < max_guesses:
            if guess < low or guess > high:
                print('--------------------------------------------------------------------------------------------------------------------')
                print('That number is out of range!')
                print(f'Your guess must be between {low} and {high}')
                print('--------------------------------------------------------------------------------------------------------------------')
            elif guess > answer:
                print('Too high! Try again!')
            elif guess < answer:
                print('Too low! Try again!')
            else:
                print('--------------------------------------------------------------------------------------------------------------------')
                print(f'Correct!!! The answer was {answer}.')
                print(f'You got the answer in {attempts} guesses!')
                print('--------------------------------------------------------------------------------------------------------------------')
                play_again()      
        else:
            print('--------------------------------------------------------------------------------------------------------------------')
            print(f'you have passed the limit of {max_guesses} guesses.')
            print(f'The answer was {answer}')
            print('--------------------------------------------------------------------------------------------------------------------')
            play_again()
    else:
        print('--------------------------------------------------------------------------------------------------------------------')
        print('Invalid guess.')
        print('--------------------------------------------------------------------------------------------------------------------')
        attempts-=1





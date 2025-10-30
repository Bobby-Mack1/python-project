import random
low=1
high=10
attempts=0
answer = random.randint(1, 10)
max_guesses = 10
var=True
var2 =1
var3 =1




def play_again():
    global var
    global answer
    global attempts
    global var2
    while True:
        print('--------------------------------------------------------------------------------------------------------------------')
        question = input('Would you like to play again? (Y/N): ').lower()
        print('--------------------------------------------------------------------------------------------------------------------')
        if question == 'y':
            print()
            print()
            answer = random.randint(1, 10)
            attempts=0
            var2 = 1
            break
        elif question == 'n':
            print('--------------------------------------------------------------------------------------------------------------------')
            print('Thanks for playing!')
            print('--------------------------------------------------------------------------------------------------------------------')
            var = False
            break
        else:
            print(f'{question} is not a valid input.')          
            continue


def select_difficulty():
    global var2
    global max_guesses
    while var2 == 1:
        while var3 ==1:
            print('--------------------------------------------------------------------------------------------------------------------')
            print('Welcome to the number guessing game!')
            rules = input('Would you like to read the rules and objectives of the game? (Y/N):').lower()
            if rules == 'y':
                print('--------------------------------------------------------------------------------------------------------------------')
                print('The objective of the game is to guess a randomly generated number that lays between 1 and 100.')
                print('There are 3 difficulties available: easy- 10 guesses, medium- 7 guesses and hard- 5 guesses.')
                print('--------------------------------------------------------------------------------------------------------------------')
                break
            elif rules == 'n':
                break
            else:
                print(f'{rules} is and invalid input. Please try again.')
                continue

        difficulty = input('Please input a difficulty by typing the first letter of either easy, medium or hard (E, M or H):').lower()
        if difficulty == 'e':
            max_guesses = 10
            var2 = 0    
        elif difficulty == 'm':
            max_guesses = 7
            var2 = 0     
        elif difficulty == 'h':
            max_guesses = 5
            var2 = 0  
        else:
            print(f'{difficulty} is not a valid input')
            continue 





while var is True:
    select_difficulty()
    print('--------------------------------------------------------------------------------------------------------------------')
    guess=(input(f'Guess a whole number between {low} and {high}: '))
    print('--------------------------------------------------------------------------------------------------------------------')
    if guess.isdigit():
        guess=int(guess)
        attempts+=1
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
                print(f'Correct!!! The answer was {answer}')
                print(f'You got the answer in {attempts} guesses.')
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





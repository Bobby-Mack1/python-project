import random
low=1
high=10
attempts=0
answer = random.randint(1, 10)
max_guesses = 10
var=True




def play_again():
    global var
    global answer
    global attempts
    while True:
        question = input('Would you like to play again? (Y/N): ').lower()
        if question == 'y':
            print()
            answer = random.randint(1, 10)
            attempts=0
            break
        elif question == 'n':
            print('Thanks for playing!')
            var=False
            break
        else:
            print(f'{question} is not a valid input.')          
            continue


    


while var is True:
    guess=(input(f'Guess a whole number between {low} and {high}: '))
    if guess.isdigit():
        guess=int(guess)
        attempts+=1

        if attempts < max_guesses:

            if guess < low or guess > high:
                print('That number is out of range!')
                print(f'Your guess must be between {low} and {high}')
            elif guess > answer:
                print('Too high! Try again!')
            elif guess < answer:
                print('Too low! Try again!')
            else:
                print()
                print(f'Correct!!! The answer was {answer}')
                print(f'You got the answer in {attempts} guesses.')
                print()
                play_again()      
        else:
            print(f'you have passed the limit of {max_guesses} guesses.')
            print(f'The answer was {answer}')
            play_again()
        
    else:
        print('Invalid guess.')





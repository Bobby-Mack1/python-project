import random
low=1
high=100
attempts=0
answer = random.randint(1, 100)


while True:
    guess=(input(f'Guess a whole number between {low} and {high}: '))
    if guess.isdigit():
        guess=int(guess)
        attempts+=1

        if attempts <5:

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
                question = input('Would you like to play again? (Y/N): ').lower()
                if question == 'y':
                    print()
                    answer = random.randint(1, 100)
                    attempts=0
                    continue
                elif question == 'n':
                    print('Thanks for playing!')
                    break
                else:
                    print(f'{question} is not a valid input. You are not allowed to play.')
                    print('Please learn how to read. Goodbye.')
                    break
        else:
            print(f"you have breached the {attempts} attempt limit and have lost")
            question = input('Would you like to play again? (Y/N): ').lower()
            if question == 'y':
                print()
                answer = random.randint(1, 100)
                attempts=0
                continue
            elif question == 'n':
                print('Thanks for playing!')
                break
            else:
                print(f'{question} is not a valid input. You are not allowed to play.')
                print('Please learn how to read. Goodbye.')
                break

                       
    
    else:
        print('Invalid guess.')





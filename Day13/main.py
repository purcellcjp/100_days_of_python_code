import random
import os
from art import logo

HARD_ATTEMPTS = 5
EASY_ATTEMPTS = 10

def return_difficulty_turns():
    response = input('Choose a difficulty. Type ''easy'' or ''hard'':').lower()
    if response == 'hard':
        return HARD_ATTEMPTS
    else:
        return EASY_ATTEMPTS    
    
    
def compare_guesses(guess, answer):
    
    if guess == answer:
        return f'You got it! The answer was {answer}'
    elif guess > answer:
        return 'Too high\nGuess again'
    else:
        return 'Too low\nGuess again'

    
def my_guessing_number_game():

    tries = 0
    number_to_guess = random.randint(1,100)    
    
    os.system('cls')
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print('I''m thinking of a number between 1 and 100.')

    # difficulty = input('Choose a difficulty. Type ''easy'' or ''hard'':').lower()
    # if difficulty == 'hard':
    #     tries = HARD_ATTEMPTS
    # else:
    #     tries = EASY_ATTEMPTS
    
    tries = return_difficulty_turns()
    
    
    while tries > 0:
        print(f'You have {tries} attempts remaining to guess the number.')
        response = int(input('Make a guess:'))
        
        status = compare_guesses(response, number_to_guess)
        print(status)
        
        if str(number_to_guess) in status:
            break
        else:
            tries -= 1
    
    if str(number_to_guess) not in status:
        print(' You''ve run out of guesses. You lost')
    
    play_again = input('Play again? Enter (y/n)').lower()
    if play_again == 'y':
        my_guessing_number_game()
        
        
        
my_guessing_number_game()

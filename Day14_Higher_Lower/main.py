import random
import os
from art import logo, vs
from game_data import data

RESPONSE_CODE_DICT = {'A':0,'B':1}


def get_comparison_item():
    res = random.choice(data)
    return res

def return_winner(choice_list):
    if choice_list[0]['follower_count'] > choice_list[1]['follower_count']:
        return 0
    else:
        return 1
    

def play_higher_lower():
    
    comp_list = []
    winner_index=-1
    player_score = 0
    
    # get first two comparisons
    comp_list.append(get_comparison_item())

    os.system('cls')
    print(logo)
        
    # keep playing until user has incorrect answer
    while True:
                
        comp_list.append(get_comparison_item())
        
        print(f'Against A: {comp_list[0]['name']}, {comp_list[0]['description']}, from {comp_list[0]['country']}')
        print(vs)
        print(f'Against B: {comp_list[1]['name']}, {comp_list[1]['description']}, from {comp_list[1]['country']}')
        resp = input('\nWho has more followers? Type ''A'' or ''B'': ').upper()
        
        # Compare followers
        winner_index = return_winner(comp_list)
        
        # did user select correctly?
        if RESPONSE_CODE_DICT[resp] == winner_index:
            player_score += 1
            os.system('cls')
            print(logo)
            print(f'You\'re right! Current score: {player_score}')
            #Update list
            comp_list[0] = comp_list[1]
            comp_list.remove(comp_list[1])
            
            
        else:
            os.system('cls')
            print(logo)
            print(f'Sorry that\'s wrong. Final score: {player_score}')            
            break   



play_higher_lower()
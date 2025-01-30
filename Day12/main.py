import random
import os
import art

def deal_card():
    """Returns random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare_scores(dealer_score, player_score):
    if dealer_score == player_score:
        return 'Draw'
    elif dealer_score == 0:
        return 'You lose - dealer has blackjack'
    elif player_score == 0:
        return 'You win - you have Blackjack'
    elif player_score > 21:
        return 'You lose - you went over 21'
    elif dealer_score > 21:
        return 'You win - dealer went over 21'
    elif player_score > dealer_score:
        return 'You win - higher score than dealer'
    else:
        return 'You lose - lower score than dealer'


def calculate_score(cards):
    # if score > 21 check for aces
    # If ace(s) are present replace 11 with 1
    score = sum(cards)
    
    # return 0 if player/cpu has blackjack on first deal
    if score == 21 and len(cards) == 2:
        return 0
    
    while cards.count(11) > 0 and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
           
    return score


def my_blackjack_game():
           
        player_cards=[]
        dealer_cards=[]
        player_score = -1
        dealer_score = -1        
        
        # Deal 2 cards to user and dealer
        for i in range(2):
            player_cards.append(deal_card())            
            dealer_cards.append(deal_card())
        
        another_card = True
        
        while another_card:
            
            # player_cards=[11,11]
            player_score = calculate_score(player_cards)
            dealer_score = calculate_score(dealer_cards)        
        
            # show cards
            print(f'\tYour cards: {player_cards}, current score: {player_score}')            
            # show dealer's first card
            print(f"\tDealer''s first card: {dealer_cards[0]}")
            
            if player_score == 0 or dealer_score == 0 or player_score > 21:
                another_card = False
            else:
                new_card = input('Type ''y'' to get another card, type ''n'' to pass:\n').lower()
                if new_card == 'y':
                    player_cards.append(deal_card())
                else:
                    another_card = False

        # Loop through dealer hands
        # Dealer continues to draw cards when score < 17
        while dealer_score != 0 and dealer_score < 17:
            dealer_cards.append(deal_card())
            dealer_score = calculate_score(dealer_cards)
                                
        # Show final hands
        print(f'Your final hand: {player_cards}, final score: {player_score}')
        print(f'Dealer\'s final hand: {dealer_cards}, final score: {dealer_score}')

        # Compare hands
        print(compare_scores(dealer_score=dealer_score, player_score=player_score))
        
        
os.system('cls')    
while input('Do you want to play a game of Blackjack? (y/n)\n').lower() == 'y':
    os.system('cls')
    print(art.logo)      
    my_blackjack_game()


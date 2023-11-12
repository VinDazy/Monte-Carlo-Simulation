import random
import sys
import matplotlib.pyplot as plt
import numpy as np
random.seed(619)
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
colors = {'Hearts': 'Red', 'Diamonds': 'Red',
              'Clubs': 'Black', 'Spades': 'Black'}

def draw_cards(num_draws):
    deck = [{'rank': rank, 'suit': suit, 'color': colors[suit]}
            for rank in ranks for suit in suits]
    hand = random.sample(deck, num_draws)
    return hand


def monte_carlo_Sahara_Ace(num_simulations):
    """input : number of simluations for the game
        output : probability of winning game in num_simulation rounds, player credit after num_simulation rounds
    """
    player_credit = 0
    round_won = 0
    for _ in range(num_simulations):
        hand = draw_cards(1)
        if hand[0]['rank'] == 'A':
            player_credit += 10
            round_won += 1
    probability_of_winning = round_won / num_simulations
    return probability_of_winning, player_credit,round_won


def monte_carlo_Tunisian_Twins(num_simulations):
    """input : number of simluations for the game
    output : probability of winning game in num_simulation rounds, player credit after num_simulation rounds
    """
    player_credit = 0
    round_won = 0
    for _ in range(num_simulations):
        hand = draw_cards(2)
        if (hand[0]['rank'] == hand[1]['rank']) or (hand[0]['suit'] == hand[1]['suit']) or (hand[0]['color'] == hand[1]['color']):
            player_credit += 50
            round_won += 1
    probability_of_winning = round_won / num_simulations
    return probability_of_winning, player_credit,round_won

def monte_carlo_Medina_Biggie(num_simulations):
    player_credit = 0
    round_won = 0
    for _ in range(num_simulations):
        hand=draw_cards(2)
        face_card_mapping = {'J': 11, 'Q': 12, 'K': 13, 'A':1}
        for card in hand:
            if card['rank'] in face_card_mapping:
                card['rank'] = face_card_mapping[card['rank']]
        rank_1=int(hand[1]['rank'])
        rank_0=int(hand[0]['rank'])
        if rank_1>rank_0:
            player_credit+=2
            round_won+=1
    probability_of_winning = round_won / num_simulations
    return probability_of_winning, player_credit,round_won


def monte_carlo_Desert_Hearts(num_simulations):
    player_credit=0
    round_won=0
    for _ in range(num_simulations):
        hand = draw_cards(3)
        if any(card['suit'] == 'Hearts' for card in hand):
            player_credit=sum(1 for card in hand if card['suit'] == 'Hearts')
            round_won+=1
    probability_of_winning = round_won / num_simulations
    return probability_of_winning, player_credit,round_won



def has_consecutive_run(hand):
    # Sort the hand by numerical rank
    hand.sort(key=lambda x: ranks.index(x['rank']))

    consecutive_count = 1

    for i in range(1, len(hand)):
        current_rank = ranks.index(hand[i]['rank'])
        previous_rank = ranks.index(hand[i - 1]['rank'])

        if current_rank == previous_rank + 1:
            consecutive_count += 1
            if consecutive_count >= 3:
                return True
        else:
            consecutive_count = 1

    return False

def monte_carlo_Oasis_Runny(num_simulations):
    player_credit=0
    round_won = 0

    for _ in range(num_simulations):
        hand = draw_cards(5)
        if has_consecutive_run(hand):
            player_credit += 5
            round_won+=1
    probability_of_winning = round_won / num_simulations
    return probability_of_winning, player_credit,round_won

def monte_carlo_Consecutive_Colors(num_simulations):
    """Personal Game  - Consecutive Colors:
    The player draws four cards.
    If there is a consecutive sequence of at least three cards that have the same color (either Red or Black), the player wins 15 Tunisian dinars.
    Otherwise, the player loses.
"""
    player_credit = 0
    round_won = 0

    for _ in range(num_simulations):
        hand = draw_cards(4)
        hand.sort(key=lambda x: ranks.index(x['rank']))

        consecutive_count = 1

        for i in range(1, len(hand)):
            current_color = hand[i]['color']
            previous_color = hand[i - 1]['color']

            if current_color == previous_color:
                consecutive_count += 1
                if consecutive_count >= 3:
                    player_credit += 15
                    round_won += 1
                    break
            else:
                consecutive_count = 1

    probability_of_winning = round_won / num_simulations
    return probability_of_winning, player_credit,round_won

def save_probability_bar_chart(game_names, probabilities, filename):
    plt.figure(figsize=(10, 6))
    colors = plt.cm.viridis(np.linspace(0, 1, len(game_names)))
    bars = plt.bar(game_names, probabilities, color=colors)
    add_value_labels(bars)
    plt.ylabel("Winning Probability (%)")
    plt.title("Winning Probability of Each Game")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def save_money_made_bar_chart(game_names, money_made, filename):
    plt.figure(figsize=(10, 6))
    colors = plt.cm.viridis(np.linspace(0, 1, len(game_names)))
    bars = plt.bar(game_names, money_made, color=colors)
    add_value_labels(bars)
    plt.ylabel("Money Made")
    plt.title("Money Made from Each Game")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def add_value_labels(bars):
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, round(yval, 2), ha='center', va='bottom')
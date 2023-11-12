from games_functions import *
games = [
    monte_carlo_Sahara_Ace,
    monte_carlo_Tunisian_Twins,
    monte_carlo_Medina_Biggie,
    monte_carlo_Desert_Hearts,
    monte_carlo_Oasis_Runny,
    monte_carlo_Consecutive_Colors
]

number_of_simulations = 100,000
for game in games:
        probability, score, round_won = game(number_of_simulations)
        game_name = game.__name__.replace("monte_carlo_", "").replace("_", " ")
        probability_percentage = probability * 100
        print(f"{game_name} - Probability: {probability_percentage:.2f}%, Round Won : {round_won}, Score: {score}")
    
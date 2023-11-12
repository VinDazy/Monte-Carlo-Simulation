from games_functions import *

def main():
    # Check if a command-line argument is provided
    if len(sys.argv) > 1:
        try:
            number_of_simulations = int(sys.argv[1])
        except ValueError:
            print("Invalid input. Please provide a valid number of simulations.")
            return
    else:
        # Default value if no argument is provided
        number_of_simulations = 100000

    games = [
        monte_carlo_Sahara_Ace,
        monte_carlo_Tunisian_Twins,
        monte_carlo_Medina_Biggie,
        monte_carlo_Desert_Hearts,
        monte_carlo_Oasis_Runny,
        monte_carlo_Consecutive_Colors
    ]

    results = []
    for game in games:
        probability, score, round_won = game(number_of_simulations)
        game_name = game.__name__.replace("monte_carlo_", "").replace("_", " ")
        probability_percentage = probability * 100
        print(f"{game_name} - Probability: {probability_percentage:.2f}%, Rounds Won: {round_won}, Score: {score}")
        results.append((game_name, probability_percentage, score))

    # Sort results based on winning probabilities and money made
    results.sort(key=lambda x: x[1], reverse=True)  # Sort by winning probabilities
    game_names, probabilities, money_made = zip(*results)

    # Generate and save vertical bar charts with labels
    save_probability_bar_chart(game_names, probabilities, "winning_probability_bar_chart.png")
    save_money_made_bar_chart(game_names, money_made, "money_made_bar_chart.png")

    print("Bar charts successfully saved in the current working directory.")
if __name__ == "__main__":
    main()
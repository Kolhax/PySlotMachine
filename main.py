import random

# Constants
INIT_STAKE = 50

# Define items, probabilities, and payouts in dictionaries
ITEMS_PROBABILITIES = {
    "CHERRY": 10,
    "LEMON": 10,
    "ORANGE": 10,
    "PLUM": 14,
    "BELL": 16,
    "BAR": 4,
}

ITEMS_PAYOUTS = {
    "CHERRY": {2: 2, 3: 5},
    "ORANGE": {3: 10},
    "PLUM": {3: 14},
    "BELL": {3: 20},
    "BAR": {3: 250},
}

# Define emojis for items
EMOJIS = {
    "CHERRY": "🍒",
    "LEMON": "🍋",
    "ORANGE": "🍊",
    "PLUM": "🐥",
    "BELL": "🔔",
    "BAR": "💎",
}

def print_wheels(wheels):
    """
    Print the results of spinning the wheels.
    """
    print(" | ".join([EMOJIS[item] for item in wheels]))

def spin_wheel():
    """
    Spin a single wheel and return the result.
    """
    return random.choices(list(ITEMS_PROBABILITIES.keys()), weights=list(ITEMS_PROBABILITIES.values()))[0]

def calculate_win(wheels):
    """
    Calculate the player's win based on the result of spinning the wheels.
    """
    win = -1
    for item, payouts in ITEMS_PAYOUTS.items():
        count = wheels.count(item)
        if count in payouts:
            win = payouts[count]
            break
    return win

def play():
    """
    Main game loop.
    """
    stake = INIT_STAKE

    while stake > 0:
        play_question = input(f"You have ${stake}. Would you like to play? ").lower()
        if play_question in ["yes", "y"]:
            first_wheel = spin_wheel()
            second_wheel = spin_wheel()
            third_wheel = spin_wheel()

            print_wheels([first_wheel, second_wheel, third_wheel])

            win = calculate_win([first_wheel, second_wheel, third_wheel])
            if win > 0:
                print(f"You win ${win}!")
            else:
                print("You lose!")

            stake += win
        elif play_question in ["no", "n"]:
            print(f"You ended the game with ${stake} in your hand.")
            break
        else:
            print("Wrong input!")

if __name__ == "__main__":
    print("Welcome to the Slot Machine Simulator")
    print("You'll start with $50. You'll be asked if you want to play.")
    print("Answer with yes/no. You can also use y/n.")
    print("No case sensitivity in your answer.")
    print("For example, you can answer with YEs, yEs, Y, nO, N.")
    print("To win, you must get one of the following combinations:")
    print("BAR\tBAR\tBAR\t\tpays\t$250")
    print("BELL\tBELL\tBELL/BAR\tpays\t$20")
    print("PLUM\tPLUM\tPLUM/BAR\tpays\t$14")
    print("ORANGE\tORANGE\tORANGE/BAR\tpays\t$10")
    print("CHERRY\tCHERRY\tCHERRY\t\tpays\t$7")
    print("CHERRY\tCHERRY\t  -\t\tpays\t$5")
    print("CHERRY\t  -\t  -\t\tpays\t$2")

    play()

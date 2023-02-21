import random

# Define the game board as a dictionary
board = {1: 38, 4: 14, 9: 31, 17: 7, 21: 42, 28: 84, 51: 67, 54: 34, 62: 19, 64: 60, 72: 91, 80: 99, 87: 36, 93: 73, 95: 75, 98: 79}

# Define the number of players
num_players = 2

# Define the initial positions of the players
positions = [0] * num_players

# Define a function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Define a function to move a player's position
def move_player(player, steps):
    positions[player] += steps
    if positions[player] in board:
        positions[player] = board[positions[player]]

# Define a function to check if a player has won
def has_won(player):
    return positions[player] >= 100

# Play the game
current_player = 0
while True:
    # Roll the dice
    input(f"Player {current_player + 1}'s turn. Press Enter to roll the dice...")
    steps = roll_dice()
    print(f"Player {current_player + 1} rolled a {steps}.")
    
    # Move the player's position
    move_player(current_player, steps)
    print(f"Player {current_player + 1} is now at position {positions[current_player]}.")
    
    # Check if the player has won
    if has_won(current_player):
        print(f"Player {current_player + 1} has won!")
        break
    
    # Move on to the next player
    current_player = (current_player + 1) % num_players

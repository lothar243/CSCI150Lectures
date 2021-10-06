# A simple game where a number is chosen at random and two players try to get closer
# The game continues as long as the users want, and keeps track of the total number of wins

import random


# Initializing some variables
player1_wins = 0
player2_wins = 0
done = False # While this remains false, the program stays in the while loop

print("This is a game where I choose a number between 1 and 100")
print("Both players get a guess, and the one that's closer wins")

while not done:
    target_number = random.randint(1, 100)
    player1_guess = int(input("Player 1, choose a number: "))
    player2_guess = int(input("Player 2, choose a number: "))
    player1_diff = abs(player1_guess - target_number)
    player2_diff = abs(player2_guess - target_number)

    # Test to see which player got closer
    if player1_diff < player2_diff:
        print("Player 1 wins!, my number was {}".format(target_number))
        player1_wins += 1
    elif player2_diff < player1_diff:
        print("Player 2 wins!, my number was {}".format(target_number))
        player2_wins += 1
    else:
        print("There was a tie!, my number was {}".format(target_number))
    more_games = input("Would you like to play again?") # If the user inputs a 'y' or 'yes', then we keep going
    done = not (more_games == "y" or more_games == "yes")

# Exiting the program
print("I hope you had fun, player 1 won {} times, and player 2 won {} times".format(player1_wins, player2_wins))

PRICE_OF_SOFA = 2000

print("Welcome to the price is right!")
print("The winner of this round is the player that guesses the value of the sofa closest without going over")
player1_guess = float(input("Player 1 - Please give your guess for the price of this sofa: "))
player2_guess = float(input("Player 2 - Please give your guess for the price of the sofa: "))

# Check to see who got closer without going over
if player1_guess == player2_guess:
    print("Hey, you both guessed the same amount. Try again")
elif player1_guess < PRICE_OF_SOFA:
    if player2_guess < PRICE_OF_SOFA:
        # both players guessed below the price, so we'll compare the differences
        player1_difference = PRICE_OF_SOFA - player1_guess
        player2_difference = PRICE_OF_SOFA - player2_guess
        if player1_difference < player2_difference:
            print("Player 1 wins! Congratulations!")
        else:
            print("Player 2 wins! Congratulations!")
    else:
        # player 2's guess was too big
        print("Player 2's guess was above the price of the sofa, so player 1 Wins. Congratulations!")
else:
    # player 1's guess was too big, but it's possible player 2 also guessed too large
    if player2_guess < PRICE_OF_SOFA:
        print("Player 1's guess was above the price of the sofa, so player 2 Wins. Congratulations!")
    else:
        print("Both players guessed values that were too large")
        if player1_guess < player2_guess:
            print("However, player 1's guess was closer, so they win. Congratulations!")
        else:
            print("However, player 2's guess was closer, so they win. Congratulations!")

print("Thanks for playing!")

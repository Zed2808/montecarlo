import tictactoe

# Create a new game history, starting with a new game
history = [tictactoe.new_game()]

# Print out the game board
print(tictactoe.to_string(history))

# Continue while the game has no winner (and is not tied)
while tictactoe.winner(history) == -1:
    # Get a list of legal moves
    legal_plays = tictactoe.legal_plays(history)

    invalid_input = True
    while invalid_input:
        # Get move from user
        choice = input('Choose a space: ')

        try:
            # Try to convert input to an integer
            choice = int(choice)

            # Convert from user-readable slot number to slot coordinates
            play = ((choice-1)//3, (choice-1)%3)

            # Make sure selected slot is still open
            if play not in legal_plays:
                raise Exception()
            else:
                invalid_input = False
        except:
            print('Please enter a legal move.')

    history.append(tictactoe.next_state(history, play))

    # Print out the game board
    print()
    print(tictactoe.to_string(history))

if tictactoe.winner(history) == -2:
    print('The game ends in a tie!')
else:
    print(f'Player {tictactoe.winner(history) + 1} has won the game!')


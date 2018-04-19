import tictactoe

# Create a new game history, starting with a new game
state = tictactoe.new_game()

# Print out the game board
print(tictactoe.to_string(state))

# Continue while the game has no winner (and is not tied)
while tictactoe.winner(state) == -1:
    # Get a list of legal moves
    legal_plays = tictactoe.legal_plays(state)

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

    tictactoe.next_state(state, play)

    # Print out the game board
    print()
    print(tictactoe.to_string(state))

if tictactoe.winner(state) == -2:
    print('The game ends in a tie!')
else:
    print(f'Player {tictactoe.winner(state) + 1} has won the game!')


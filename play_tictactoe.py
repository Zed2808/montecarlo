import tictactoe
import montecarlo

# Create a new game history, starting with a new game
state = tictactoe.new_game()

# Print out the game board
print(tictactoe.to_string(state, numbers=True))

# Continue while the game has no winner (and is not tied)
while tictactoe.winner(state) == -1:
    # Get a list of legal moves
    legal_plays = tictactoe.legal_plays(state)

    # If it's X's turn, use player input
    if tictactoe.current_player(state) == 0:
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
    # Otherwise, use AI input
    else:
        play = montecarlo.best_play(tictactoe, state)

    tictactoe.next_state(state, play)

    # Print out the game board
    print(f'\n{tictactoe.to_string(state, numbers=True)}')

if tictactoe.winner(state) == -2:
    print('The game ends in a tie!')
else:
    print(f'Player {tictactoe.winner(state) + 1} has won the game!')


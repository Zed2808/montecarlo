import mcts
import random

# Name of game we're using with the API
game = 'checkers'

# Number of games to simulate
max_games = 10

# Time to spend per turn on MCTS simulation (in seconds)
sim_time = 1

# Instances to run for each MCTS call
instances = 10

games_played = 0
wins = {0: 0, 1: 0, -1: 0}

# Call API for a new game state
state = mcts.new_game(game)
print(mcts.to_string(game, state))

while games_played < max_games:
    # Get a list of legal plays for the current player
    legal = mcts.legal_plays(game, state)

    try:
        # Select a move from the list of legal plays
        # If only one move, just select it
        if len(legal) == 1:
            play = legal[0]
        # Player 1 uses MCTS
        elif mcts.current_player(game, state) == 0:
            play = mcts.best_play(game, state, sim_time, instances)['best_play']
        # Player 2 uses random choice
        else:
            play = random.choice(legal)

        state = mcts.next_state(game, state, play)
        print(mcts.to_string(game, state))
    except:
        # Print the winner and track their win
        winner = mcts.winner(game, state)
        games_played += 1
        wins[winner] += 1

        # Set up a new game
        state = mcts.new_game(game)

print('Results:')
print(f'Player 1: {wins[0]} wins')
print(f'Player 2: {wins[1]} wins')

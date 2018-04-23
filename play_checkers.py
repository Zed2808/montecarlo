import checkers
import montecarlo
import random

# Number of games to simulate
max_games = 10

# Time to spend per turn on MCTS simulation (in seconds)
sim_time = 0.1

games_played = 0
wins = {0: 0, 1: 0, -1: 0}

state = checkers.new_game()
print(checkers.to_string(state))

while games_played < max_games:
    # Get a list of legal plays for the current player
    legal = checkers.legal_plays(state)

    try:
        # Select a move from the list of legal plays
        # (Player 1 used MCTS, player 2 uses random choice)
        if checkers.current_player(state) == 0:
            play = montecarlo.best_play(checkers, state, sim_time=sim_time)
        else:
            play = random.choice(legal)

        checkers.next_state(state, play)
        print(checkers.to_string(state))
    except:
        # Print the winner and track their win
        winner = checkers.winner(state)
        games_played += 1
        wins[winner] += 1

        # Set up a new game
        state = checkers.new_game()

print('Results:')
print(f'Player 1: {wins[0]} wins')
print(f'Player 2: {wins[1]} wins')

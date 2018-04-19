import datetime
import random
import copy

'''
1. Find current player's legal moves
2. Run one simulation for each legal move until time runs out
3. For each simulation, choose a sequence of random moves until a winner is found
4. Once a winner is found, update the win% for that first play
'''

# Return the best move after simulations
def best_play(game, state, sim_time=1):
    # Change sim_time from seconds to a datetime-compatible timedelta
    sim_time = datetime.timedelta(seconds=sim_time)

    # Get the current player and their legal moves within the game
    player = game.current_player(state)
    legal_plays = game.legal_plays(state)

    # Create a dictionary with all legal plays to store wins/play
    wins = {play: 0 for play in legal_plays}

    print(game.to_string(state))
    print(f'State: {state}')
    print(f'Legal plays: {legal_plays}')

    # Return early if no choices are available
    if not legal_plays:
        return
    if len(legal_plays) == 1:
        return legal_plays[0]

    # Number of games simulated from the current state
    games = 0

    # Current time (to track elapsed time)
    start_time = datetime.datetime.utcnow()

    # Simulate only until sim_time has elapsed
    while datetime.datetime.utcnow() - start_time < sim_time:
        # Run the same number of simulations for each possible play
        for play in legal_plays:
            print(f'Game #{games}:\n{game.to_string(state)}\n')

            # Simulate a game randomly after the given play
            win = simulate(game, state, play)

            print(f'Game won: {win}')
            print('---------------------------------------')

            # Add the result of the game to the dict of win stats
            if win:
                wins[play] += 1

            games += 1

    print(f'Simulated {games} games in {datetime.datetime.utcnow() - start_time}')
    print(f'Wins/play: {wins}')

    move = max(wins, key=wins.get)
    print(f'Best play: {move}')

    return move

# Randomly simulate a game given a play, return whether or not the game was won
def simulate(game, state, play):
    # Store original player this game
    player = game.current_player(state)

    # Make a copy of the game's state to avoid altering the original
    state_copy = copy.deepcopy(state)

    # Update state with the given play
    state_copy = game.next_state(state_copy, play)

    print(f'Simulating from:\n{game.to_string(state_copy)}\n')

    # Until a winner has been determined
    while game.winner(state_copy) == -1:
        # Get legal plays for the new state
        legal_plays = game.legal_plays(state_copy)

        # Randomly select a legal play
        play = random.choice(legal_plays)

        # Update state with new random play
        state_copy = game.next_state(state_copy, play)

    print(f'Game ended as:\n{game.to_string(state_copy)}')

    # If player whose turn it is wins, return True
    return True if player == game.winner(state_copy) else False

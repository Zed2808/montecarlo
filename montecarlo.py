import datetime
import random
import copy

DEBUG = False

def log(s):
    if DEBUG:
        print(s)

# Return the best move after simulations
def best_play(game, state, sim_time=1):
    log('---------------------------------')
    log('BEGINNING MONTE CARLO TREE SEARCH')
    # Change sim_time from seconds to a datetime-compatible timedelta
    sim_time = datetime.timedelta(seconds=sim_time)

    # Get the current player and their legal moves within the game
    player = game.current_player(state)
    legal_plays = game.legal_plays(state)

    # Create a dictionary with all legal plays to store wins/play
    wins = {play: 0 for play in legal_plays}

    log(f'Legal plays: {legal_plays}')

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
            log(f'Game #{games}')

            # Simulate a game randomly after the given play
            win = simulate(game, state, play)

            log(f'Game won: {win}')
            log('---------------------------------------')

            # Add the result of the game to the dict of win stats
            if win:
                wins[play] += 1

            games += 1

    log(f'Simulated {games} games in {datetime.datetime.utcnow() - start_time}')
    log(f'Wins/play: {wins}')

    move = max(wins, key=wins.get)
    log(f'Best play: {move}')

    return wins

# Randomly simulate a game given a play, return whether or not the game was won
def simulate(game, state, play):
    # Store original player this game
    player = game.current_player(state)

    # Make a copy of the game's state to avoid altering the original
    state_copy = copy.deepcopy(state)

    # Update state with the given play
    game.next_state(state_copy, play)

    log(f'Simulating from:\n{game.to_string(state_copy)}\n')

    # Until a winner has been determined
    while game.winner(state_copy) == -1:
        # Get legal plays for the new state
        legal_plays = game.legal_plays(state_copy)

        # If no moves are available (stalemate)
        if not legal_plays:
            break

        # Randomly select a legal play
        play = random.choice(legal_plays)

        # Update state with new random play
        game.next_state(state_copy, play)

    log(f'Game ended as:\n{game.to_string(state_copy)}')

    # If player whose turn it is wins, return True
    return True if player == game.winner(state_copy) else False

# Returns starting state of a new game
def new_game():
    return {'board': [['', '', ''], ['', '', ''], ['', '', '']], 'player': 0}

# Returns a list of legal moves for the current player
def legal_plays(state_history):
    board = state_history[-1]['board']
    return [(row[0], col[0]) for row in enumerate(board) for col in enumerate(row[1]) if col[1] == '']

# Returns the next game state given the current state and move
def next_state(state, play):
    state['board'][play[0]][play[1]] = 'x' if state['player'] == 0 else 'o'
    state['player'] = 1 if state['player'] == 0 else 0
    return state

# Given game state, determine if the game has been won (or tied)
def winner(state_history):
    board = state_history[-1]['board']

    # Check for horizontal wins
    for row in board:
        # If the instances of row[0] is the same as the length of row
        # (meaning every element in the row is the same)
        if row.count(row[0]) == len(row):
            return 0 if row[0] == 'x' else 1

    # Check for vertical wins
    for col in board[0]:
        for row in board:
            

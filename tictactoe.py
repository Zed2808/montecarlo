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
    for col in enumerate(board[0]):
        if col[1] == board[1][col[0]] and col[1] == board[2][col[0]]:
            return 0 if col[1] == 'x' else 1

    # Check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2]:
        return 0 if board[0][0] == 'x' else 1

    if board[0][2] == board[1][1] == board[2][0]:
        return 0 if board[0][2] == 'x' else 1

    # Check for tie
    # If there are no empty spaces:
    if not any('' in row for row in board):
        return -2

    # If no player has won yet
    return -1

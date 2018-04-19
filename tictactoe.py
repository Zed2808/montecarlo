# Returns starting state of a new game
def new_game():
    return {'board': [['', '', ''], ['', '', ''], ['', '', '']], 'player': 0}

# Returns the id of the active player
def current_player(state):
    return state['player']

# Returns a list of legal moves for the current player
def legal_plays(state):
    board = state['board']
    return [(row[0], col[0]) for row in enumerate(board) for col in enumerate(row[1]) if col[1] == '']

# Returns the next game state given the current state and move
def next_state(state, play):
    state['board'][play[0]][play[1]] = 'X' if state['player'] == 0 else 'O'
    state['player'] = 1 if state['player'] == 0 else 0

# Given game state, determine if the game has been won (or tied)
def winner(state):
    board = state['board']

    # Check for horizontal wins
    for row in board:
        # If the instances of row[0] is the same as the length of row
        # (meaning every element in the row is the same)
        if row.count(row[0]) == len(row) and row[0]:
            return 0 if row[0] == 'X' else 1

    # Check for vertical wins
    for col in enumerate(board[0]):
        if col[1] == board[1][col[0]] and col[1] == board[2][col[0]] and col[1]:
            return 0 if col[1] == 'X' else 1

    # Check for diagonal wins
    if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
        return 0 if board[0][0] == 'X' else 1

    if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
        return 0 if board[0][2] == 'X' else 1

    # Check for tie
    # If there are no empty spaces:
    if not any('' in row for row in board):
        return -2

    # If no player has won yet
    return -1

# Prints the game board
def to_string(state, numbers=False):
    board = state['board']

    # Replace empty spots with a space (or number) instead of an empty string
    if numbers:
        board = [[col[1] if col[1] else (row[0])*3 + col[0]+1  for col in enumerate(row[1])] for row in enumerate(board)]
    else:
        board = [[col if col else ' ' for col in row] for row in board]

    s  = f' {board[0][0]} | {board[0][1]} | {board[0][2]}\n'
    s += '-----------\n'
    s += f' {board[1][0]} | {board[1][1]} | {board[1][2]}\n'
    s += '-----------\n'
    s += f' {board[2][0]} | {board[2][1]} | {board[2][2]}'

    return s

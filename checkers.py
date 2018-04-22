black_pieces = ['○', '◔']
white_pieces = ['●', '◕']
black_king = '◔'
white_king = '◕'

# Returns starting state of a new game
def new_game():
    return {'board': [['', '●', '', '●', '', '●', '', '●'],
                      ['●', '', '●', '', '●', '', '●', ''],
                      ['', '●', '', '●', '', '●', '', '●'],
                      ['', '', '', '', '', '', '', ''],
                      ['', '', '', '', '', '', '', ''],
                      ['○', '', '○', '', '○', '', '○', ''],
                      ['', '○', '', '○', '', '○', '', '○'],
                      ['○', '', '○', '', '○', '', '○', '']],
            'player': 0}

# Returns the id of the currently active player
def current_player(state):
    return state['player']

# Determines whether given coordinates are within the bounds of the board
def in_bounds(coords):
    row, col = coords
    return True if row in range(0, 8) and col in range(0, 8) else False

# Returns a list of legal moves for the current player
# [(f1, e2), (f3, e2), (f3, e4), ...] Human coords
# [(41, 34), (43, 34), (43, 36), ...] Space number
# [((5, 0), (4, 1)), ((5, 2), (4, 1)), ((5, 2), (4, 3)), ...]
def legal_plays(state):
    # First check for any legal jumps
    jumps = legal_jumps(state)

    # If there are jumps available, they must be taken
    if jumps:
        return jumps

    board = state['board']
    player = state['player']

    legal = []

    # Iterate over each row on the board
    for rownum, row in enumerate(board):
        # Iterate over each space in the row
        for colnum, col in enumerate(row):
            # Space occupied by black
            if col in black_pieces and player == 0:
                # Check up/left & up/right diagonals for empty spaces
                if in_bounds((rownum-1, colnum-1)) and board[rownum-1][colnum-1] == '':
                    legal.append(((rownum, colnum), (rownum-1, colnum-1)))

                if in_bounds((rownum-1, colnum+1)) and board[rownum-1][colnum+1] == '':
                    legal.append(((rownum, colnum), (rownum-1, colnum+1)))

            # Check extra spaces for black kings
            if col == black_king and player == 0:
                # Check down/left & down/right diagonals for empty spaces
                if in_bounds((rownum+1, colnum-1)) and board[rownum+1][colnum-1] == '':
                    legal.append(((rownum, colnum), (rownum+1, colnum-1)))

                if in_bounds((rownum+1, colnum+1)) and board[rownum+1][colnum+1] == '':
                    legal.append(((rownum, colnum), (rownum+1, colnum+1)))

            # Space is occupied by white
            if col in white_pieces and player == 1:
                # Check down/left & down/right diagonals for empty spaces
                if in_bounds((rownum+1, colnum-1)) and board[rownum+1][colnum-1] == '':
                    legal.append(((rownum, colnum), (rownum+1, colnum-1)))

                if in_bounds((rownum+1, colnum+1)) and board[rownum+1][colnum+1] == '':
                    legal.append(((rownum, colnum), (rownum+1, colnum+1)))

            # Check extra spaces for white kings
            if col == white_king and player == 1:
                # Check up/left & up/right diagonals for empty spaces
                if in_bounds((rownum-1, colnum-1)) and board[rownum-1][colnum-1] == '':
                    legal.append(((rownum, colnum), (rownum-1, colnum-1)))

                if in_bounds((rownum-1, colnum+1)) and board[rownum-1][colnum+1] == '':
                    legal.append(((rownum, colnum), (rownum-1, colnum+1)))

    return legal

# Returns a list of legal jumps available to the current player
def legal_jumps(state):
    board = state['board']
    player = state['player']

    legal = []

    # Iterate over each space on the board
    for rownum, row in enumerate(board):
        for colnum, col in enumerate(row):
            # Check forward jumps available to black
            if col in black_pieces and player == 0:
                # Space two up/two left is in bounds and empty
                if in_bounds((rownum-2, colnum-2)) and board[rownum-2][colnum-2] == '':
                    # Space directly up/left is a white piece
                    if board[rownum-1][colnum-1] in white_pieces:
                        legal.append( ((rownum, colnum), (rownum-2, colnum-2)) )

                # Space 2up/2right is in bounds and empty
                if in_bounds((rownum-2, colnum+2)) and board[rownum-2][colnum+2] == '':
                    # Space directly up/right is a white piece
                    if board[rownum-1][colnum+1] in white_pieces:
                        legal.append( ((rownum, colnum), (rownum-2, colnum+2)) )

            # Check backward jumps available to black
            if col == black_king and player == 0:
                # Space 2down/2left is in bounds and empty
                if in_bounds((rownum+2, colnum-2)) and board[rownum+2][colnum-2] == '':
                    # Space directly down/left is a white piece
                    if board[rownum+1][colnum-1] in white_pieces:
                        legal.append( ((rownum, colnum), (rownum+2, colnum-2)) )

                # Space 2down/2right is in bounds and empty
                if in_bounds((rownum+2, colnum+2)) and board[rownum+2][colnum+2] == '':
                    # Space directly down/right is a white piece
                    if board[rownum+1][colnum+1] in white_pieces:
                        legal.append( ((rownum, colnum), (rownum+2, colnum+2)) )

            # Check forward jumps available to white
            if col in white_pieces and player == 1:
                # Space 2down/2left is in bounds and empty
                if in_bounds((rownum+2, colnum-2)) and board[rownum+2][colnum-2] == '':
                    # Space directly down/left is a black piece
                    if board[rownum+1][colnum-1] in black_pieces:
                        legal.append( ((rownum, colnum), (rownum+2, colnum-2)) )

                # Space 2down/2right is in bounds and empty
                if in_bounds((rownum+2, colnum+2)) and board[rownum+2][colnum+2] == '':
                    # Space directly down/right is a black piece
                    if board[rownum+1][colnum+1] in black_pieces:
                        legal.append( ((rownum, colnum), (rownum+2, colnum+2)) )

            # Check backward jumps available to white
            if col == white_king and player == 1:
                # Space 2up/2left is in bounds and empty
                if in_bounds((rownum-2, colnum-2)) and board[rownum-2][colnum-2] == '':
                    # Space directly up/left is a black piece
                    if board[rownum-1][colnum-1] in black_pieces:
                        legal.append( ((rownum, colnum), (rownum-2, colnum-2)) )

                # Space 2up/2right is in bounds and empty
                if in_bounds((rownum-2, colnum+2)) and board[rownum-2][colnum+2] == '':
                    # Space directly up/right is a black piece
                    if board[rownum-1][colnum+1] in black_pieces:
                        legal.append( ((rownum, colnum), (rownum-2, colnum+2)) )

    return legal

# Alters game state according to the play made
def next_state(state, play):
    origin, dest = play
    origin_row, origin_col = origin
    dest_row, dest_col = dest
    piece = state['board'][origin_row][origin_col]

    # Determine whether piece should become a king
    if dest_row == 0 or dest_row == 7:
        if piece in black_pieces:
            piece = black_king
        elif piece in white_pieces:
            piece = white_king

    # Move piece from origin to destination
    state['board'][origin_row][origin_col] = ''
    state['board'][dest_row][dest_col] = piece

    # If a piece was jumped, remove it from the game
    if abs(origin_row - dest_row) == 2:
        jumped_row = (origin_row + dest_row) // 2
        jumped_col = (origin_col + dest_col) // 2
        state['board'][jumped_row][jumped_col] = ''

    # Change active player
    state['player'] = 1 if state['player'] == 0 else 0

# Given a game state, determine if the game has been won/lost/tied
def winner(state):
    num_black = 0
    num_white = 0

    # Iterate through all spaces, count number of each piece
    for row in board:
        for col in row:
            if col in black_pieces:
                num_black += 1
            elif col in white_pieces:
                num_white += 1

    # If there are 0 of one color, the other color wins
    if num_black == 0:
        return 1
    elif num_white == 0:
        return 0
    else:
        return -1

# Prints the game board
def to_string(state):
    board = state['board']

    # Replace empty spots with a space to print properly spaced
    board = [[col if col else ' ' for col in row] for row in board]

    s  = '  1 2 3 4 5 6 7 8\n'
    s += ' ┏━┳━┳━┳━┳━┳━┳━┳━┓\n'
    s += 'A┃' + '┃'.join(board[0]) + '┃' + '\n'
    s += ' ┣━╋━╋━╋━╋━╋━╋━╋━┫\n'
    s += 'B┃' + '┃'.join(board[1]) + '┃' + '\n'
    s += ' ┣━╋━╋━╋━╋━╋━╋━╋━┫\n'
    s += 'C┃' + '┃'.join(board[2]) + '┃' + '\n'
    s += ' ┣━╋━╋━╋━╋━╋━╋━╋━┫\n'
    s += 'D┃' + '┃'.join(board[3]) + '┃' + '\n'
    s += ' ┣━╋━╋━╋━╋━╋━╋━╋━┫\n'
    s += 'E┃' + '┃'.join(board[4]) + '┃' + '\n'
    s += ' ┣━╋━╋━╋━╋━╋━╋━╋━┫\n'
    s += 'F┃' + '┃'.join(board[5]) + '┃' + '\n'
    s += ' ┣━╋━╋━╋━╋━╋━╋━╋━┫\n'
    s += 'G┃' + '┃'.join(board[6]) + '┃' + '\n'
    s += ' ┣━╋━╋━╋━╋━╋━╋━╋━┫\n'
    s += 'H┃' + '┃'.join(board[7]) + '┃' + '\n'
    s += ' ┗━┻━┻━┻━┻━┻━┻━┻━┛\n'

    return s


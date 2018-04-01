import datetime
import random

class MonteCarlo:

    # Takes a Board instance and initializes list of game states and stats
    def __init__(self, board, **kwargs):
        self.board = board
        self.history = []
        self.wins = {}
        self.plays = {}

        # Get argument for max simulation time in seconds
        seconds = kwargs.get('time', 5)
        self.sim_time = datetime.timedelta(seconds=seconds)

        # Get max moves to make during a simulation
        self.max_moves = kwargs.get('max_moves', 10)

    # Takes game state and appends it to history
    def update(self, state):
        self.history.append(state)

    # Calculate the best move from the current state
    def get_play(self):
        self.max_depth = 0
        state = self.history[-1]
        player = self.board.current_player(state)
        legal_plays = self.board.legal_plays(self.history)

        # Return early if 0 or 1 choices
        if not legal_plays:
            return
        if len(legal) == 1:
            return legal[0]

        games = 0
        start_time = datetime.datetime.utcnow()

        # Simulate only until sim_time has elapsed
        while datetime.datetime.utcnow() - start_time < self.sim_time:
            self.simulate()
            games += 1

        # Create a list of (play, state) tuples for each legal move and the state it will produce
        plays_states = [(p, self.board.next_state(state, p)) for p in legal]

        # Display the number of simulate() calls and the time elapsed
        print(f'{games} games played in {datetime.datetime.utcnow() - start_time} seconds')

        # Pick the move with the highest winrate
        winrate, move = max((self.wins.get((player, s), 0) / self.plays.get((player, s), 1), p) for p, s in plays_states)

        # Display the stats for each possible play

        print(f'Maximum depth search: {self.max_depth}')

        return move

    # Execute random playout from current state and update stats tables
    def simulate(self):
        visited_states = set()
        history_copy = self.history[:]
        state = history_copy[-1]
        player = self.board.current_player(state)

        expand = True
        for t in range(self.max_moves):
            legal_plays = self.board.legal_plays(history_copy)

            play = random.choice(legal_plays)
            state = self.board.next_state(state, play)
            history_copy.append(state)

            # Player refers to the player that moved into the state
            if expand and (player, state) not in self.plays:
                expand = False
                self.plays[(player, state)] = 0
                self.wins[(player, state)] = 0

            visited_states.add((player, state))

            player = self.board.current_player(state)
            winner = self.board.winner(history_copy)
            if winner:
                break

        for player, state in visited_states:
            if (player, state) not in self.plays:
                continue
            self.plays[(player, state)] += 1
            if player == winner:
                self.wins[(player, state)] += 1


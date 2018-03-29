import datetime
import random

class MonteCarlo:

    # Takes a Board instance and initializes list of game states and stats
    def __init__(self, board, **kwargs):
        self.board = board
        self.states = []
        self.wins = {}
        self.plays = {}

        # Get argument for max simulation time in seconds
        seconds = kwargs.get('time', 5)
        self.sim_time = datetime.timedelta(seconds=seconds)

        # Get max moves to make during a simulation
        self.max_moves = kwargs.get('max_moves', 10)

    # Takes game state and appends it to history
    def update(self, state):
        self.states.append(state)

    # Calculate the best move from the current state
    def get_play(self):
        start_time = datetime.datetime.utcnow()

        # Simulate until sim_time has elapsed
        while datetime.datetime.utcnow() - start_time < self.sim_time:
            self.simulate()

    # Execute random playout from current state and update stats tables
    def simulate(self):
        states_copy = self.states[:]
        state = states_copy[-1]

        for i in range(self.max_moves):
            legal_plays = self.board.legal_plays(states_copy)

            play = random.choice(legal_plays)
            state = self.board.next_state(state, play)
            states_copy.append(state)

            winner = self.board.winner(states_copy)
            if winner:
                break

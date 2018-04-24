import montecarlo
import tictactoe
import threading

class MCTSThread(threading.Thread):

    def __init__(self, game, state):
        threading.Thread.__init__(self)
        self.game = game
        self.state = state
        self.data = None

    def run(self):
        self.data = montecarlo.best_play(self.game, self.state)

    def results(self):
        return self.data

state = tictactoe.new_game()
num_threads = 5
threads = []
wins = []

# Create and start num_threads new threads
for i in range(num_threads):
    thread = MCTSThread(tictactoe, state)
    thread.start()
    threads.append(thread)

# Wait for all threads to complete execution then get results from each
for thread in threads:
    thread.join()
    wins.append(thread.results())

print(f'wins: {wins}')

# Add up results from each thread
w = {key: 0 for key in wins[0]}
for result in wins:
    w = {key: w[key] + result[key] for key in w}

print(f'total wins: {w}')


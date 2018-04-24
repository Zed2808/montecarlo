import requests
import json
import tictactoe

api = 'https://kfdn9vy106.execute-api.us-east-1.amazonaws.com/production/mcts-sum'

game = 'tictactoe'
sim_time = 1
instances = 10

state = requests.post(api, data=json.dumps({'action': 'new_game', 'game': 'tictactoe'})).json()
print(f'new_game: {state}')

current_player = requests.post(api, data=json.dumps({'action': 'current_player', 'game': 'tictactoe', 'state': state})).json()
print(f'current_player: {current_player}')

plays = requests.post(api, data=json.dumps({'action': 'legal_plays', 'game': 'tictactoe', 'state': state})).json()
print(f'legal_plays: {plays}')

state = requests.post(api, data=json.dumps({'action': 'next_state', 'game': 'tictactoe', 'state': state, 'play': plays[0]})).json()
print(f'next_state: {state}')

winner = requests.post(api, data=json.dumps({'action': 'winner', 'game': 'tictactoe', 'state': state})).json()
print(f'winner: {winner}')

s = requests.post(api, data=json.dumps({'action': 'to_string', 'game': 'tictactoe', 'state': state})).json()
print(f'to_string:\n{s}')

# data = json.dumps({'action': 'best_play', 'game': game, 'state': state, 'sim_time': sim_time, 'instances': instances})
# results = requests.post(api, data=data)
# print(results.json())

# games = results['games']
# run_time = results['run_time']
# wins = results['wins']
# move = max(wins, key=wins.get)

# print(f'Simulated {games} games in {run_time} seconds over {instances} instances ({games / run_time: .6} games/second)')
# print(f'Total wins per play: {wins}')
# print(f'Best play: {move}')

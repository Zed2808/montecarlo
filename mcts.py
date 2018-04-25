import requests
import json

api = 'https://kfdn9vy106.execute-api.us-east-1.amazonaws.com/production/mcts-sum'

def call_api(args):
	# print(f'> Calling API ({args["action"]})')
	r = requests.post(api, data=json.dumps(args)).json()

	# best_play will return the win list and best play as strings
	if args['action'] == 'best_play':
		# Convert the best play back into a tuple
		r['best_play'] = eval(r['best_play'])

	# print(f'< API returned: {r} ({type(r)})')
	return r

def best_play(game, state, sim_time=1, instances=10):
	args = {'action': 'best_play', 'game': game, 'state': state, 'sim_time': sim_time, 'instances': instances}
	return call_api(args)

def new_game(game):
	args = {'action': 'new_game', 'game': game}
	return call_api(args)

def current_player(game, state):
	args = {'action': 'current_player', 'game': game, 'state': state}
	return call_api(args)

def legal_plays(game, state):
	args = {'action': 'legal_plays', 'game': game, 'state': state}
	return call_api(args)

def next_state(game, state, play):
	args = {'action': 'next_state', 'game': game, 'state': state, 'play': play}
	return call_api(args)

def winner(game, state):
	args = {'action': 'winner', 'game': game, 'state': state}
	return call_api(args)

def to_string(game, state):
	args = {'action': 'to_string', 'game': game, 'state': state}
	return call_api(args)

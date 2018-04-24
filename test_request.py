import requests
import json
import tictactoe

api = 'https://kfdn9vy106.execute-api.us-east-1.amazonaws.com/production/mcts-sum'

state = tictactoe.new_game()
sim_time = 1
instances = 5

data = json.dumps({'state': state, 'sim_time': sim_time, 'instances': instances})

results = requests.post(api, data=data)

print(results.json())


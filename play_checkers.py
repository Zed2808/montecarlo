import checkers
import random

state = checkers.new_game()

print(checkers.to_string(state))

while True:
    legal = checkers.legal_plays(state)
    play = random.choice(legal)

    checkers.next_state(state, play)

    print(checkers.to_string(state))


import checkers
import random

state = checkers.new_game()

print(checkers.to_string(state))

while True:
    input()

    legal = checkers.legal_plays(state)

    try:
        play = random.choice(legal)
    except:
        print('No more moves available.')
        break

    checkers.next_state(state, play)

    print(checkers.to_string(state))


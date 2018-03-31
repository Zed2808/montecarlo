import unittest
import tictactoe

class TicTacToeTestCase(unittest.TestCase):

    def test_new_game(self):
        expected = {'board': [['', '', ''], ['', '', ''], ['', '', '']], 'player': 0}
        self.assertEqual(tictactoe.new_game(), expected)

    def test_legal_plays(self):
        state_history = []
        state = tictactoe.new_game()
        state['board'] = [['x', '', ''], ['', 'o', ''], ['', '', 'x']]
        state_history.append(state)
        expected = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
        self.assertEqual(tictactoe.legal_plays(state_history), expected)

    def test_next_state(self):
        state = tictactoe.new_game()
        state['board'] = [['x', '', ''], ['', 'o', ''], ['', '', 'x']]
        state['player'] = 1
        play = (1, 2)
        expected = {'board': [['x', '', ''], ['', 'o', 'o'], ['', '', 'x']], 'player': 0}
        self.assertEqual(tictactoe.next_state(state, play), expected)

    def test_winner(self):
        state_history = []
        state = tictactoe.new_game()
        state_history.append(state)

        # Horizontal win
        state['board'] = [['x', '', 'x'], ['o', 'o', 'o'], ['', '', 'x']]
        self.assertEqual(tictactoe.winner(state_history), 1)

        # Vertical win
        state['board'] = [['x', '', 'o'], ['x', 'o', ''], ['x', '', 'x']]
        self.assertEqual(tictactoe.winner(state_history), 0)

        # Diagonal win
        state['board'] = [['x', 'x', 'o'], ['', 'o', ''], ['o', '', 'x']]
        self.assertEqual(tictactoe.winner(state_history), 1)

        # No win yet
        state['board'] = [['x', '', 'x'], ['', 'o', 'o'], ['', '', 'x']]
        self.assertEqual(tictactoe.winner(state_history), -1)

        # Tied game
        state['board'] = [['x', 'o', 'x'], ['o', 'x', 'o'], ['o', 'x', 'o']]
        self.assertEqual(tictactoe.winner(state_history), -2)

if __name__ == '__main__':
    unittest.main()

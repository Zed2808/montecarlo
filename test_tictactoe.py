import unittest
import tictactoe

class TicTacToeTestCase(unittest.TestCase):

    def test_new_game(self):
        expected = {'board': [['', '', ''], ['', '', ''], ['', '', '']], 'player': 0}
        self.assertEqual(tictactoe.new_game(), expected)

    def test_legal_plays(self):
        state_history = []
        state = tictactoe.new_game()
        state['board'] = [['X', '', ''], ['', 'O', ''], ['', '', 'X']]
        state_history.append(state)
        expected = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
        self.assertEqual(tictactoe.legal_plays(state_history), expected)

    def test_next_state(self):
        state_history = []
        state = tictactoe.new_game()
        state['board'] = [['X', '', ''], ['', 'O', ''], ['', '', 'X']]
        state['player'] = 1
        state_history.append(state)
        play = (1, 2)
        expected = {'board': [['X', '', ''], ['', 'O', 'O'], ['', '', 'X']], 'player': 0}
        self.assertEqual(tictactoe.next_state(state_history, play), expected)

    def test_winner(self):
        state_history = []
        state = tictactoe.new_game()
        state_history.append(state)

        # Horizontal win
        state['board'] = [['X', '', 'X'], ['O', 'O', 'O'], ['', '', 'X']]
        self.assertEqual(tictactoe.winner(state_history), 1)

        # Vertical win
        state['board'] = [['X', '', 'O'], ['X', 'O', ''], ['X', '', 'X']]
        self.assertEqual(tictactoe.winner(state_history), 0)

        # Diagonal win
        state['board'] = [['X', 'X', 'O'], ['', 'O', ''], ['O', '', 'X']]
        self.assertEqual(tictactoe.winner(state_history), 1)

        # No win yet
        state['board'] = [['X', '', 'X'], ['', 'O', 'O'], ['', '', 'X']]
        self.assertEqual(tictactoe.winner(state_history), -1)

        # Tied game
        state['board'] = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
        self.assertEqual(tictactoe.winner(state_history), -2)

    def test_to_string(self):
        state_history = []
        state = tictactoe.new_game()
        state['board'] = [['X', '', 'X'], ['O', 'O', ''], ['X', '', '']]
        state_history.append(state)

        expected  = ' X | 2 | X\n'
        expected += '-----------\n'
        expected += ' O | O | 6\n'
        expected += '-----------\n'
        expected += ' X | 8 | 9'
        self.assertEqual(tictactoe.to_string(state_history), expected)

if __name__ == '__main__':
    unittest.main()

import unittest
from task_06 import rps_game_winner, define_winning_action_index, \
    WrongNumberOfPlayersError, NoSuchStrategyError, PlayerDataFormatError


class TaskSixTestCase(unittest.TestCase):
    def test_winning_action_paper_scissors(self):
        self.assertEqual(define_winning_action_index(["P", "S"]), 1)

    def test_winning_action_paper_rock(self):
        self.assertEqual(define_winning_action_index(["P", "R"]), 0)

    def test_winning_action_paper_paper(self):
        self.assertEqual(define_winning_action_index(["P", "P"]), 0)

    def test_winning_action_rock_scissors(self):
        self.assertEqual(define_winning_action_index(["R", "S"]), 0)

    def test_winning_action_rock_rock(self):
        self.assertEqual(define_winning_action_index(["R", "R"]), 0)

    def test_winning_action_rock_paper(self):
        self.assertEqual(define_winning_action_index(["R", "P"]), 1)

    def test_winning_action_scissors_scissors(self):
        self.assertEqual(define_winning_action_index(["S", "S"]), 0)

    def test_winning_action_scissors_rock(self):
        self.assertEqual(define_winning_action_index(["S", "R"]), 1)

    def test_winning_action_scissors_paper(self):
        self.assertEqual(define_winning_action_index(["S", "P"]), 0)

    def test_non_list_input_raises_type_error(self):
        self.assertRaises(TypeError, rps_game_winner, "Wrong data")

    def test_list__with_not_two_elements_raises_wrong_number_players_error(self):
        self.assertRaises(WrongNumberOfPlayersError, rps_game_winner,
                          [['player1', 'P'], ['player2', 'S'], ['player3', 'S']])

    def test_player_data_given_not_in_list_raises_type_error(self):
        self.assertRaises(TypeError, rps_game_winner, ['ISILDUR, P', ['player2', "S"]])

    def test_player_data_contains_not_two_elements_raises_data_format_error(self):
        self.assertRaises(PlayerDataFormatError, rps_game_winner, [['player1', 'P', 'R'], ['player2', 2]])

    def test_player_name_not_string_raises_type_error(self):
        self.assertRaises(TypeError, rps_game_winner, [[1, 'P'], ['player2', "R"]])

    def test_wrong_player_action_raises_wrong_strategy_error(self):
        self.assertRaises(NoSuchStrategyError, rps_game_winner, [['player1', 'P'], ['player2', 'A']])

    def test_player_two_scissors_is_winner(self):
        self.assertEqual(rps_game_winner([['player1', 'P'], ['player2', 'S']]), 'player2 S')

    def test_player_one_is_winner_both_players_same_action(self):
        self.assertEqual(rps_game_winner([['player1', 'P'], ['player2', 'P']]), 'player1 P')

    def test_player_two_paper_is_winner(self):
        self.assertEqual(rps_game_winner([['Bob', 'R'], ['Alice', 'P']]), 'Alice P')

    def test_player_one_rock_is_winner(self):
        self.assertEqual(rps_game_winner([['Bob', 'R'], ['Alice', 'S']]), 'Bob R')


if __name__ == '__main__':
    unittest.main()

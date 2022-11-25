from typing import List


class WrongNumberOfPlayersError(Exception):
    """ Incorrect number of players is given """


class NoSuchStrategyError(Exception):
    """ Incorrect action is given """


ALLOWED_ACTIONS = ("P", "R", "S")


def rps_game_winner(players_actions: List[List[str]]) -> str:

    if len(players_actions) != 2:
        raise WrongNumberOfPlayersError("There should be exactly 2 players!")

    player_one = players_actions[0]
    player_two = players_actions[1]

    player_one_action = player_one[1]
    player_two_action = player_two[1]

    if player_one_action not in ALLOWED_ACTIONS or player_two_action not in ALLOWED_ACTIONS:
        raise NoSuchStrategyError("Allowed actions include 'R'-rock, 'P'-paper or 'S'-scissors only!")

    players_actions_dict = dict()
    for player_action in players_actions:
        players_actions_dict[player_action[0]] = player_action[1]

    if player_one_action == player_two_action:
        winner_result = f"{player_one[0]} {player_one[1]}"
    else:
        winner_action = who_is_winner([player_one_action,  player_two_action])
        for name, action in players_actions_dict.items():
            if action == winner_action:
                winner_name = name

        winner_result = f"{winner_name} {winner_action}"

    return winner_result


def who_is_winner(actions: List[str]) -> str:

    if "R" in actions and "S" in actions:
        winner = "R"
    elif "R" in actions and "P" in actions:
        winner = "P"
    elif "S" in actions and "P" in actions:
        winner = "S"
    else:
        winner = actions[0]

    return winner


test_data = [
    # [['player1', 'P'], ['player2', 'S'], ['player3', 'S']],
    # [['player1', 'P'], ['player2', 'A']],
    [['player1', 'P'], ['player2', 'S']],
    [['player1', 'P'], ['player2', 'P']]
    ]

if __name__ == "__main__":
    for data in test_data:
        print(rps_game_winner(data))

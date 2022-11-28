from typing import List


class WrongNumberOfPlayersError(Exception):
    """ Incorrect number of players is given """


class NoSuchStrategyError(Exception):
    """ Incorrect action is given """


class PlayerDataFormatError(Exception):
    """ Player's data include more or less elements, than name and action  """


ALLOWED_ACTIONS = ("P", "R", "S")


def rps_game_winner(players_actions: List[List[str]]) -> str:
    """ Returns name and action of the winner in Rock-Paper-Scissors game.
    Raises appropriate exceptions if the given data is in wrong format """

    # data checking
    if not isinstance(players_actions, list):
        raise TypeError("List has to be provided for input!")

    if len(players_actions) != 2:
        raise WrongNumberOfPlayersError("There should be exactly 2 players!")

    player_one = players_actions[0]
    player_two = players_actions[1]

    if not isinstance(player_one, list) or \
            not isinstance(player_two, list):
        raise TypeError("Player's name and action should be given in list!")

    if len(player_one) != 2 or len(player_two) != 2:
        raise PlayerDataFormatError("Player's list should include exactly"
                                    " two elements: 'name' and 'action'!")

    player_one_name = player_one[0]
    player_two_name = player_two[0]

    if not isinstance(player_one_name, str) or \
            not isinstance(player_two_name, str):
        raise TypeError("Player's name should be of 'str' type!")

    player_one_action = player_one[1]
    player_two_action = player_two[1]

    if player_one_action not in ALLOWED_ACTIONS or \
            player_two_action not in ALLOWED_ACTIONS:
        raise NoSuchStrategyError("Allowed actions include only: "
                                  "'R'-rock, 'P'-paper or 'S'-scissors!")

    # method logic
    winning_action_index = define_winning_action_index([player_one_action, player_two_action])
    winner = players_actions[winning_action_index]
    winner_data = f"{winner[0]} {winner[1]}"

    return winner_data


def define_winning_action_index(actions: List[str]) -> int:
    """ Gets list with exactly two allowed actions in RPS game
    and defines index of the winning action: 0 or 1 """

    if "R" in actions and "S" in actions:
        winning_action = "R"
    elif "R" in actions and "P" in actions:
        winning_action = "P"
    elif "S" in actions and "P" in actions:
        winning_action = "S"
    else:  # same actions
        winning_action = actions[0]
    return actions.index(winning_action)


test_data = [
    [['player1', 'P'], ['player2', 'S'], ['player3', 'S']],
    [['player1', 'P'], ['player2', 'A']],
    [['player1', 'P'], ['player2', 'S']],
    [['player1', 'P'], ['player2', 'P']],
    [['player1', 'P'], ['player2', 2]],
    [[1, 'P'], ['player2', "R"]],
    ['ISILDUR, P', ['player2', "S"]],
    [['Bob', 'R'], ['Alice', 'P']],
    [['Bob', 'R'], ['Alice', 'S']],
    ]

if __name__ == "__main__":
    for data in test_data:
        try:
            print(rps_game_winner(data))
        except Exception as e:
            print(e)
            continue



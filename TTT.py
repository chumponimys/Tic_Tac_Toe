# TTT.py - Main Tic Tac Toe File
# Ari Cohen

from TTT_interface import *
from TTT_state import *
from TTT_player import *

def quarto(player_1, player_2, interface_state):
    game_state = GameState(interface_state)
    game_status = GameStatus.PLAYING
    toggle_player_turns = -1
    turn_player = player_1
    display_game_state(game_state)
    while game_status == GameStatus.PLAYING:
        toggle_player_turns = -toggle_player_turns
        if toggle_player_turns == 1:
            turn_player = player_1
        else:
            turn_player = player_2
        while True:
            [move, game_status] = turn_player.get_move(game_state)
            if game_status == GameStatus.QUITTING: 
                break
            [move_check, game_status] = check_move(game_state,move)
            if move_check == MoveStatus.LEGAL_MOVE:
                make_move_and_display(game_state, move)
                break
            else:
                display_game_state(game_state)
                signal_bad_move(move, move_check, turn_player) 
    final_move = turn_player
    return [game_state, game_status, final_move, player_1, player_2]



while True:
        interface_state = MainInterface()
        player_1 = GamePlayer()
        player_1.player_num = "1"
        player_2 = GamePlayer()
        player_2.player_num = "2"
        get_players_info(player_1, player_2, interface_state)
        [game_state, game_status, final_move, player_1, player_2] = quarto(player_1, player_2, interface_state)
        signal_end_of_game(game_status, game_state, player_1, player_2, final_move)

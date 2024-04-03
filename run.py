from random import randint


def initialize_game_boards():
    '''
        Initialize game boards before the game
    '''

    
    player_hidden_pattern = [[' '] * 8 for _ in range(8)]
    player_guess_pattern = [[' '] * 8 for _ in range(8)]
    computer_hidden_pattern = [[' '] * 8 for _ in range(8)]
    computer_guess_pattern = [[' '] * 8 for _ in range(8)]

    return (player_hidden_pattern,
            player_guess_pattern,
            computer_hidden_pattern,
            computer_guess_pattern)


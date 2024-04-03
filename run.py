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
            

def print_boards(board1, board2,
                 board1_title="Your Guesses", board2_title="Computer's Guesses"):
    '''
        Function to print two game boards side by side

        input : 
            board1 : list of characters related to the user
            board2 : list of characters related to the computer
            board1_title : title of the user board
            board2_title : title of the computer board

        output : 
            prints the title of two boards and then the boards themselves

    '''

    
    print(f'{board1_title:20s}    {board2_title}')
    print('   A B C D E F G H      A B C D E F G H')
    print('   ****************     ****************')

    
    for row_num in range(8):
        row1 = " ".join(board1[row_num])
        row2 = " ".join(board2[row_num])
        print(f"{row_num + 1}|{row1}|    {row_num + 1}|{row2}|")
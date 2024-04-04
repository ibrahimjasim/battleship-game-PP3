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


def get_row_from_user():
    '''
        Get the row as a input from the user and then
        validate the user input. If it is not correct,
        let the user again enter the row. Once a valid 
        input is detected, convert that to an int and return.
    '''

    while True:
        row = input('Please enter a ship row (1-8): ')

        
        if row not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Please enter a valid row ( 1<= row <= 8 ) ")
            continue
        else:
            return int(row)-1
            

def get_col_from_user():
    '''
        Get the column as a input from the user and then
        validate the user input. If it is not correct,
        let the user again enter the row. Once a valid 
        input is detected, get the corresponding index value and return.

    '''

    
    letters_to_index_mapping = {'A': 0, 'B': 1,
                                'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    while True:
        column = input('Please enter a ship column (A-H): ').upper()

        
        if column not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            print("Please enter a valid column ( A <= column <= H ) ")
            continue
        else:
            return letters_to_index_mapping[column]


def get_computer_location():
    '''
        Get the location choosen by the computer. This location
        is randomly decided.
    '''
    
    return randint(0, 7), randint(0, 7)



def create_ships(board, num_ships):
    '''
        This function places ships on the board randomly.

        input : number of ships to be placed on the board.
    '''

    
    for _ in range(num_ships):
        ship_row, ship_col = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_col] == 'X':
            ship_row, ship_col = randint(0, 7), randint(0, 7)
        board[ship_row][ship_col] = 'X'


def count_hit_ships(board):
    '''
        Count the number of ships that are hit.

        input : board to count the hit number of ships
    '''

    
    return sum(row.count('X') for row in board)

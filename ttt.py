

# TIC TAC TOE


# Initialize a board state
board = [[None, None, None], [None, None, None], [None, None, None]]


# board = [['X', 'X', 'X'],['X', 'X', 'X'],['X', 'X', 'X']]

# print board

def print_board(x):
    for i in range(3):
        for j in range(3):
            print(x[i][j], ' | ', end="")
        print()
        print("---------------------")


def check_gameover(x):
    if x[0][0] == x[0][1] == x[0][2] != None:
        print('winner is :', x[0][0])
        return True
    elif   x[1][0] == x[1][1] == x[1][2] != None:
        print('winner is :', x[1][0])
        return True
    elif   x[2][0] == x[2][1] == x[2][2] != None:
        print('winner is :', x[2][0])
        return True
    elif   x[0][0] == x[1][0] == x[2][0] != None:
        print('winner is :', x[0][0])
        return True
    elif   x[0][1] == x[1][1] == x[2][1] != None:
        print('winner is :', x[0][1])
        return True
    elif   x[0][2] == x[1][2] == x[2][2] != None:
        print('winner is :', x[0][2])
        return True
    elif   x[0][2] == x[1][2] == x[2][2] != None:
        print('winner is :', x[0][2])
        return True
    elif   x[0][0] == x[1][1] == x[2][2] != None:
        print('winner is :', x[0][0])
        return True
    elif   x[0][2] == x[1][1] == x[2][0] != None:
        print('winner is :', x[0][2])
        return True
    else:
        count_n = 0
        for i in range(3):
            for j in range(3):
                if x[i][j] == None:
                    count_n += 1
        if count_n == 0:
            print('draw')
            return True
        else:
            return False


def check_turn(x):
    count_x = 0
    count_o = 0
    count_n = 0
    for i in range(3):
        for j in range(3):
            if x[i][j] == 'X':
                count_x += 1
            elif x[i][j] == 'O':
                count_o += 1
            else:
                count_n += 1
    if count_n == 0:
        return ('Game over')
    elif count_x == count_o:
        return 'X'
    else:
        return 'O'


def get_input(x):
    if check_turn(x) is not 'Game over':
        pos_x = int(input("Input row :"))
        pos_y = int(input("Input column :"))
        return (pos_x, pos_y)
    else:
        return ('Game over')


# pos = get_input(board)

def check_move(x, pos):
    if x[pos[0]][pos[1]] == None:
        return True
    else:
        return False


while check_gameover(board) is not True:
    player = check_turn(board)
    print('turn of' + player)
    print_board(board)
    pos = get_input(board)
    if check_move(board, pos) is False:
        while check_move(board,pos) is False:
            print('invalid position. please fill a valid position')
            pos = get_input(board)
    else:
        board[pos[0]][pos[1]] = player

    #check_gameover(board)



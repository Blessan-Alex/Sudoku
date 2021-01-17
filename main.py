import colorama
from colorama import Fore, Back, Style
colorama.init()

board = [
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 7, 0, 0, 1, 0, 5, 0, 0],
    [4, 0, 0, 0, 0, 5, 3, 0, 0],
    [0, 1, 0, 0, 7, 0, 0, 0, 6],
    [0, 0, 3, 2, 0, 0, 0, 8, 0],
    [0, 6, 0, 5, 0, 0, 0, 0, 9],
    [0, 0, 4, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 9, 7, 0, 0]
]


# This functon is for information purpose only
# Just to refer the postions of the elements

# ****************************************
def know_postions(b):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(i, j)
# ****************************************

# algoruthm


def is_solve(b):
    find = is_empty(b)
    # base case is the board is full[which means we reached the end and thus solved]
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(b, i, (row, col)):
            # i is the num and its checks if its valid, if it is then add it
            b[row][col] = i

            if is_solve(b):
                return True

            b[row][col] = 0

    return False  # if 1-10 looping is over, then return false, then is_solve is false , reset it


def is_valid(b, num, pos):
    # Checking the row
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i:
            # pos[0]
            # so at first b[0][0] then checks the entire row whether the number we entered is there till 8
            # pos[1] != i means we just inserted num to that, we dont need to check that again
            return False

    # Checking the column
    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[0] != i:
            # b[0][0]
            # checks vertically down
            return False

    # Checking the box
    box_x = pos[1] // 3  # returns 0 , 1 or 2
    box_y = pos[0] // 3  # returns 0, 1 or 2

    for i in range(box_y * 3, box_y * 3 + 3):  # if we are in box 2, 2*3= index 6
        for j in range(box_x * 3, box_x * 3 + 3):
            if b[i][j] == num and (i, j) != pos:
                # check any other is equal to the one we added
                # we dont need to check the position of what we just added
                return False
    return True  # if we reach here then its a valid position


def pretty_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:

                print(" | ", end="")
            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")


def is_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0 or b[i][j] == ' ':
                return (i, j)  # returns the postion where its empty
                # row , col
    return None  # if no blank squares then say None , so that we can go to find_empty and put true


if __name__ == "__main__":
    print()
    print(Fore.BLACK+Back.WHITE+"THE BOARD TO BE SOLVED :")
    print(Fore.RESET+Back.RESET)
    pretty_board(board)
    is_solve(board)
    print()
    print(Fore.BLACK+Back.WHITE+"THE SOLVED BOARD:")
    print(Fore.RESET+Back.RESET+Style.BRIGHT)
    pretty_board(board)

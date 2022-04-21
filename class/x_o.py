# def displayBoard():
#     db_row1 = [" _", " _", " _"]
#     db_row2 = [" _", " _", " _"]
#     db_row3 = [" _", " _", " _"]
#
#     for i in db_row1:
#         print(i,"|" ,end=" ")
#     print(" ")
#     for i in db_row2:
#         print(i, "|",end=" ")
#     print(" ")
#     for i in db_row3:
#         print (i, "|",end=" ")
#

def print_board(boards):
    for board in boards:
        for cell in board:
            print(cell, end=" ")
        print()


def printing_board(boards):
    for board in boards:
        print(" ".join(board))

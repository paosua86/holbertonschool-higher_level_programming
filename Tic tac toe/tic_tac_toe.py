#!/usr/bin/python3
from collections import deque



turn = deque(["0","X"])
board= [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def rotate_turn():
    turn.rotate()
    return turn[0]

def show_board():
    print ()
    for row in board:
        print (row)

def process_position(position):
    row,column = position.split(",")
    return [int(row)-1, int(column)-1]

def correct_position(position):
    if 0 <= position[0] <= 2 and 0 <= position[1] <= 2:
        if board[position[0]][position[1]] == " ":
            return True
    return False

def update_board(position, player):
    board[position[0]][position[1]] = player

def winner(p):
    if board[0] == [p,p,p] or board[1] == [p,p,p] or board[2] == [p,p,p]:
        return True
    elif board[0][0] == p and board[1][0] == p and board[2][0] == p:
        return True
    elif board[0][1] == p and board[1][1] == p and board[2][1] == p:
        return True
    elif board[0][2] == p and board[1][2] == p and board[2][2] == p:
        return True
    #diagonal
    elif board[0][0] == p and board[1][1] == p and board[2][2] == p:
        return True
    elif board[0][2] == p and board[1][1] == p and board[2][0] == p:
        return True
    return False


def game():
    show_board()
    player = rotate_turn()
    while True:
        position = input("{} turn. Choose a row position, column from 1 to 3: ".format(player))
        if position == "exit":
            break
        try:
            position_l = process_position(position)
        except:
            print ("Error, position {} is not valid".format(position))
            continue
        if correct_position(position_l):
            print ("correct")
            update_board(position_l, player)
            show_board()
            
            if winner(player):
                print ("Player {} has won!!".format(player))
                break
            player = rotate_turn()
                        
        else:
            print ("Position {} is not correct".format(position)) 
game()


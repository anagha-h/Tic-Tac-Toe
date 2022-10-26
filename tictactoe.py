"""
Tic Tac Toe Player
"""

import math
import copy
from re import I

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    o_count = 0
    x_count = 0
    for r in board:
        for c in r:
            if c == "X":
                x_count+=1
            if c == "O":
                o_count+=1
    if x_count == o_count or x_count == 0:
        return X
    if x_count > o_count:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                act.add((i, j))
    
    return act


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_cc = copy.deepcopy(board)
    r, c = action
    #c = action[1]
    if board[r][c] != EMPTY:
        raise
    else:
        board_cc[r][c] = player(board)
        return board_cc


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[1][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[1][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[1][2]
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[1][1]
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    elif not any(EMPTY in i for i in board) and winner(board) is None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else: 
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            v = -999
            act = tuple()
            for action in actions(board):
                if(minimize(result(board, action)) > v):
                    v = minimize(result(board, action))
                    act = action
            return act
        else:
            v = 999
            act = tuple()
            for action in actions(board):
                if(maximize(result(board, action)) < v):
                    v = maximize(result(board, action))
                    act = action
            return act

def maximize(board):
    v = -999
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        if minimize(result(board, action)) > v:
            v = minimize(result(board, action))
    return v

def minimize(board):
    v = 999
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        if maximize(result(board, action)) < v:
            v = maximize(result(board, action))
    return v
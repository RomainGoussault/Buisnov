# -*- coding: utf-8 -*-

"""
    A simple evaluation function for testing purposes
    @author: Navid Hedjazian
"""

import chess as ch

QUEEN_VALUE = 900
ROOK_VALUE = 500
KING_VALUE = 10000
KNIGHT_VALUE = 310
BISHOP_VALUE = 325
PAWN_VALUE = 100


def evaluate(board):
    """ This is a simple evaluation function that takes only into account the material 
    :param board: a Board object, i.e. the state of the game
    :return score: the score associated to the Board in centipawns
    """
    score = 0
    w = board.occupied_co[ch.WHITE]
    b = board.occupied_co[ch.BLACK]
    score += (ch.popcount(board.pawns & w) - ch.popcount(board.pawns & b)) * PAWN_VALUE + \
             (ch.popcount(board.knights & w) - ch.popcount(board.knights & b)) * KNIGHT_VALUE + \
             (ch.popcount(board.bishops & w) - ch.popcount(board.bishops & b)) * BISHOP_VALUE + \
             (ch.popcount(board.rooks & w) - ch.popcount(board.rooks & b)) * ROOK_VALUE + \
             (ch.popcount(board.queens & w) - ch.popcount(board.queens & b)) * QUEEN_VALUE + \
             (ch.popcount(board.kings & w) - ch.popcount(board.kings & b)) * KING_VALUE
    return score


def get_moves_scores(eval_func, board):
    moves_scores = []
    for move in board.legal_moves:
        board.push(move)
        moves_scores.append(eval_func(board))
        board.pop()
    return moves_scores

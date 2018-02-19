# -*- coding: utf-8 -*-

"""
    An extension of the board class
    @author: Navid Hedjazian
"""

import chess as ch


class Board(ch.Board):

    def __init__(self, fen=ch.STARTING_FEN):
        ch.Board.__init__(self, fen=fen)
        # TODO : see python-chess Core to handle input FEN
        self.moves_list = list(self.legal_moves)


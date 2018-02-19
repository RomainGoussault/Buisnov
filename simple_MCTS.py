# -*- coding: utf-8 -*-

"""
    A simple implementation of Monte-Carlo Tree search for testing purposes
    @author: Navid Hedjazian
"""

import chess
import simple_eval as eval


class Node:
    def __init__(self, state):
        self.state = state


class MCTS:
    def __init__(self, board):
        self.board = board


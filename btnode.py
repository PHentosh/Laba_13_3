"""
Board node
"""

class BTNode:
    def __init__(self, board=None, left=None, right=None):
        """ init """
        self.board = board
        self.left = left
        self.right = right

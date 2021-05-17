"""
Game board
"""
from random import randrange
from btnode import BTNode
from copy import deepcopy

class Board:
    """
    Game board and previous move
    """
    def __init__(self, board=None):
        """ init """
        if board != None:
            self.board = board
        else:
            self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.last_move = None

    def check_if_win(self, turn):
        """
        check if turn is win
        """
        cros1 = ''
        cros2 = ''
        for i in range(3):
            cros1 += self.board[i][i]
            cros2 += self.board[i][2-i]
            line1 = ''
            line2 = ''
            for j in range(3):
                line1 += self.board[i][j]
                line2 += self.board[j][i]
            if line1 == f'{turn*3}' or line2 == f'{turn*3}':
                return True
        if cros1 == f'{turn*3}' or cros2 == f'{turn*3}':
            return True
        else:
            return False

    def get_status(self):
        """
        Check if someone win or draw or the game is continiuing
        """
        if self.check_if_win('x'):
            return 'x'
        elif self.check_if_win('0'):
            return '0'
        else:
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '':
                        return 'continue'
            return 'draw'

    def make_move(self, position, turn):
        """
        make a move
        """
        try:
            cur_pos = self.board[position[0]][position[1]]
        except IndexError:
            raise IndexError
        if cur_pos !='':
            raise IndexError
        self.last_move = position
        self.board[position[0]][position[1]] = turn

    def make_computer_move(self):
        """
        make a random computer move
        """
        if self.last_move == None:
            return "Make first move"
        elif self.board[self.last_move[0]][self.last_move[1]] == '0':
            return 'Make your move using \'x\''
        else:
            position = self.chose_next_move('0')
            if position == None:
                return 'There is no avaliable moves'
            else:
                self.make_move(position, '0')

    def build_a_tree(self, board):
        """
        build a tree of possible moves
        """
        if board.check_if_win('x') or board.check_if_win('0'):
            return BTNode(board)
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == '':
                    possible_moves.append((i, j))
        if len(possible_moves) == 2:
            if board.last_move == None or board.last_move == '0':
                turn = "x"
            else:
                turn = '0'
            board1 = Board(deepcopy(board.board))
            board1.make_move(possible_moves[0], turn)
            board2 = Board(deepcopy(board.board))
            board2.make_move(possible_moves[1], turn)
            return BTNode(board, BTNode(board1), BTNode(board2))
        elif len(possible_moves) == 1:
            if board.last_move == None or board.last_move == '0':
                turn = "x"
            else:
                turn = '0'
            board1 = Board(deepcopy(board.board))
            board1.make_move(possible_moves[0], turn)
            return BTNode(board, BTNode(board1))
        else:
            if board.last_move == None or board.last_move == '0':
                turn = "x"
            else:
                turn = '0'
            board1 = Board(deepcopy(board.board))
            board1.make_move(possible_moves[0], turn)
            board2 = Board(deepcopy(board.board))
            board2.make_move(possible_moves[1], turn)
            return BTNode(board, self.build_a_tree(board1), self.build_a_tree(board2))

    def calculate(self, boardtree, turn):
        if boardtree.board.get_status() == turn:
            return 1
        elif boardtree.board.get_status() == 'draw':
            return 0
        elif boardtree.board.get_status() == 'continue':
            if boardtree.left != None and boardtree.right != None:
                return self.calculate(boardtree.left, turn) + self.calculate(boardtree.right, turn)
            elif boardtree.left == None and boardtree.right != None:
                return self.calculate(boardtree.right, turn)
            elif boardtree.left != None and boardtree.right == None:
                return self.calculate(boardtree.left, turn)
        else:
            return -1

    def chose_next_move(self, turn):
        """
        """
        possition = None
        tree = Board(deepcopy(self.board))
        chosetree = self.build_a_tree(tree)
        left = self.calculate(chosetree.left, turn)
        right = self.calculate(chosetree.right, turn)
        if left <= right:
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] != chosetree.right.board.board[i][j]:
                        possition = (i, j)
                        break
        elif right < left:
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] != chosetree.left.board.board[i][j]:
                        possition = (i, j)
                        break
        return possition

    def __str__(self):
        string = ''
        for i in range(3):
            string += '['
            for j in range(3):
                string += self.board[i][j]
                string += ', '
            string = string[:-2]
            string += ']\n'
        return string[:-1]

    def clear(self):
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.last_move = None


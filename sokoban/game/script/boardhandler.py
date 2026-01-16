from .board import Board

class BoardHandler():
    @staticmethod
    def create_board(board: Board):
        board.cell = []
        board.thing_list = []
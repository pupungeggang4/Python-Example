class Board():
    @staticmethod
    def flip(board: list[list[int]], pos: list[int]) -> None:
        d: list[list[int]] = [[-1, 0], [0, -1], [0, 1], [1, 0], [0, 0]]
        for i in range(len(d)):
            pos_current: list[int] = [pos[0] + d[i][0], pos[1] + d[i][1]]
            if pos_current[0] >= 0 and pos_current[0] < 7 and pos_current[1] >= 0 and pos_current[1] < 7:
                board[pos_current[0]][pos_current[1]] = 1 - board[pos_current[0]][pos_current[1]]

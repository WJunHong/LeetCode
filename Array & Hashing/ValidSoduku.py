class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0] * 9
        col = [0] * 9
        box = [0] * 9
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != ".":
                    row[int(board[i][j]) - 1] += 1
                    if row[int(board[i][j]) - 1] > 1:
                        return False
                if board[j][i] != ".":
                    col[int(board[j][i]) - 1] += 1
                    if col[int(board[j][i]) - 1] > 1:
                        return False
            row = [0] * 9
            col = [0] * 9

        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(3 * i, (3 * i) + 3):
                    for l in range(3 * j, (3 * j) + 3):
                        if board[k][l] != ".":
                            box[int(board[k][l]) - 1] += 1
                            if box[int(board[k][l]) - 1] > 1:
                                return False
                box = [0] * 9

        return True

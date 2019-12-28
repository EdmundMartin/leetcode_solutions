from typing import List


# Runtime: 1220 ms, faster than 7.72% of Python3 online submissions for Battleships in a Board.
# Memory Usage: 13.3 MB, less than 25.00% of Python3 online submissions for Battleships in a Board.
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board) - 1
        cols = len(board[0]) - 1
        visited = []
        boats = 0
        for row_idx, row in enumerate(board):
            for col_idx, col in enumerate(row):
                if (row_idx, col_idx) in visited:
                    continue
                if board[row_idx][col_idx] == "X":
                    boats += 1
                    horizontal = self.find_horizontal(board, row_idx, col_idx, cols)
                    vertical = self.find_vertical(board, row_idx, col_idx, rows)
                    if horizontal > vertical:
                        visited.extend(horizontal)
                    else:
                        visited.extend(vertical)
        return boats

    def find_horizontal(self, board, start_row, start_col, cols):
        cords = [(start_row, start_col)]
        col = start_col
        while col < cols and board[start_row][col+1] == 'X':
            cords.append((start_row, col+1))
            col += 1
        return cords

    def find_vertical(self, board, start_row, start_col, rows):
        cords = [(start_row, start_col)]
        row = start_row
        while row < rows and board[row+1][start_col] == 'X':
            cords.append((row+1, start_col))
            row += 1
        return cords


class OptimalSolution:
    def countBattleships(self, board: List[List[str]]) -> int:
        X, Y = len(board), len(board[0])

        def is_water(x, y):
            if x < 0 or y < 0:
                return True
            elif x >= X or y > Y:
                return True
            elif board[x][y] == '.':
                return True
            return False

        count = 0
        for row in range(X):
            for col in range(Y):
                if board[row][col] == 'X':
                    if is_water(row, col-1) and is_water(row-1, col):
                        count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    b = s.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]])
    print(b)
    o = OptimalSolution()
    boats = o.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]])
    print(boats)
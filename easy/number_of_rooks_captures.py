"""
Available Captures for Rook
On an 8 x 8 chessboard, there is one white rook. There also may be empty squares,
white bishops, and black pawns.  These are given as characters 'R', '.', 'B',
and 'p' respectively. Uppercase characters represent white pieces, and lowercase
characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions
(north, east, west, and south), then moves in that direction until it chooses to
stop, reaches the edge of the board, or captures an opposite colored pawn by moving
to the same square it occupies.  Also, rooks cannot move into the same square as
other friendly bishops.

Return the number of pawns the rook can capture in one move.


Example 1:
Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation:
In this example the rook is able to capture all the pawns.

Example 2:
Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation:
Bishops are blocking the rook to capture any pawn.

Example 3:
Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation:
The rook can capture the pawns at positions b5, d6 and f5.

Note:
board.length == board[i].length == 8
board[i][j] is either 'R', '.', 'B', or 'p'
There is exactly one cell with board[i][j] == 'R'
"""
from typing import List, Tuple


# Runtime: 32 ms, faster than 87.30% of Python3 online submissions for Available Captures for Rook.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Available Captures for Rook.
class Solution:

    ROOK = 'R'
    TARGET = 'p'

    def get_rook_index(self, board: List[List[str]]) -> Tuple[int, int]:
        for row in range(8):
            for col in range(8):
                if board[row][col] == self.ROOK:
                    return row, col

    def in_bounds(self, row, col):
        if row < 8 and row >= 0 and col >= 0 and col < 8:
            return True
        return False

    def capture(self, rook, board, directions, captures):
        row_dir, col_dir = directions
        row, col = rook
        row += row_dir
        col += col_dir
        while self.in_bounds(row, col):
            if board[row][col] in ['P', 'B', 'R' 'b', 'r']:
                return
            if board[row][col] == self.TARGET:
                captures.append((row, col))
                return
            row = row + row_dir
            col = col + col_dir

    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook = self.get_rook_index(board)
        captures = []
        for i in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            self.capture(rook, board, i, captures)
        return len(captures)


if __name__ == '__main__':
    s = Solution()
    s.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]])
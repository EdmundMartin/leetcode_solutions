from typing import List


# Runtime: 132 ms, faster than 50.56% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row, _ in enumerate(grid):
            col = len(grid[0]) - 1
            while grid[row][col] < 0 and col >= 0:
                count += 1
                col -= 1
        return count


if __name__ == '__main__':
    s = Solution()
    res = s.countNegatives(g2)
    print(res)
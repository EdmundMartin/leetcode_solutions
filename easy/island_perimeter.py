"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular,
width and height don't exceed 100. Determine the perimeter of the island.

Example:
Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
"""
from typing import List


# Runtime: 496 ms, faster than 97.61% of Python3 online submissions for Island Perimeter.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Island Perimeter.
class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total = 0
        if not grid:
            return total
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    # Island found - add 4 to perimeter
                    total += 4
                    # Check row above if island - take two off
                    if row > 0 and grid[row-1][col] == 1:
                        total -= 2
                    # Check column to left - take two off
                    if col > 0 and grid[row][col-1] == 1:
                        total -= 2
        return total


if __name__ == '__main__':
    s = Solution()
    res = s.islandPerimeter([[0,1,0,0],
                        [1,1,1,0],
                        [0,1,0,0],
                        [1,1,0,0]])
    print(res)
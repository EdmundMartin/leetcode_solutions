"""
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell
there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same
row or on the same column.

Return the number of servers that communicate with any other server.

Example 1:
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Example 3:
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other.
The two servers in the third column can communicate with each other. The server at right bottom corner
can't communicate with any other server.


Constraints:
m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
"""
from typing import List
from collections import defaultdict


# Runtime: 504 ms, faster than 90.29% of Python3 online submissions for Count Servers that Communicate.
# Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Count Servers that Communicate.
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    rows[x].append((x, y))
                    cols[y].append((x, y))
        results = []
        for res in rows.values():
            if len(res) > 1:
                results.extend(res)
        for res in cols.values():
            if len(res) > 1:
                results.extend(res)
        return len(set(results))


if __name__ == '__main__':
    s = Solution()
    s.countServers([[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]])
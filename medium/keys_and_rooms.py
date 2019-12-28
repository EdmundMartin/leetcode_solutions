from typing import List


# Runtime: 68 ms, faster than 90.96% of Python3 online submissions for Keys and Rooms.
# Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Keys and Rooms.
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        stack = [rooms[0]]
        while stack:
            values = stack.pop()
            for value in values:
                if value not in visited:
                    stack.append(rooms[value])
                    visited.add(value)
        return len(visited) == len(rooms)


if __name__ == '__main__':
    s = Solution()
    res = s.canVisitAllRooms([[1],[2],[3],[]])
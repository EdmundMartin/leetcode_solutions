"""
Students are asked to stand in non-decreasing order of heights for an annual photo.
Return the minimum number of students not standing in the right positions.
(This is the number of students that must move in order for all students to be standing
in non-decreasing order of height.)


Example 1:
Input: [1,1,4,2,1,3]
Output: 3
Explanation:
Students with heights 4, 3 and the last 1 are not standing in the right positions.

Note:
1 <= heights.length <= 100
1 <= heights[i] <= 100
"""
from typing import List


# Runtime: 44 ms, faster than 54.91% of Python3 online submissions for Height Checker.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Height Checker.
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    s.heightChecker([1,1,4,2,1,3])
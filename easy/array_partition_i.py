"""
Array Partition I
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
"""
from typing import List


# Runtime: 300 ms, faster than 93.05% of Python3 online submissions for Array Partition I.
# Memory Usage: 15.2 MB, less than 6.06% of Python3 online submissions for Array Partition I.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        total = 0
        nums = sorted(nums)
        for i in range(0, len(nums), 2):
            if nums[i] < nums[i + 1]:
                total += nums[i]
            else:
                total += nums[i + 1]
        return total


if __name__ == '__main__':
    s = Solution()
    res = s.arrayPairSum([1, 2, 3, 4])
    print(res)
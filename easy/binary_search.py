"""
704. Binary Search
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search
target in nums. If target exists, then return its index, otherwise return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Note:
You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
"""
from typing import List


# Runtime: 260 ms, faster than 74.33% of Python3 online submissions for Binary Search.
# Memory Usage: 14 MB, less than 90.32% of Python3 online submissions for Binary Search.
class Solution:

    def binary_search(self, nums: List[int], target: int, start: int, end: int) -> int:
        if start > end:
            return -1
        middle = (start+end) // 2
        current = nums[middle]
        if current == target:
            return middle
        elif current > target:
            return self.binary_search(nums, target, 0, middle-1)
        else:
            return self.binary_search(nums, target, middle+1, end)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums)-1)


if __name__ == '__main__':
    s = Solution()
    res = s.search([-1, 0, 5], 5)
    print(res)
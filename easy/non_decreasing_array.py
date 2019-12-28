"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: [4,2,1]
Output: False

Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""
from typing import List


# Runtime: 200 ms, faster than 96.61% of Python3 online submissions for Non-decreasing Array.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Non-decreasing Array.
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if self.is_sorted_ascending(nums):
            return True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return self.is_sorted_ascending(nums[:i] + nums[i+1:]) or \
                       self.is_sorted_ascending(nums[:i+1] + nums[i+2:])
        return True

    def is_sorted_ascending(self, nums: List[int]):
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    res = s.checkPossibility([3,4,2,3])
    print(res)
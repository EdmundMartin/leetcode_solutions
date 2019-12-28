"""
283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
from typing import List


# Runtime: 48 ms, faster than 92.58% of Python3 online submissions for Move Zeroes.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Move Zeroes.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] == 0:
                nums.pop(left)
                nums.append(0)
                right -= 1
            else:
                left += 1

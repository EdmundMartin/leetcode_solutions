"""
287. Find the Duplicate Number
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
from typing import List


# Runtime: 64 ms, faster than 81.76% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 15.3 MB, less than 17.86% of Python3 online submissions for Find the Duplicate Number.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            left = nums[i]
            right = nums[i + 1]
            if left == right:
                return left

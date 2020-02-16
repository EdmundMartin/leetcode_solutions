"""
35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it
would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
"""
from typing import List


class Solution:

    def binary_search_between(self, nums: List[int], target: int, start: int, end: int) -> int:
        if start > end:
            return start
        middle = (start + end) // 2
        if nums[middle] == target:
            return middle
        if nums[middle] > target:
            return self.binary_search_between(nums, target, start, middle - 1)
        else:
            return self.binary_search_between(nums, target, middle + 1, end)

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search_between(nums, target, 0, len(nums) - 1)
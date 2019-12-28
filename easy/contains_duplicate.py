"""
Contains Duplicate
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
from typing import List


# Runtime: 136 ms, faster than 69.21% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 18.2 MB, less than 88.68% of Python3 online submissions for Contains Duplicate.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        results = set()
        for i in nums:
            if i not in results:
                results.add(i)
            else:
                return True
        return False


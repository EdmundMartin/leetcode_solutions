"""
219. Contains Duplicate II
Given an array of integers and an integer k, find out whether there are two distinct indices i and j
in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
from typing import List


# Runtime: 100 ms, faster than 77.32% of Python3 online submissions for Contains Duplicate II.
# Memory Usage: 23.7 MB, less than 18.75% of Python3 online submissions for Contains Duplicate II.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexes = {}
        for i in range(len(nums)):
            current = nums[i]
            if current not in indexes:
                indexes[current] = [i]
            else:
                values = indexes[current]
                if min([i - val for val in values]) <= k:
                    return True
                indexes[current].append(i)
        return False

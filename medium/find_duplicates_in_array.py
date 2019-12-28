"""
442. Find All Duplicates in an Array
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
from typing import List


# Runtime: 392 ms, faster than 89.60% of Python3 online submissions for Find All Duplicates in an Array.
# Memory Usage: 20.2 MB, less than 35.71% of Python3 online submissions for Find All Duplicates in an Array.
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        rep = []
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                rep.append(nums[i])
        return list(set(rep))
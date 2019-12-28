"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


# Runtime: 1400 ms, faster than 30.06% of Python3 online submissions for 3Sum.
# Memory Usage: 16.1 MB, less than 100.00% of Python3 online submissions for 3Sum.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        array = sorted(nums)
        triplets = []
        for i in range(len(array) - 2):
            if array[i] > 0:
                break
            if i > 0 and array[i] == array[i-1]:
                continue
            left, right = i+1, len(array) - 1
            while left < right:
                current = [array[i], array[left], array[right]]
                if sum(current) == 0:
                    triplets.append(current)
                    while left < right and array[left] == array[left+1]:
                        left += 1
                    left += 1
                    while left < right and array[right] == array[right-1]:
                        right -= 1
                    right -= 1
                elif sum(current) > 0:
                    right -= 1
                else:
                    left += 1
        return triplets

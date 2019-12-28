"""
Sort An Array
Given an array of integers nums, sort the array in ascending order.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

Constraints:
1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
"""

from typing import List


# Runtime: 272 ms, faster than 73.42% of Python3 online submissions for Sort an Array.
# Memory Usage: 19.6 MB, less than 64.29% of Python3 online submissions for Sort an Array.
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        less = []
        equal = []
        greater = []
        if len(nums) > 1:
            pivot = nums[0]
            for x in nums:
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                elif x > pivot:
                    greater.append(x)
            return self.sortArray(less) + equal + self.sortArray(greater)
        return nums

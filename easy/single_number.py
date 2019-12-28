"""
136. Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
"""
from typing import List


# Runtime: 88 ms, faster than 90.41% of Python3 online submissions for Single Number.
# Memory Usage: 15.1 MB, less than 18.03% of Python3 online submissions for Single Number.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        target = set()
        for num in nums:
            if num in target:
                target.remove(num)
            else:
                target.add(num)
        return list(target)[0]


if __name__ == '__main__':
    s = Solution()
    res = s.singleNumber([4, 1, 2, 1, 2])
    print(res)
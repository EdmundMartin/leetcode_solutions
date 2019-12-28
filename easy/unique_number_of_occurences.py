"""
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.



Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true


Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""
from typing import List


# Runtime: 36 ms, faster than 94.07% of Python3 online submissions for Unique Number of Occurrences.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Unique Number of Occurrences.
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mapping = {}
        for item in arr:
            if item not in mapping:
                mapping[item] = 1
            else:
                mapping[item] += 1
        return len(mapping.keys()) == len(set(mapping.values()))
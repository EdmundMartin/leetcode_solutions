"""
1287. Element Appearing More Than 25% In Sorted Array
Given an integer array sorted in non-decreasing order, there is exactly one integer
in the array that occurs more than 25% of the time.

Return that integer.

Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Constraints:
1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
"""
from typing import List


# Runtime: 96 ms, faster than 56.51% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        occuring = {}
        quarter = len(arr) // 4
        for el in arr:
            if el not in occuring:
                occuring[el] = 1
            else:
                occuring[el] += 1
            if occuring[el] > quarter:
                return el


# Runtime: 92 ms, faster than 80.42% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
class FasterSolution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr) // 4
        current_el = None
        current_count = 0
        for el in arr:
            if current_el != el:
                current_el = el
                current_count = 1
            else:
                current_count += 1
            if current_count > quarter:
                return current_el

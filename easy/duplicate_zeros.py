"""
Given a fixed length array arr of integers, duplicate each occurrence of zero,
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.


Example 1:
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]

Note:
1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""
#TODO Implement optimal solution
from typing import List


# Runtime: 588 ms, faster than 10.73% of Python3 online submissions for Duplicate Zeros.
# Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Duplicate Zeros.
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if 0 not in arr:
            return
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr[:] = arr[:i] + [0] + arr[i:-1]
                i += 2
            else:
                i += 1
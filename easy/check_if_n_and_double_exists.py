"""
1346. Check If N and Its Double Exist
Given an array arr of integers, check if there exists two integers N and M such that N is the double of
M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]


Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Example 2:
Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

Example 3:
Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.


Constraints:
2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3
"""
from typing import List


# Runtime: 64 ms, faster than 20.14% of Python3 online submissions for Check If N and Its Double Exist.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Check If N and Its Double Exist.
class Solution:

    def binary_search(self, array: List[int], target: int, start: int, end: int):
        if start > end:
            return False
        middle = (start + end) // 2
        if array[middle] == target:
            return True
        elif array[middle] > target:
            return self.binary_search(array, target, start, middle-1)
        else:
            return self.binary_search(array, target, middle+1, end)

    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in arr:
            double = i * 2
            if i == 0 and arr.count(i) == 1:
                continue
            if self.binary_search(arr, double, 0, len(arr)-1):
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    res = s.checkIfExist([-2,0,10,-19,4,6,-8])
    print(res)
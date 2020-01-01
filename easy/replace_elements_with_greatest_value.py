"""
1299. Replace Elements with Greatest Element on Right Side
Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1.
After doing so, return the array.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

Constraints:
1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
"""
from typing import List


# Runtime: 84 ms, faster than 53.94% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
# Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            temp = current_max
            if arr[i] > current_max:
                current_max = arr[i]
            arr[i] = temp
        return arr


if __name__ == '__main__':
    s = Solution()
    res = s.replaceElements([17, 18, 5, 4, 6, 1])
    print(res)
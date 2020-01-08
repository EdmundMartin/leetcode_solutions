"""
905. Sort Array By Parity
Given an array A of non-negative integers, return an array consisting of all the even elements of A,
followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:
1 <= A.length <= 5000
0 <= A[i] <= 5000
"""
from typing import List


# Runtime: 76 ms, faster than 92.18% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 13.3 MB, less than 98.70% of Python3 online submissions for Sort Array By Parity.
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even_part = [num for num in A if num % 2 == 0]
        odd_part = [num for num in A if num % 2 != 0]
        return even_part + odd_part

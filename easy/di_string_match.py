"""
DI String Match
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]

Example 1:
Input: "IDID"
Output: [0,4,1,3,2]

Example 2:
Input: "III"
Output: [0,1,2,3]

Example 3:
Input: "DDI"
Output: [3,2,0,1]
"""
from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        maxi, mini = len(S), 0
        result = []
        for char in S:
            if char == 'I':
                result.append(mini)
                mini += 1
            else:
                result.append(maxi)
                maxi -= 1
        result.append(maxi)
        return result


if __name__ == '__main__':
    s = Solution()
    res = s.diStringMatch("IDID")
    print(res)
"""
Buddy Strings
Given two strings A and B of lowercase letters, return true if and
only if we can swap two letters in A so that the result equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true

Example 2:
Input: A = "ab", B = "ab"
Output: false

Example 3:
Input: A = "aa", B = "aa"
Output: true

Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false

Note:
0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""
from typing import List


# Runtime: 24 ms, faster than 99.80% of Python3 online submissions for Buddy Strings.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Buddy Strings.
class Solution:

    def can_swap_elements(self, A: str, B: str, indxs: List[int]) -> bool:
        # Array will always be two in length so we just check if we and swap elements
        if A[indxs[0]] != B[indxs[1]] or B[indxs[0]] != A[indxs[1]]:
            return False
        return True

    def buddyStrings(self, A: str, B: str) -> bool:
        a_length = len(A)
        if a_length != len(B):
            return False
        comparison = [i for i in range(a_length) if A[i] != B[i]]
        if len(comparison) > 2:
            return False
        if len(comparison) == 2:
            return self.can_swap_elements(A, B, comparison)
        # Handles cases such as "aa" and "bb" where both elements are the same but can be swapped
        if a_length > len(set(A)):
            return True
        return False

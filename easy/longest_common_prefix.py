"""
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
"""
from typing import List


# Runtime: 28 ms, faster than 95.28% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.
class Solution:

    def smallest_size(self, strs: List[str]) -> int:
        smallest = len(strs[0])
        for i in range(1, len(strs)):
            current = len(strs[i])
            if current < smallest:
                smallest = current
        return smallest

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        if len(set(strs)) == 1:
            return strs[0]

        result = ""
        smallest = self.smallest_size(strs)

        for idx in range(smallest):
            test_char = strs[0][idx]
            for str_idx in range(1, len(strs)):
                if strs[str_idx][idx] != test_char:
                    return result
            result += test_char
        return result

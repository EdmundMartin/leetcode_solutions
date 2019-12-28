"""
Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
"""

# Runtime: 140 ms, faster than 36.01% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14 MB, less than 6.52% of Python3 online submissions for First Unique Character in a String.
class NonOptimalSolution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        for idx, ch in enumerate(s):
            if ch not in chars:
                chars[ch] = [idx]
            else:
                chars[ch].append(idx)
        index = -1
        for key, value in chars.items():
            if len(value) == 1:
                if index == -1:
                    index = value[0]
                else:
                    index = min(value[0], index)
        return index


class Solution:
    def firstUniqChar(self, s: str) -> int:

        sorted_set = sorted(set(s), key=s.index)

        for ch in sorted_set:
            if s.count(ch) == 1:
                return s.index(ch)
        return -1

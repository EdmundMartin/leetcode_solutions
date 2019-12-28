"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


# Runtime: 1396 ms, faster than 5.02% of Python3 online submissions for Valid Anagram.
# Memory Usage: 13.2 MB, less than 87.50% of Python3 online submissions for Valid Anagram.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = list(s)
        for ch in t:
            if ch not in chars:
                return False
            chars.remove(ch)
        return len(chars) == 0


# Runtime: 48 ms, faster than 78.97% of Python3 online submissions for Valid Anagram.
# Memory Usage: 13.5 MB, less than 34.38% of Python3 online submissions for Valid Anagram.
class SolutionOptimised:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

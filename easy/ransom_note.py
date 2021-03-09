"""
383. Ransom Note
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:

You may assume that both strings contain only lowercase letters.
"""
from collections import defaultdict


# Runtime: 64 ms, faster than 48.97% of Python3 online submissions for Ransom Note.
# Memory Usage: 14.3 MB, less than 64.70% of Python3 online submissions for Ransom Note.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_count = defaultdict(int)
        for ch in magazine:
            letter_count[ch] += 1
        for ch in ransomNote:
            letter_count[ch] -= 1
            if letter_count[ch] < 0:
                return False
        return True

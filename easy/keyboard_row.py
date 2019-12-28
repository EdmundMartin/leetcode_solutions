"""
Given a List of words, return the words that can be typed using letters of alphabet
on only one row's of American keyboard like the image below.

Example:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""
from typing import List


# Runtime: 28 ms, faster than 91.19% of Python3 online submissions for Keyboard Row.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Keyboard Row.
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ch_rows = {}
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        for idx, r in enumerate(rows):
            for ch in r:
                ch_rows[ch.lower()] = idx
        result = []
        for word in words:
            idx = ch_rows[word[0].lower()]
            same_row = [ch_rows[ch.lower()] for ch in word[1:]]
            if all([idx == i for i in same_row]):
                result.append(word)
        return result


if __name__ == '__main__':
    s = Solution()
    res = s.findWords(["Hello", "Alaska", "Dad", "Peace"])
    print(res)
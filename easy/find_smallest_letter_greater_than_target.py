"""
744. Find Smallest Letter Greater Than Target
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the
smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
"""
from typing import List


# Runtime: 112 ms, faster than 71.42% of Python3 online submissions for Find Smallest Letter Greater Than Target.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Find Smallest Letter Greater Than Target.
class Solution:

    def binary_search(self, letters: List[str], target: str, start: int, end: int):
        if start > end:
            return start
        middle = (start + end) // 2
        if letters[middle] == target:
            return middle
        elif letters[middle] < target:
            return self.binary_search(letters, target, middle +1, end)
        else:
            return self.binary_search(letters, target, start, middle -1)

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.sort()
        idx = self.binary_search(letters, target, 0, len(letters)-1)
        if idx > len(letters) - 1:
            return letters[0]
        if letters[idx] != target:
            return letters[idx]
        while letters[idx] == target:
            if idx + 1 > len(letters) - 1:
                idx = 0
            else:
                idx += 1
        return letters[idx]

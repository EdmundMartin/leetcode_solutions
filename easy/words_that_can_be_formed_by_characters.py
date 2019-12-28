"""
Find Words That Can Be Formed by Characters
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation:
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10

Explanation:
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


Note:
1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
"""
from typing import List


def less_chars(word, chars):
    for ch in set(word):
        if word.count(ch) > chars.count(ch):
            return False
    return True


# Runtime: 160 ms, faster than 66.11% of Python3 online submissions for Find Words That Can Be Formed by Characters.
# Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Find Words That Can Be Formed by Characters.
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        found = 0
        for word in words:
            all_letters = all([i in chars for i in word])
            if all_letters and less_chars(word, chars):
                found += len(word)
        return found


if __name__ == '__main__':
    s = Solution()
    res = s.countCharacters(["cat","bt","hat","tree"],"atach")
    print(res)
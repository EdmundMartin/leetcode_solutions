"""
1189. Maximum Number of Balloons
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0

Constraints:
1 <= text.length <= 10^4
text consists of lower case English letters only.
"""


# Runtime: 28 ms, faster than 95.92% of Python3 online submissions for Maximum Number of Balloons.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Maximum Number of Balloons.
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_b = text.count('b')
        count_a = text.count('a')
        count_l = text.count('l') // 2
        count_o = text.count('o') // 2
        count_n = text.count('n')
        if len(set([count_b, count_a, count_l, count_o, count_n])) == 0:
            return count_b
        else:
            return min([count_b, count_a, count_l, count_o, count_n])




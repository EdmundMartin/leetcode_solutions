"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:
Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Example 3:
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Example 4:
Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'


Constraints:
1 <= s.length <= 1000
s[i] = 'L' or 'R'
"""


# Runtime: 28 ms, faster than 95.43% of Python3 online submissions for Split a String in Balanced Strings.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Split a String in Balanced Strings.
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_count = 0
        r_count = 0
        total = 0

        for ch in s:
            if ch == 'R':
                r_count += 1
            else:
                l_count += 1

            if r_count == l_count:
                total += 1
                l_count, r_count = 0, 0
        return total


if __name__ == '__main__':
    s = Solution().balancedStringSplit("RLRRLLRLRL")
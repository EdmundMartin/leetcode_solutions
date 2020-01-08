"""
1309. Decrypt String from Alphabet to Integer Mapping
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

Example 1:
Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:
Input: s = "1326#"
Output: "acz"

Example 3:
Input: s = "25#"
Output: "y"

Example 4:
Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"

Constraints:
1 <= s.length <= 1000
s[i] only contains digits letters ('0'-'9') and '#' letter.
s will be valid string such that mapping is always possible.
"""
from string import ascii_lowercase


# Runtime: 32 ms, faster than 31.23% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
class Solution:

    def get_num(self, idx: int, s: str):
        hash_idx = idx + 2
        if hash_idx <= len(s) - 1 and s[hash_idx] == "#":
            return int(s[idx:hash_idx])
        return int(s[idx])

    def freqAlphabets(self, s: str) -> str:
        idx = 0
        results = []
        while idx < len(s):
            res = self.get_num(idx, s)
            results.append(res-1)
            if res > 9:
                idx += 3
            else:
                idx += 1
        return ''.join([ascii_lowercase[r] for r in results])


if __name__ == '__main__':
    s = Solution()
    res = s.freqAlphabets("10#11#12")
    print(res)

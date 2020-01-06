"""
784. Letter Case Permutation
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""
from typing import List


# Runtime: 48 ms, faster than 92.42% of Python3 online submissions for Letter Case Permutation.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Letter Case Permutation.
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        output = ['']
        for element in S:
            if element.isalpha():
                lower = element.lower()
                upper = element.upper()
                output = [x + lower for x in output] + [x + upper for x in output]
            else:
                output = [x + element for x in output]
        return output


if __name__ == '__main__':
    s = Solution()
    res = s.letterCasePermutation('a1b2')
    print(res)
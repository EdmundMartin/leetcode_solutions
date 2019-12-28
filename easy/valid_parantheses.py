"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false
"""


# Runtime: 32 ms, faster than 92.40% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening, closing = ['(', '{', '['], [')', '}', ']']
        matching_brackets = {')': '(', ']': '[', '}': '{'}
        for br in s:
            if not stack and br in closing:
                return False
            elif stack and br in closing:
                last = stack[len(stack)-1]
                if last == matching_brackets[br]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(br)
        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    result = s.isValid("()[]{}")
    assert result is True

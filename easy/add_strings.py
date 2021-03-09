"""
415. Add Strings
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


# Runtime: 372 ms, faster than 5.56% of Python3 online submissions for Add Strings.
# Memory Usage: 47.9 MB, less than 6.77% of Python3 online submissions for Add Strings.
class Solution:
    chars_to_ints = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }

    def number_from_string(self, num: str, sum: int) -> int:
        if len(num) == 1:
            return self.chars_to_ints[num] + sum
        multiplier = 10 ** (len(num) - 1)
        val = self.chars_to_ints[num[0]] * multiplier + sum
        return self.number_from_string(num[1:], val)

    def addStrings(self, num1: str, num2: str) -> str:
        result = self.number_from_string(num1, 0) + self.number_from_string(num2, 0)
        return str(result)


if __name__ == '__main__':
    s = Solution()
    res = s.addStrings("2130", "102")
    print(res)
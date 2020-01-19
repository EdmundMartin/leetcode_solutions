"""
1323. Maximum 69 Number
Given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Example 1:
Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

Example 2:
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.

Example 3:
Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.

Constraints:
1 <= num <= 10^4
num's digits are 6 or 9.
"""


# Runtime: 28 ms, faster than 66.67% of Python3 online submissions for Maximum 69 Number.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Maximum 69 Number.
class Solution:
    def maximum69Number (self, num: int) -> int:
        res_str = [i for i in str(num)]
        for idx, value in enumerate(res_str):
            if value == '6':
                res_str[idx] = '9'
                break
        return int(''.join(res_str))

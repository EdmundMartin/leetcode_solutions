"""
1281. Subtract the Product and Sum of Digits of an Integer
Given an integer number n, return the difference between the product of its digits and the sum of its digits.


Example 1:
Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

Example 2:
Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21


Constraints:
1 <= n <= 10^5
"""


# Runtime: 28 ms, faster than 57.39% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
class Solution:

    def product_digits(self, n: int) -> int:
        n = str(n)
        if len(n) == 1:
            return int(n)
        product = int(n[0])
        for i in n[1:]:
            product = product * int(i)
        return product

    def sum_digits(self, n: int) -> int:
        n = str(n)
        count = 0
        for i in n:
            count += int(i)
        return count

    def subtractProductAndSum(self, n: int) -> int:
        return self.product_digits(n) - self.sum_digits(n)

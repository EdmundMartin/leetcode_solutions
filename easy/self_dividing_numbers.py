"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number,
including the bounds if possible.

Example 1:

Input:  left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:
The boundaries of each input argument are 1 <= left <= right <= 10000.
"""
from typing import List


# Runtime: 52 ms, faster than 83.80% of Python3 online submissions for Self Dividing Numbers.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Self Dividing Numbers.
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        while left <= right:
            if left > 0 and left < 10:
                nums.append(left)
            else:
                dividing = True
                contains = self.containing_nums(left)
                if 0 not in contains:
                    for i in contains:
                        if left % i != 0:
                            dividing = False
                            break
                    if dividing:
                        nums.append(left)
            left += 1
        return nums

    def containing_nums(self, number):
        return [int(n) for n in str(number)]


if __name__ == '__main__':
    s = Solution()
    out = s.selfDividingNumbers(1, 22)
    print(out)
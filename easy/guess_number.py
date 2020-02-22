"""
374. Guess Number Higher or Lower
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!

Example :
Input: n = 10, pick = 6
Output: 6
"""


# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
def guess(num: int) -> int:
    pass


# Runtime: 28 ms, faster than 54.11% of Python3 online submissions for Guess Number Higher or Lower.
# Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Guess Number Higher or Lower.
class Solution:

    def guessNumber(self, n: int) -> int:
        start = 0
        end = n
        while True:
            middle = (start + end) // 2
            result = guess(middle)
            if result == 0:
                return middle
            elif result == 1:
                start = middle + 1
            elif result == -1:
                end = middle - 1



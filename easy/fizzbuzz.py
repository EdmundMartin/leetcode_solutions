"""
Fizzbuzz
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""
from typing import List


# Runtime: 36 ms, faster than 98.64% of Python3 online submissions for Fizz Buzz.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Fizz Buzz.
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        results = []
        for i in range(1, n + 1):
            if i % 5 == 0 and i % 3 == 0:
                results.append("FizzBuzz")
            elif i % 3 == 0:
                results.append("Fizz")
            elif i % 5 == 0:
                results.append("Buzz")
            else:
                results.append(str(i))
        return results


if __name__ == '__main__':
    s = Solution()
    res = s.fizzBuzz(1)
    print(res)
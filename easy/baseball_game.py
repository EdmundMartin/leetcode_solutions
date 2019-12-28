"""
Baseball Game
You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.

Example 1:
Input: ["5","2","C","D","+"]
Output: 30
Explanation:
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get 2 points. The sum is: 7.
Operation 1: The round 2's data was invalid. The sum is: 5.
Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
Round 4: You could get 5 + 10 = 15 points. The sum is: 30.
Example 2:
Input: ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get -2 points. The sum is: 3.
Round 3: You could get 4 points. The sum is: 7.
Operation 1: The round 3's data is invalid. The sum is: 3.
Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
Round 5: You could get 9 points. The sum is: 8.
Round 6: You could get -4 + 9 = 5 points. The sum is 13.
Round 7: You could get 9 + 5 = 14 points. The sum is 27.
Note:
The size of the input list will be between 1 and 1000.
Every integer represented in the list will be between -30000 and 30000.
"""
from typing import List


def is_int(s: str):
    try:
        int(s)
        return True
    except Exception as e:
        return False


# Runtime: 44 ms, faster than 76.32% of Python3 online submissions for Baseball Game.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Baseball Game.
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        total = 0
        valid_rounds = []
        for i in range(len(ops)):
            if is_int(ops[i]):
                total += int(ops[i])
                valid_rounds.append(int(ops[i]))
            elif ops[i] == 'C':
                val = valid_rounds.pop()
                total -= val
            elif ops[i] == 'D':
                val = valid_rounds[-1]
                total += (val * 2)
                valid_rounds.append(val * 2)
            elif ops[i] == '+':
                vals = valid_rounds[-2:]
                total += sum(vals)
                valid_rounds.append(sum(vals))
        return total


if __name__ == '__main__':
    s = Solution()
    res = s.calPoints(["5","-2","4","C","D","9","+","+"])
    print(res)

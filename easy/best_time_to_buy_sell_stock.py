"""
121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of
the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        mins = [0] * len(prices)
        mins[0] = prices[0]
        for i in range(1, len(prices)):
            mins[i] = min(prices[i-1], prices[i])

        print('-----Mins-----')
        print(mins)

        right_max = 0
        maxes = [0] * len(prices)

        for i in range(len(prices)-1, -1, -1):
            if i == len(prices) - 1:
                maxes[i] = 0
            else:
                maxes[i] = right_max
            right_max = max(right_max, prices[i])

        print('----Maxes----')
        print(maxes)

        best = 0
        for i in range(len(prices)):
            best = max(best, (maxes[i] - mins[i]))
        return best


if __name__ == '__main__':
    s = Solution()
    s.maxProfit([7, 1, 5, 3, 6, 4])
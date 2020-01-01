from typing import List


# Runtime: 892 ms, faster than 81.51% of Python3 online submissions for Distribute Candies.
# Memory Usage: 14.5 MB, less than 91.67% of Python3 online submissions for Distribute Candies.
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        unique_candy_values = len(set(candies))
        half_size = len(candies)//2
        return min(unique_candy_values, half_size)

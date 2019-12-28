"""
347. Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from typing import List


# Runtime: 104 ms, faster than 94.83% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 17.3 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        most_frq = sorted(frequencies.items(), key=lambda kv: kv[1], reverse=True)
        result = []
        for i in range(k):
            result.append(most_frq[i][0])
        return result


if __name__ == '__main__':
    s = Solution()
    s.topKFrequent([1,1,1,2,2,3], 2)
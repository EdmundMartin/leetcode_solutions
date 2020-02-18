"""
215. Kth Largest Element in an Array
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:

You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]


# Runtime: 60 ms, faster than 92.18% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Kth Largest Element in an Array.
class SolutionHeap:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for el in nums:
            heapq.heappush(heap, el)
        for i in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop()


# Too Slow
class SolutionQuicksort:

    def quicksort(self, array: List[int]):
        if len(array) == 0:
            return []
        if len(array) == 1:
            return array
        pivot = array[0]
        smaller = []
        partition = [pivot]
        larger = []
        for i in range(1, len(array)):
            if array[i] == pivot:
                partition.append(array[i])
            elif array[i] > pivot:
                larger.append(array[i])
            else:
                smaller.append(array[i])
        return self.quicksort(smaller) + partition + self.quicksort(larger)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = self.quicksort(nums)
        return result[-k]

from typing import List


# Runtime: 364 ms, faster than 96.70% of Python3 online submissions for Minimum Absolute Difference.
# Memory Usage: 26.8 MB, less than 100.00% of Python3 online submissions for Minimum Absolute Difference.
class Solution:

    def min_difference(self, arr: List[int]):
        min_diff = float('inf')
        last = arr[0]
        for i in range(1, len(arr)):
            diff = abs(arr[i] - last)
            if diff < min_diff:
                min_diff = diff
            last = arr[i]
        return min_diff

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        min_diff = self.min_difference(arr)
        last = arr[0]
        result = []
        for i in range(1, len(arr)):
            diff = abs(arr[i] - last)
            if diff == min_diff:
                result.append([last, arr[i]])
            last = arr[i]
        return result


if __name__ == '__main__':
    s = Solution()
    s.minimumAbsDifference([4,2,1,3])
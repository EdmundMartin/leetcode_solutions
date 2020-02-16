from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        even = total_length % 2 == 0
        middle = total_length // 2
        joined = []
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                joined.append(nums1.pop(0))
            else:
                joined.append(nums2.pop(0))
            if len(joined) == middle:
                break
        if len(nums1) > 0:
            joined.extend(nums1)
        else:
            joined.extend(nums2)
        print(joined)
        if even:
            return (joined[middle] + joined[middle-1]) / 2
        return joined[middle]


if __name__ == '__main__':
    s = Solution()
    res = s.findMedianSortedArrays([1, 3], [2])
    print(res)
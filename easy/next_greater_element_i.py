"""
496. Next Greater Element I
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]

Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        results = []
        nums2 = sorted(nums2)
        for number in nums1:
            if number not in nums2:
                results.append(-1)
            idx = nums2.index(number)
            found = False
            for i in range(idx, len(nums2)):
                if nums2[i] > number:
                    results.append(nums2[i])
                    found = True
                    break
            if not found:
                results.append(-1)
        return results


class OptimisedSolution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s2 = {number: index for index, number in enumerate(nums2)}
        result = []
        for item in nums1:
            num2_idx = s2[item]
            temp_max = item
            for j in range(num2_idx + 1, len(nums2)):
                if nums2[j] > temp_max:
                    temp_max = nums2[j]
                    break
            if temp_max == item:
                result.append(-1)
            else:
                result.append(temp_max)
        return result


if __name__ == '__main__':
    s = Solution()
    res = s.nextGreaterElement([4,1,2], [1,3,4,2])
    print(res)
from typing import List


# Runtime 52ms
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            other = target - nums[i]
            if i + 1 < len(nums):
                temp = nums[:i] + nums[i+1:]
            else:
                temp = nums[:i]
            if other in temp:
                return [i, nums.index(other)]
        return []


if __name__ == '__main__':
    s = Solution()
    result = s.twoSum([3, 2, 4], 6)
    print(result)
    assert result == [1, 2]
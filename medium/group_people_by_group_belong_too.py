"""
1282. Group the People Given the Group Size They Belong To
There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group.
Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are
and the people's IDs each group includes.

You can return any solution in any order and the same applies for IDs. Also, it is guaranteed
that there exists at least one solution.


Example 1:
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation:
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

Example 2:
Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]

Constraints:

groupSizes.length == n
1 <= n <= 500
1 <= groupSizes[i] <= n
"""
from typing import List


# Runtime: 72 ms, faster than 93.00% of Python3 online submissions for Group the People Given the Group Size They Belong To.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Group the People Given the Group Size They Belong To.
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        for idx, group_size in enumerate(groupSizes):
            if group_size in groups:
                groups[group_size].append(idx)
            else:
                groups[group_size] = [idx]

        result = []

        for size, values in groups.items():
            total_groups = len(values) // size
            if total_groups == 1:
                result.append(values)
            else:
                for i in range(0, len(values), size):
                    result.append(values[i: i + size])
        return result

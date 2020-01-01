"""
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as
the sum of all the node values formed by the subtree rooted at that node (including the node itself).
So what is the most frequent subtree sum value? If there is a tie, return all the values
with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.

Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.

Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
"""
from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 44 ms, faster than 94.61% of Python3 online submissions for Most Frequent Subtree Sum.
# Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Most Frequent Subtree Sum.
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        self.sums = defaultdict(int)
        self.max_freq = 0
        self.max_vals = []

        def post_order(node: TreeNode):
            if not node:
                return 0
            subtree_sum = node.val + post_order(node.left) + post_order(node.right)
            self.sums[subtree_sum] += 1
            if self.sums[subtree_sum] > self.max_freq:
                self.max_freq = self.sums[subtree_sum]
                self.max_vals = [subtree_sum]
            elif self.sums[subtree_sum] == self.max_freq:
                self.max_vals.append(subtree_sum)

            return subtree_sum

        post_order(root)
        return self.max_vals

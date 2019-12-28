"""
559. Maximum Depth of N-ary Tree
Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5

Constraints:
The depth of the n-ary tree is less than or equal to 1000.
The total number of nodes is between [0, 10^4].
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Runtime: 40 ms, faster than 98.78% of Python3 online submissions for Maximum Depth of N-ary Tree.
# Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Maximum Depth of N-ary Tree.
class Solution:
    def maxDepth(self, root: Node) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            current_node, depth = stack.pop()
            max_depth = max(depth, max_depth)
            new_depth = depth + 1
            if current_node.children:
                for child in current_node.children:
                    stack.append((child, new_depth))
        return max_depth


if __name__ == '__main__':
    n = Node(10)
    n.children = [Node(10), Node(12)]
    s = Solution()
    res = s.maxDepth(n)
    print(res)
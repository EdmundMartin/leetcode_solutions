"""
129. Sum Root to Leaf Numbers
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
Note: A leaf is a node with no children.

Example:
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 32 ms, faster than 87.26% of Python3 online submissions for Sum Root to Leaf Numbers.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Sum Root to Leaf Numbers.
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        stack = [(root, [])]
        total = 0
        while stack:
            current_node, num_list = stack.pop()
            if current_node.left is not None:
                stack.append((current_node.left, num_list + [current_node.val]))
            if current_node.right is not None:
                stack.append((current_node.right, num_list + [current_node.val]))

            if current_node.left is None and current_node.right is None:
                num_list.append(current_node.val)
                total += int(''.join([str(i) for i in num_list]))
        return total


if __name__ == '__main__':
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    s = Solution()
    res = s.sumNumbers(t)
    print(res)
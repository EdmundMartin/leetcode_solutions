"""
1367. Linked List in Binary Tree
Given a binary tree root and a linked list with head as the first node.

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in
the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.


Example 1:
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.

Example 2:
Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true

Example 3:
Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.


Constraints:
1 <= node.val <= 100 for each node in the linked list and binary tree.
The given linked list will contain between 1 and 100 nodes.
The given binary tree will contain between 1 and 2500 nodes.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Runtime: 96 ms, faster than 100.00% of Python3 online submissions for Linked List in Binary Tree.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Linked List in Binary Tree.
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        linked_list = ","
        current = head
        while current:
            linked_list += "{},".format(current.val)
            current = current.next

        queue = [(root, ",")]

        while queue:
            current_node, path = queue.pop(0)
            n_path = path
            n_path += "{},".format(current_node.val)
            if linked_list in n_path:
                return True
            if current_node.left:
                queue.append((current_node.left, n_path))
            if current_node.right:
                queue.append((current_node.right, n_path))
        return False

"""
328. Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Runtime: 44 ms, faster than 66.50% of Python3 online submissions for Odd Even Linked List.
# Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Odd Even Linked List.
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        start = head
        odd = []
        even = []
        count = 1
        while head:
            if count % 2 == 0:
                even.append(head)
            else:
                odd.append(head)
            head = head.next
            count += 1
        for i in range(len(odd) - 1):
            odd[i].next = odd[i+1]
        if even:
            odd[-1].next = even[0]
            even[-1].next = None
        for i in range(len(even) - 1):
            even[i].next = even[i+1]
        return start


if __name__ == '__main__':
    "1->2->3->4->5->NULL"
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next = ListNode(5)

    s = Solution()
    s.oddEvenList(head)
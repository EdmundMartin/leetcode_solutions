"""
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node,
and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need
one more attribute prev to indicate the previous node in the linked list.
Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:
get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.

addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion,
the new node will be the first node of the linked list.

addAtTail(val) : Append a node of value val to the last element of the linked list.

addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the
length of linked list, the node will be appended to the end of linked list. If index is greater than the length,
the node will not be inserted.

deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.


Example:
Input:
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]

Output:
[null,null,null,null,2,null,3]
"""


# Runtime: 124 ms, faster than 95.08% of Python3 online submissions for Design Linked List.
# Memory Usage: 13.7 MB, less than 12.50% of Python3 online submissions for Design Linked List.
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        # If index in first half of list move forward
        if index < self.length // 2:
            current = self.head
            for i in range(index):
                current = current.next
            return current.value
        current = self.tail
        for i in range(self.length- index - 1):
            current = current.prev
        return current.value

    def addAtHead(self, val: int) -> None:
        self.length += 1
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            tmp = self.head
            new_node.next = tmp
            tmp.prev = new_node
            self.head = new_node

    def addAtTail(self, val: int) -> None:
        self.length += 1
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            tmp = self.tail
            tmp.next = new_node
            new_node.prev = tmp
            self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)
        if index == self.length:
            return self.addAtTail(val)
        if index > self.length:
            return

        new_node = Node(val)
        if index < self.length // 2:
            current = self.head
            for i in range(index - 1):
                current = current.next
        else:
            current = self.tail
            for i in range(self.length - index):
                current = current.prev

        new_node.next = current.next
        current.next = new_node
        new_node.prev = current
        new_node.next.prev = new_node

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return

        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None

            self.length -= 1
            return

        if index < self.length // 2:
            current = self.head
            for i in range(index - 1):
                current = current.next
        else:
            current = self.tail
            for i in range(self.length - index):
                current = current.prev

        if current.next == self.tail:
            self.tail = current

        current.next = current.next.next
        if current.next is not None:
            current.next.prev = current
        self.length -= 1
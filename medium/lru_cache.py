"""
146. LRU Cache
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the
following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
from typing import Dict


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"<Node, Key:{self.key}, Value:{self.val}>"


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node: Node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            head = node
            head.next = self.head
            self.head.prev = head
            self.head = head

    def remove(self, node: Node):
        if node == self.head:
            if node.next:
                self.head = node.next
            else:
                self.head = None
            return
        if node == self.tail:
            if node.prev:
                self.tail = node.prev

        next_node = node.next
        prev_node = node.prev
        if next_node:
            next_node.prev = prev_node
        if prev_node:
            prev_node.next = next_node

    def iterate_list(self):
        node = self.head
        while node:
            print(node.key, node.val)
            node = node.next
        return


# Runtime: 236 ms, faster than 42.16% of Python3 online submissions for LRU Cache.
# Memory Usage: 22.4 MB, less than 6.06% of Python3 online submissions for LRU Cache.
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.link_list = DoubleLinkedList()
        self.node_map: Dict[int, Node] = {}

    def get(self, key: int) -> int:
        node = self.node_map.get(key)
        if not node:
            return -1
        result = node.val
        self.link_list.remove(node)
        self.link_list.add(node)
        return result

    def put(self, key: int, value: int) -> None:
        node = self.node_map.get(key)
        if node:
            node.val = value
            self.link_list.remove(node)
            self.link_list.add(node)
        else:
            if len(self.node_map) == self.capacity:
                tail_val = self.link_list.tail
                self.node_map.pop(tail_val.key)
                self.link_list.remove(tail_val)
            new_node = Node(key, value)
            self.node_map[key] = new_node
            self.link_list.add(new_node)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    res = cache.get(1)  # returns 1
    print(res)
    cache.put(3, 3)  # evicts key 2
    res = cache.get(2)  # returns - 1(not found)
    print(res)
    cache.put(4, 4)  # evicts key 1
    res = cache.get(1)  # returns - 1(not found)
    print(res)
    print(cache.node_map)
    res = cache.get(3)  # returns 3
    print(res)
    res = cache.get(4)  # returns 4
    print(res)
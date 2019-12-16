# Leetcode Problem
#  - id: 138
#  - title: Copy List with Random Pointer
#  - url: https://leetcode.com/problems/copy-list-with-random-pointer/
#  - difficulty: medium
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        heap = {}
        new_head = self._allocate_node(heap, head.val, id(head))
        p = head
        p_copy = new_head
        while p:
            # Copy next.
            if p.next:
                p_copy.next = self._allocate_node(heap, p.next.val, id(p.next))
            # Copy random.
            if p.random:
                p_copy.random = self._allocate_node(heap, p.random.val,
                                                    id(p.random))

            p = p.next
            p_copy = p_copy.next

        return new_head

    def _allocate_node(self, heap: dict, val: int, addr: int) -> 'Node':
        if addr in heap:
            return heap[addr]

        node = Node(val, None, None)
        heap[addr] = node
        return node

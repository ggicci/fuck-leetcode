# Leetcode Problem #19 - Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n <= 0:
            return head

        p = head
        q = head

        # 1. Move q for n steps ahead.
        while n and q:
            q = q.next
            n -= 1

        if not q:
            if n <= 0:
                # The length of the list is just of n.
                # So we only need to remove the head.
                return p.next

        # 2. Move p, q simultaneously, until q reach the end.
        while True:
            q = q.next
            if not q:
                break
            p = p.next

        # 3. Remove the next node of p.
        p.next = p.next.next
        return head

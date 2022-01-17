# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def dump(self, head):
        while head:
            print(head.val, end=' -> ')
            head = head.next
        print(None)

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = start = ListNode(None)
        root.next = head
        for _ in range(left - 1):
            start = start.next
        else:
            end = start.next

        for _ in range(right - left):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp

        return root.next














s = Solution()
input = ListNode(5)
s.reverseBetween(input, 1, 1)

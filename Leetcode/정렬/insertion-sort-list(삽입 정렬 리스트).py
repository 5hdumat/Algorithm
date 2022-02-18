# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
import sys
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def dump(self, l1):
        while l1:
            print(l1.val, end='')
            if l1.next:
                print(' -> ', end='')
            l1 = l1.next
        print()

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode()

        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            if head and cur.val > head.val:
                cur = parent

        return self.dump(parent.next)


s = Solution()
s.insertionSortList(
    ListNode(6, ListNode(5, ListNode(3, ListNode(1, ListNode(8, ListNode(7, ListNode(2, ListNode(4)))))))))

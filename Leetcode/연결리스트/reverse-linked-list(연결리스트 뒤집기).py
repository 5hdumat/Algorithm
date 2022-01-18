# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            next, head.next = head.next, prev
            head, prev = next, head

        # self.dump(prev)
        return prev

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node, prev=None):
            if not node:
                return prev

            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)


s = Solution()

input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
lists = s.reverseList(input)
s.dump(lists)

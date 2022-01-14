# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import functools
from operator import add
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def dump(self, l1):
        while l1:
            print(l1.val, end=' -> ')
            l1 = l1.next
        print(None)

    def reverse(self, node):
        prev = None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    def toList(self, node):
        ans = []

        while node:
            ans.append(node.val)
            node = node.next

        return ans

    def toReversedLinkedList(self, res):
        prev = None
        for x in res:
            node = ListNode(x)
            node.next = prev
            prev = node

        return node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverse(l1))
        b = self.toList(self.reverse(l2))
        res = functools.reduce(lambda x, y: x * 10 + y, a, 0) + functools.reduce(lambda x, y: x * 10 + y, b, 0)

        return self.toReversedLinkedList(str(res))


s = Solution()

input1 = ListNode(2, ListNode(4, ListNode(3, None)))
input2 = ListNode(5, ListNode(6, ListNode(4, None)))
s.addTwoNumbers(input1, input2)

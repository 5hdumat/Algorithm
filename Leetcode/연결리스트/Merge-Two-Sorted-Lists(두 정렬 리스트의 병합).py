# https://leetcode.com/problems/merge-two-sorted-lists/
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass


s = Solution()

input1 = ListNode(1, ListNode(2, ListNode(4, None)))
input2 = ListNode(1, ListNode(3, ListNode(4, None)))

s.mergeTwoLists(input1, input2)

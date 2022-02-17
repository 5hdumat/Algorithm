# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
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

    def mergeTwoLists(self, l1, l2):
        if not l1 or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1

        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        # 러너 기법을 활용해 피벗 구하기
        pivot, slow, fast = None, head, head
        while fast and fast.next:
            pivot, slow, fast = slow, slow.next, fast.next.next

        # -1 -> 5 / 0 -> 3 -> 4 으로 리스트 자르기
        pivot.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)


s = Solution()
sort_list = s.sortList(ListNode(-1, ListNode(5, ListNode(0, ListNode(3, ListNode(4))))))
s.dump(sort_list)

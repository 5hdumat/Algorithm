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

    def mergeToLists(self, l1, l2):
        # l1이 존재하지 않거나 l2가 존재하는데 l1값보다 작으면 스왑
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1

        if l1:
            l1.next = self.mergeToLists(l1.next, l2)

        return l1

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 원소가 한개일때까지 분리 후 리턴 (head는 존재하지만 head.next가 존재하지 않으면)
        if not (head and head.next):
            return head

        pivot, slow, fast = None, head, head

        # 러너 기법 활용 (패스트가 연결리스트의 끝에 도달하면 반복문을 멈춘다.)
        while fast and fast.next:
            pivot, slow, fast = slow, slow.next, fast.next.next
        pivot.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        # 분리된 요소를 병합
        return self.mergeToLists(l1, l2)


s = Solution()
sort_list = s.sortList(ListNode(-1, ListNode(5, ListNode(0, ListNode(3, ListNode(4))))))

# https://leetcode.com/problems/swap-nodes-in-pairs/

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

    def print(self, head):
        if head is not None:
            print(head.val)

    # 연결 리스트 노드를 변경
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # self.dump(head)
        root = prev = ListNode(None)

        prev.next = head
        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head

            prev.next = tmp

            head = head.next
            prev = prev.next.next

        return root.next

    def swapParisRecur(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next

            head.next = self.swapParisRecur(p.next)
            p.next = head
            return p

        return head

    # 연결 리스트의 노드 값만 변경 (노드의 값만 변경하는건 단순한 구조의 노드일 경우에만 가능하므로 권장 X)
    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        # self.dump(head)
        return head


s = Solution()

input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
recur = s.swapParisRecur(input)

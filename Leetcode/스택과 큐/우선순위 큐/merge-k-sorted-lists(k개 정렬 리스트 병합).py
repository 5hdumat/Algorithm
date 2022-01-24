# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from typing import List, Optional


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

    # 객체를 힙과 우선순위 큐에 추가할 경우에는 정렬의 기준이 무엇인지, 즉 어떻게 대소 비교를 해야할지를 명시적으로 알려줘야 합니다.
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode()
        heap = []

        for i in range(len(lists)):
            # 비어있는 연결리스트 예외처리
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            heappop = heapq.heappop(heap)
            idx = heappop[1]
            result.next = heappop[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        self.dump(root.next)

s = Solution()
s.mergeKLists([ListNode(1, ListNode(4, ListNode(5, None))),
               ListNode(1, ListNode(3, ListNode(4, None))),
               ListNode(2, ListNode(6, None))])

# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 빈 역순 연결리스트 생성
        cur = None
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            cur, cur.next, slow = slow, cur, slow.next

        '''
        연결리스트의 노드가 홀수라면 중앙값은 비교대상이 아니므로 slow를 한칸 민다.

            *
        1 2 3 2 1

        이렇게되면 3, 2, 1 로 비교가 될테니

              *
        1 2 3 2 1

        이렇게 한칸 밀어서 2, 1 로 비교하자는 의미이다. (연결리스트 cur과 slow가 동일하면 True)
        '''
        if fast:
            slow = slow.next

        while cur and cur.val == slow.val:
            cur, slow = cur.next, slow.next

        return not cur

    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        # 연결리스트의 리스트화
        q = deque()

        if head is None:
            return True

        while head is not None:
            q.append(head.val)
            head = head.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        else:
            return True


s = Solution()
input = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1, None)))))
s.isPalindrome(input)

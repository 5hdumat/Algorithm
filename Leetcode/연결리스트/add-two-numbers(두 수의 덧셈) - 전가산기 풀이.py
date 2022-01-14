# https://leetcode.com/problems/add-two-numbers/

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

    def dump(self, l1):
        while l1:
            print(l1.val, end=' -> ')
            l1 = l1.next
        print(None)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0

            # 전가산기로 치면 A와 B를 더하는 것과 같음
            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            # A + B + C(carry, 자리올림수) 를 전가산기 10진수로 표현
            # 몫을 자리올림수, 나머지를 값으로 쓴다.
            carry, val = divmod(sum + carry, 10)

            head.next = ListNode(val)
            head = head.next

        return root.next

s = Solution()

input1 = ListNode(2, ListNode(4, ListNode(3, None)))
input2 = ListNode(5, ListNode(6, ListNode(4, None)))
s.addTwoNumbers(input1, input2)

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


'''
pass 0

1 -> 2 -> 4
1 -> 3 -> 4

pass 1
1

2 -> 4
1 -> 3 -> 4

pass 2

1

1 -> 3 -> 4
2 -> 4

pass 3

1 -> 1

3 -> 4
2 -> 4

pass 4

1 -> 1

2 -> 4
3 -> 4

pass 5

1 -> 1 -> 2

4
3 -> 4

pass 6

1 -> 1 -> 2 

3 -> 4
4

pass 7

1 -> 1 -> 2 -> 3

4
4

pass 8

1 -> 1 -> 2 -> 3

None
4

pass 9


1 -> 1 -> 2 -> 3 -> 4 

4
None


pass 10


1 -> 1 -> 2 -> 3 -> 4 -> 4

None
None


pass 11


1 -> 1 -> 2 -> 3 -> 4 -> 4

None
None

'''


class Solution:
    def dump(self, l1):
        while l1:
            print(l1.val, end=' -> ')
            l1 = l1.next
        print(None)

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1

        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1


s = Solution()

input1 = ListNode(1, ListNode(1, ListNode(1, None)))
input2 = ListNode(1, ListNode(3, ListNode(4, None)))

lists = s.mergeTwoLists(input1, input2)
s.dump(lists)

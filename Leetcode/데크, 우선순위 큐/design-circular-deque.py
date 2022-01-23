# https://leetcode.com/problems/design-circular-deque/
class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev or self
        self.next = next or self


class MyCircularDeque:
    def __init__(self, capacity: int):
        self.head = Node()
        self.capacity = capacity
        self.no = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(value, self.head, self.head.next)
        self.head.next.prev = node
        self.head.next = node
        self.no += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        # -> head -> 0 -> 1 -> 2
        node = Node(value, self.head.prev, self.head)
        self.head.prev.next = node
        self.head.prev = node
        self.no += 1

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        # head -> 1 -> 2
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.no -= 1

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        # head -> 1 -> 2
        self.head.prev.prev.next = self.head
        self.head.prev = self.head.prev.prev
        self.no -= 1

        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.next.data

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.head.prev.data

    def isEmpty(self) -> bool:
        return self.head.next is self.head

    def isFull(self) -> bool:
        return self.no >= self.capacity

# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(10)
param_1 = obj.insertFront(1)
print(param_1)
param_2 = obj.insertLast(2)
print(param_2)
# param_3 = obj.deleteFront()
param_4 = obj.deleteLast()
print(obj.getFront())
print(obj.getRear())
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

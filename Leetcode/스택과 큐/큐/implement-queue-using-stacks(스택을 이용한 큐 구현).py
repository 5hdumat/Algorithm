# https://leetcode.com/problems/implement-queue-using-stacks/
import collections


class MyQueue:

    def __init__(self):
        self.stack = []
        self.front = 0
        self.rear = -1
        self.no = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.rear += 1
        self.no += 1

    def pop(self) -> int:
        if not self.empty():
            x = self.stack[self.front]
            self.front += 1
            self.no -= 1
            return x

    def peek(self) -> int:
        if not self.empty():
            return self.stack[self.front]

    def empty(self) -> bool:
        return self.no == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

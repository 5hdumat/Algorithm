# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = 0
        self.no = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.queue[self.rear] = value
        self.rear += 1
        self.no += 1

        if self.rear == self.capacity:
            self.rear = 0

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front += 1
        self.no -= 1

        if self.front == self.capacity:
            self.front = 0

        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.no <= 0

    def isFull(self) -> bool:
        return self.no >= self.capacity

    def dump(self):
        if self.isEmpty():
            print('큐가 비어있습니다.')
        else:
            for i in range(self.no):
                index = (i + self.front) % self.capacity

                print(self.queue[index], end=' ')
            print()


# ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]
# [[3],[1],[2],[3],[4],[],[],[],[4],[]]
# [null,true,true,true,false,3,true,true,true,4]
# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
obj.enQueue(1)
obj.enQueue(2)
obj.enQueue(3)
obj.enQueue(4)
print(obj.Rear())
print(obj.isFull())
obj.deQueue()
obj.enQueue(4)
print(obj.Rear())
obj.dump()

# Problem: 622. Design Circular Queue
# Link: https://leetcode.com/problems/design-circular-queue/


class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        # the size of the queue is fixed: k
        self.front = self.rear = self.size = 0
        # keep track of the front index, rear index and size

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        capacity = len(self.queue)
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % capacity
        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.size -= 1
        capacity = len(self.queue)
        if self.isEmpty():
            self.rear = self.front = 0
        else:
            self.front = (self.front + 1) % capacity

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        index = (self.rear + len(self.queue) - 1) % len(self.queue)
        return self.queue[index]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.queue)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

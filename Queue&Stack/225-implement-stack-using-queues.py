# Problem: 225. Implement Stack using Queues
# Link: https://leetcode.com/problems/implement-stack-using-queues/

# Alternative solution
# Implement the stack using only one queue


# implement a queue class with the basic methods
class Queue:
    # method for initializing the queue
    def __init__(self):
        self.queue = []

    # methof for getting the size of the queue
    def size(self):
        return len(self.queue)

    # method that checkes if the queue is empty
    def is_empty(self):
        return self.size() == 0

    # method that return the front element
    def peek(self):
        return self.queue[0]

    # method for adding an element to the queue
    def enqueue(self, value):
        self.queue.append(value)

    # method for removing an element from the queue
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)


class MyStack:

    # initialize
    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        # push the new element
        self.queue.enqueue(x)

        # move all the elements below by dequeueing them and enqueuing them again
        # after the newest element
        # this reverses the order of the elements and keeps LIFO order of processing elements
        size = self.queue.size()
        for _ in range(size - 1):
            self.queue.enqueue(self.queue.dequeue())

    def pop(self) -> int:
        # dequeue if the queue is not empty
        if not self.queue.is_empty():
            return self.queue.dequeue()

    def top(self) -> int:
        if not self.queue.is_empty():
            return self.queue.peek()

    # all the elements are in the queue
    # to check if the stack is empty call the is_empty method of the queue
    def empty(self) -> bool:
        return self.queue.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# The solution that uses two queues
"""
# implement a queue class with the basic methods
class Queue:
    # method for initializing the queue
    def __init__(self):
        self.queue = []

    # method for getting the size of the queue
    def size(self):
        return len(self.queue)

    # method that checkes if the queue is empty
    def is_empty(self):
        return self.size() == 0

    # method that return the front element
    def peek(self):
        return self.queue[0]

    # method for adding an element to the queue
    def enqueue(self, value):
        self.queue.append(value)

    # method for rmeoving an element from the queue
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)


class MyStack:

    # initialize the stack
    def __init__(self):
        # main queue
        self.queue1 = Queue()
        # helper queue
        self.queue2 = Queue()

    # reverse the order of elements in queue1 by using helper queue2
    # in order to keep LIFO processing order of elements
    def push(self, x: int) -> None:
        # add the new element to queue2
        self.queue2.enqueue(x)

        # move all elements to queue2
        while not self.queue1.is_empty():
            self.queue2.enqueue(self.queue1.dequeue())
        # swap queues
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        # if queue1 is not empty, dequeue
        if not self.queue1.is_empty():
            return self.queue1.dequeue()

    def top(self) -> int:
        if not self.queue1.is_empty():
            return self.queue1.peek()

    def empty(self) -> bool:
        # all elements are in queue1, queue2 is only used as a helper queue
        return self.queue1.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
"""

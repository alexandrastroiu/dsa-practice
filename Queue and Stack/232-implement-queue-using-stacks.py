# Problem: 232. Implement Queue using Stacks
# Link: https://leetcode.com/problems/implement-queue-using-stacks/

# The solution using stack 2 for the dequeue operation is more efficient
# than the solution that uses stack 2 ony as a helper for reversing the order of elements in stack1


# implement a class for stack
class Stack:

    def __init__(self):
        self.stack = []

    # method for checking if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # method for pushing an element in the stack
    def push(self, value):
        self.stack.append(value)

    # method for removing the last element
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    # method for returning the value of the last element (top of the stack)
    def top(self):
        if not self.is_empty():
            return self.stack[-1]


# implement a class for queue using two stacks
# the implemented queue should support all the functions of a normal queue
class MyQueue:

    # initialize
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    # method for pushing an element to the queue
    # the end of stack1 acts as the end of the queue
    def push(self, x: int) -> None:
        self.stack1.push(x)

    # method for removing an element from the queue
    # in a queue elements are processed in FIFO order
    # in stack1 elements are processed in LIFO order (the first element is at position 0, second at 1)
    # we must reverse the elements using stack2 in order to simulate FIFO processing of elements
    def pop(self) -> int:
        # if there are no elements in stack2
        # push all elemnts from stack1 (first element in stack1 will be last in stack2)
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        # remove the last element (FIFO) - stack2 acts as the front of the queue
        return self.stack2.pop()

    # method for returning the value of the first element in the queue
    def peek(self) -> int:
        # if there are elements in stack 2
        # return the last element in stack 2
        if not self.stack2.is_empty():
            return self.stack2.stack[-1]
        # else return the first element from stack1
        return self.stack1.stack[0]

    # all elements of the queue. are either in stack1 or stack2
    # if both stacks are empty, then the queue is empty
    def empty(self) -> bool:
        return self.stack1.is_empty() and self.stack2.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

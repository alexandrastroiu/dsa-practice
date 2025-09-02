# Problem: 155. Min Stack
# Link: https://leetcode.com/problems/min-stack/


class MinStack:

    def __init__(self):
        self.stack = []
        # use a list to represent the stack
        self.minimum = []
        # use a list to keep track of the minimum element in the stack at each level

    def push(self, val: int) -> None:
        self.stack.append(val)
        # add a new element to the stack
        if len(self.minimum) == 0:
            self.minimum.append(val)
        # check if the new value is smaller than the minimum
        elif val < self.minimum[-1]:
            self.minimum.append(val)
        else:
            self.minimum.append(self.minimum[-1])

    def pop(self) -> None:
        # the pop operation will be called on non-empty stacks
        if len(self.stack) == 0:
            return
        self.stack.pop()
        # remove the element from the end of the list
        self.minimum.pop()
        # remove the last minimum element calculated

    def top(self) -> int:
        # the top operation will be called on non-empty stacks
        if len(self.stack) != 0:
            return self.stack[-1]
        # return the last element (top of the stack)

    def getMin(self) -> int:
        # the getMin operation will be called on non-empty stacks
        if len(self.stack) != 0:
            return self.minimum[-1]
        # return the current minimum value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Problem: 739. Daily Temperatures
# Link: https://leetcode.com/problems/daily-temperatures/


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
            self.stack.pop()

    # method for returning the value of the last element (top of the stack)
    def top(self):
        if not self.is_empty():
            return self.stack[-1]


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # answer list
        answer = [0] * len(temperatures)
        # initialize the stack
        stack = Stack()
        # current index
        index = 0

        # for each daily temperature
        for temp in temperatures:

            # check if the current temperatur is higher than those in the stack
            # indexes of temperatures for which a higher temperature was not found yet are in the stack
            while not stack.is_empty() and temperatures[stack.top()] < temp:
                answer[stack.top()] = index - stack.top()
                # complete the answer for temperatures with indexes in the stack
                stack.pop()
                # remove from the stack after the answer is completed

            stack.push(index)
            # push the index of the current temperature to the stack
            index += 1
            # update the index

        return answer
        # return the answer list

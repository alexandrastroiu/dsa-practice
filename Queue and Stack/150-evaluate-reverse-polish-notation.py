# Problem: 150. Evaluate Reverse Polish Notation
# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/


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


class Solution:
    # helper function
    def calculate(self, num1, num2, operator):
        match operator:
            case "+":
                return num1 + num2
            case "-":
                return num2 - num1
            case "*":
                return num1 * num2
            case "/":
                return int(num2 / num1)
                # division rounds to zero

    def evalRPN(self, tokens: List[str]) -> int:
        # initialize the stack
        stack = Stack()
        # the set contains the operators in a RPN expression
        operators = set(("+", "-", "*", "/"))

        # goes through all tokens
        for token in tokens:
            # if the current token is an operator
            if token in operators:
                # get the last 2 elemnts in the stack as operands
                operand1 = stack.pop()
                operand2 = stack.pop()
                # calculate the current expression and push the final value tot the stack
                stack.push(self.calculate(operand1, operand2, token))
            # the current token is an operand
            else:
                # push the value to the stack
                stack.push(int(token))

        return stack.top()
        # for a valid RPN expression there will be only one element left in the stack in the end
        # return the result of the expression

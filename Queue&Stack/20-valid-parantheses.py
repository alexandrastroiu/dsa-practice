# Problem: 20. Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/


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
    def isValid(self, s: str) -> bool:
        # set that contains the opening characters
        # using a set instead of a list for efficient look up (O(1))
        opening_chars = set(("(", "[", "{"))
        # set that contains the closing characters
        closing_chars = set((")", "]", "}"))
        # set that contains the opening-closing parantheses pairs
        # could also use a dictionary instead of a set for mapping
        pairs = set((("(", ")"), ("[", "]"), ("{", "}")))
        # initialize the stack
        stack = Stack()

        # traverse the input string character by character
        for character in s:
            # an opening character is added to the stack
            if character in opening_chars:
                stack.push(character)
            # when a closing character is found, check for
            # the corresponding opening character in the stack (the top)
            if character in closing_chars:
                if not stack.is_empty() and (stack.top(), character) in pairs:
                    stack.pop()
                    # pop the element from the stack if there is a pair
                else:
                    return False
                    # not a valid pair or the stack is empty

        return stack.is_empty()
        # after traversing a valid input string, the stack should be empty

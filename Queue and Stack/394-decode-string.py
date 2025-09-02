# Problem: 394. Decode String
# Link: https://leetcode.com/problems/decode-string/


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
    def decodeString(self, s: str) -> str:
        # initialize the stack
        st = Stack()

        # pass through all the characters in the encoded string
        for char in s:
            # all characters besides "]" are pushed to the stack
            if char != "]":
                st.push(char)
            # if a "]" character is found
            else:
                # decode the innermost substring
                # initially teh substring is empty
                substring = ""
                # remove characters from the stacl until the beginning of the expression ("[") is reached
                while st.top() != "[":
                    substring = st.pop() + substring
                    # account for LIFO processing order of the stack
                st.pop()
                # pop the "[" character
                k = ""
                # it is guaranteed that before "[" there is a number
                # while there are digits at the top of the stack
                while not st.is_empty() and st.top().isdigit():
                    k = st.pop() + k
                    # account for LIFO processing order of the stack when calculating k
                st.push(int(k) * substring)
                # all the elements related nested expression were removed from the stack
                # the result of the nested expression is pushed to the stack
                # strings that are not part of a nested expression (not in brackets) remain in the stack as they are

        return "".join(st.stack)
        # get the result string by using the join method and return it

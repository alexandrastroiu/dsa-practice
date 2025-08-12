# Problem: 20. 94. Binary Tree Inorder Traversal
# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

# Iterative solution using a stack


# implement a stack class
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def top(self):
        if not self.is_empty():
            return self.stack[-1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # initialize the stack
        stack = Stack()
        # start from the root
        current = root
        # the list that will be returned after traversal
        inorder = []

        # handle edge case: empty tree
        if root is None:
            return []

        while current or not stack.is_empty():
            while current:
                stack.push(current)
                current = current.left
                # keep moving in the left subtree until current reaches null

            current = stack.pop()
            inorder.append(current.val)
            # move to the right subtree of the last node
            current = current.right

        return inorder

# 430. Flatten a Multilevel Doubly Linked List
# Link: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


# recursive solution
class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        def flatten_list(previous_node, current_node):
            if current_node is None:
                return previous_node

            current_node.prev = previous_node
            previous_node.next = current_node
            next_node = current_node.next
            tail = flatten_list(current_node, current_node.child)
            current_node.child = None

            return flatten_list(tail, next_node)

        if head is None:
            return None

        dummy_node = Node(0, None, None, None)
        flatten_list(dummy_node, head)
        dummy_node.next.prev = None

        return dummy_node.next


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

# the iterative solution
"""
class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        # edge case
        if head is None:
            return head

        # traverse the linked list (starting with the first level)
        current_node = head
        while current_node:
            next_node = current_node.next

            # if there is a child node
            if current_node.child:
                node = current_node.child
                # find the tail of the level below
                while node.next:
                    node = node.next

                child_tail = node
                # connect the current_node with its child
                current_node.child.prev = current_node
                current_node.next = current_node.child
                # child pointer set to null
                current_node.child = None
                # connect the tail node of the child linked list with the original next node
                child_tail.next = next_node

                # if the next_node is not null change it prev field value
                if next_node:
                    next_node.prev = child_tail

            # move to the next node
            current_node = current_node.next

        # return the head of the flattened linked list
        return head
"""

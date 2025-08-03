# Problem: 138. Copy List with Random Pointer
# Link: https://leetcode.com/problems/copy-list-with-random-pointer/


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        new_head = previous = Node(x=0)
        current_node = head
        map_nodes = {}
        # solution that uses extra space to prevent creating multiple copies of the same node
        # keep mapping of old node -> new node

        if head is None:
            return None

        while current_node:
            node = Node(x=current_node.val)
            previous.next = node
            previous = node
            map_nodes[current_node] = node
            current_node = current_node.next

        previous.next = None
        current_node = head
        new_head = new_head.next

        while current_node:
            if current_node.random:
                map_nodes[current_node].random = map_nodes[current_node.random]
            else:
                map_nodes[current_node].random = None
            current_node = current_node.next

        return new_head

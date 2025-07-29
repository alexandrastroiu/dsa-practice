# Problem: 160. Intersection of Two Linked Lists
# Link: https://leetcode.com/problems/intersection-of-two-linked-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# the solution using a two-pointer technique
# O(m + n) time and O(1) memory
class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointer_a = headA
        pointer_b = headB

        while pointer_a != pointer_b:
            pointer_a = pointer_a.next if pointer_a else headB
            pointer_b = pointer_b.next if pointer_b else headA

        return pointer_a


# the solution using a hash set
# O(m + n) time, O(m) memory (because of the hash set)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""
class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        current_node = headA

        while current_node:
            visited.add(current_node)
            # visit the nodes starting from headA
            current_node = current_node.next

        current_node = headB

        while current_node:
            if current_node in visited:
                return current_node
            # return the common node between the two linked lists
            current_node = current_node.next

        return None  # the two linked lists do not intersect
"""

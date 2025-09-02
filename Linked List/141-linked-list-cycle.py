# Problem: 141. Linked List Cycle
# Link: https://leetcode.com/problems/linked-list-cycle/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's Tortoise and Hare algorithm (two-pointer technique)
        slow = fast = head
        # both the slow and fast pointer start at the head of the linked list

        # the fast pointer reaches null first if there is no cycle
        while fast and fast.next:
            slow = slow.next  # slow pointer moves 1 step at a time
            fast = fast.next.next  # fast pointer moves 2 steps at a time

            if slow == fast:
                return True  # the slow pointer and the fast pointer meet = there is a cycle

        return False  # there is no cycle in the linked list

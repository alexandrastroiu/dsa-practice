# Problem: 142. Linked List Cycle II
# Link: https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        # using a slow pointer and a fast pointer

        # the fast pointer could reach the end of the linked list first
        while fast and fast.next:
            slow = slow.next
            # the slow pointer moves 1 step at a time
            fast = fast.next.next
            # the fast pointer moves 2 times faster than the slow pointer

            if slow == fast:
                # if the slow pointer and the fast pointer meet, there is a cycle
                start = head
                # another pointer used to find the beginning of the cycle

                while start != slow:
                    start = start.next
                    slow = slow.next

                return start  # return the node where the cycle begins

        return None  # the linked list does not contain a cycle

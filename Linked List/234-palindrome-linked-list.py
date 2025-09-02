# Problem: 234. Palindrome Linked List
# Link: https://leetcode.com/problems/palindrome-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # two-pointer technique
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the list
        previous = None
        current_node = slow.next

        while current_node:
            next_node = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = next_node

        node1 = head
        node2 = previous

        while node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next

        return True

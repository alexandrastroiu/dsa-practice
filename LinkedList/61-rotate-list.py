# Problem: 61. Rotate List
# Link: https://leetcode.com/problems/rotate-list/

# the solution that has O(1) space complexity


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # handle edge cases
        if head is None or head.next is None:
            return head

        current_node = head
        count = 0

        while current_node:
            count += 1
            current_node = current_node.next

        k %= count
        # handle edge case
        if k == 0:
            return head

        # two-pointer technique
        fast = slow = head
        for _ in range(k):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        # the head of the new list
        rotated_list_head = slow.next
        slow.next = None
        fast.next = head

        return rotated_list_head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# solution that uses extra memory that depends on the input linked list
"""
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node_values = []
        current_node = head

        # edge case
        if head is None:
            return None

        while current_node:
            node_values.append(current_node.val)
            current_node = current_node.next

        length = len(node_values)
        k %= length
        result = [0] * length

        for i in range(length):
            result[(i + k) % length] = node_values[i]

        current_node = head
        i = 0
        while current_node:
            current_node.val = result[i]
            current_node = current_node.next
            i += 1

        return head
"""

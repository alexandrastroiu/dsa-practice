# Problem: 21. Merge Two Sorted Lists
# Link: https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        current_node1 = list1
        current_node2 = list2
        head = None
        previous = head

        # edge case ( both linked lists are empty)
        if list1 is None and list2 is None:
            return None

        while current_node1 and current_node2:
            if current_node1.val < current_node2.val:
                if head is None:
                    head = current_node1
                else:
                    previous.next = current_node1
                previous = current_node1
                current_node1 = current_node1.next
            else:
                if head is None:
                    head = current_node2
                else:
                    previous.next = current_node2
                previous = current_node2
                current_node2 = current_node2.next

        while current_node1:
            if head is None:
                head = current_node1
            else:
                previous.next = current_node1
            previous = current_node1
            current_node1 = current_node1.next

        while current_node2:
            if head is None:
                head = current_node2
            else:
                previous.next = current_node2
            previous = current_node2
            current_node2 = current_node2.next

        previous.next = None

        return head

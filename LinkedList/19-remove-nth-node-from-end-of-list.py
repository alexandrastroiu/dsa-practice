# Problem: 19. Remove Nth Node From End of List
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# the solution using the two-pointer technique


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(next=head)
        # use a dummy node in order to simplify edge cases
        fast = slow = dummy_node
        # two-pointer technique

        for _ in range(n):
            fast = fast.next

        # until the fast pointer reaches the last node of the linked list
        while fast.next:
            slow = slow.next
            fast = fast.next

        # the slow pointer will point to the node before the nth node from the list
        slow.next = slow.next.next
        # delete the nth node from the end of the list
        return dummy_node.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# alternative solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        current_node = head
        count = 0

        while current_node:
            count += 1
            # count the total number of nodes in the linked list
            current_node = current_node.next

        deleted_index = count - n
        # the index of the node that will be deleted

        # edge case: deleting the first node
        if deleted_index == 0:
            head = head.next
        else:
            predecessor = head

            for _ in range(deleted_index - 1):
                predecessor = predecessor.next

            predecessor.next = predecessor.next.next

        return head

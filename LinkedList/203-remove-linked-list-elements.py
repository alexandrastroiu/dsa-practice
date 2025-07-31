# Problem: 203. Remove Linked List Elements
# Link: https://leetcode.com/problems/remove-linked-list-elements/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        # use a dummy node in order to simplify edge cases
        current_node = dummy
        
        while current_node:
            # handle consecutive nodes with the value val
            while current_node.next and current_node.next.val == val:
                current_node.next = current_node.next.next
                
            current_node = current_node.next
        
        return dummy.next
# Problem: 2. Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = l1
        previous = ListNode(next=head)
        carry = 0
        # account for carry

        while l1 and l2:
            current_sum = ((l1.val + l2.val) % 10 + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            l1.val = current_sum
            previous.next = l1
            previous = l1
            l1 = l1.next
            l2 = l2.next

        # while there are digits left in the first number
        while l1:
            current_sum = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            l1.val = current_sum
            previous.next = l1
            previous = l1
            l1 = l1.next

        # while there are digits left in the second number
        while l2:
            current_sum = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            l2.val = current_sum
            previous.next = l2
            previous = l2
            l2 = l2.next

        # add an extra node to the list if carry is one at the end
        if carry == 1:
            previous.next = ListNode(val=1)

        return head

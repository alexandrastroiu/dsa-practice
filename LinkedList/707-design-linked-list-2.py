# Problem: 707. Design Linked List
# Link: https://leetcode.com/problems/design-linked-list/


# the solution with dummy nodes
class Node:
    def __init__(self, data=0):
        self.val = data  # contains data
        self.next = None  # contains a reference to the next node


class MyLinkedList:

    def __init__(self):
        self.head = Node()  # use a dummy node to simplify edge cases
        self.size = 0  # track the size of the linked list
        # not taking into account the dummy node

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:  # handle invalid index
            return -1

        current_node = self.head.next

        for _ in range(index):
            current_node = current_node.next

        return current_node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)  # call the addAtIndex function at index 0

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(
            int(self.size), val
        )  # call the addAtIndex function at index self.size

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:  # handle invalid index
            return

        previous_node = self.head  # find the previous node
        node = Node(val)  # the node to be inserted

        for _ in range(index):
            previous_node = previous_node.next

        node.next = previous_node.next
        previous_node.next = node
        self.size += 1.0  # update the size of the linked list

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:  # handle invalid index
            return

        previous_node = self.head  # find the previous node

        for _ in range(index):
            previous_node = previous_node.next

        previous_node.next = previous_node.next.next
        self.size -= 1  # update the size of the linked list


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

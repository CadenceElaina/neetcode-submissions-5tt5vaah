# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) #value of node can be zer obut next pointer is set to head of list - insert at begin
        left = dummy
        #right = head + n  - use loop
        right = head
        while n > 0 and right: # n must be > 0 and right cannot be null - if so shift right
            right = right.next
            n -= 1
        
        # shift both pointers now - until right reaches end of the list (null/none)
        while right:
            left = left.next
            right = right.next
        
        # Left finishes on the node before the node to remove
        # to remove change next pointer to the node ahead of the one to be removed
        left.next = left.next.next
        return dummy.next # we dont want to add a node (dummy starts behind the LL)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head

        while n > 0 and r: 
            r = r.next
            n-=1

        # shift both pointers until r reaches end of list
        while r:
            l = l.next
            r = r.next
        # we need n spaces between l and r ptr so that l ends on node thats one before the one to remove once r reaches null/none (end of list)
        

        # since l finishes on node before one to remove we just set its next ptr to the node ahead of the one removed
        l.next = l.next.next
        return dummy.next